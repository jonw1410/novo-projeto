// Solicita um código OTP por e-mail para autenticação
query otp_envio_email verb=POST {
  api_group = "Authentication"

  input {
    // Email do usuário que deseja receber o OTP
    email email filters=trim|lower
  }

  stack {
    // Gera um código de 6 dígitos
    security.create_password {
      character_count = 6
      require_lowercase = false
      require_uppercase = true
      require_digit = true
      require_symbol = false
      symbol_whitelist = ""
    } as $codigo_OTP
  
    // Define a expiração para 5 minutos (300 segundos)
    var $expiracao {
      value = `now`|add_secs_to_timestamp:300
    }
  
    // Salva o código no banco de dados
    db.add userOTP {
      enforce_hidden_fields = false
      data = {
        Email         : $input.email
        OTP_CODE      : $codigo_OTP
        OTP_EXPIRES_AT: $expiracao
      }
    } as $userOTP1
  
    // Prepara os dados para o template dinâmico do SendGrid
    var $pacote_email {
      value = {OTP_CODE: $userOTP1.OTP_CODE}
    }
  
    // Envia o e-mail usando o template dinâmico
    function.run sendgrid_dynamic_send {
      input = {
        to_email   : $input.email
        template_id: "d-0e631a0710774ae2a3b40b74ae80433d"
        data       : $pacote_email
      }
    } as $func1
  }

  response = $userOTP1
}