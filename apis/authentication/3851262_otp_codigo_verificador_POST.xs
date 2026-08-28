// Verifica o código OTP e retorna um token de autenticação
// Verifica o código OTP e retorna um token de autenticação
query otp_codigo_verificador verb=POST {
  api_group = "Authentication"

  input {
    // Email do usuário
    email email filters=trim|lower
  
    // Código OTP recebido
    text otp filters=trim
  }

  stack {
    // Busca o OTP no banco de dados
    db.query userOTP {
      where = $db.userOTP.Email == $input.email && $db.userOTP.OTP_CODE == $input.otp && $db.userOTP.OTP_EXPIRES_AT > now
      return = {type: "single"}
    } as $otp_record
  
    // Valida se o OTP é válido
    precondition ($otp_record != null) {
      error_type = "inputerror"
      error = "Código OTP inválido ou expirado."
    }
  
    // Busca o usuário ou cria um novo
    db.get usuarios {
      field_name = "email"
      field_value = $input.email
    } as $user
  
    conditional {
      if ($user == null) {
        // Cria novo usuário (auto-signup)
        db.add usuarios {
          enforce_hidden_fields = false
          data = {
            email: $input.email
            name : $input.email|split:"@"|first
          }
        } as $user
      }
    }
  
    // Gera o token de autenticação
    security.create_auth_token {
      table = "usuarios"
      extras = {email: $user.email, role: $user.role}
      expiration = 86400
      id = $user.id
    } as $auth_token
  
    // Limpa o OTP usado
    db.bulk.delete userOTP {
      where = $db.userOTP.Email == $input.email
    } as $deleted
  }

  response = {authToken: $auth_token, user: $user}
}