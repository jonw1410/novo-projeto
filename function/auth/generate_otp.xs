// Gera um código OTP de 6 dígitos e salva no banco de dados para o email fornecido
// Gera um código OTP de 6 dígitos e salva no banco de dados para o email fornecido
function "auth/generate_otp" {
  input {
    // Email do usuário para o qual o OTP será gerado
    email email filters=trim|lower
  }

  stack {
    // Deleta OTPs antigos para este email
    db.bulk.delete userOTP {
      where = $db.userOTP.Email == $input.email
    } as $deleted
  
    // Gera um código aleatório de 6 dígitos
    security.random_number {
      min = 100000
      max = 999999
    } as $otp_code
  
    // Define a expiração para 10 minutos a partir de agora
    var $expires_at {
      value = now
        |transform_timestamp:"+10 minutes"
    }
  
    // Salva o novo OTP no banco de dados
    db.add userOTP {
      enforce_hidden_fields = false
      data = {
        Email         : $input.email
        OTP_CODE      : $otp_code|to_text
        OTP_EXPIRES_AT: $expires_at
      }
    } as $otp_record
  }

  response = $otp_code|to_text
  guid = "FNRZox8f0gxjsXgeusW7Y2DVkKA"
}