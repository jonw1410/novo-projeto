// Envia o código OTP por e-mail usando o SendGrid
// Envia o código OTP por e-mail usando o SendGrid
function "auth/send_otp_email" {
  input {
    // Email do destinatário
    email email
  
    // Código OTP a ser enviado
    text otp
  }

  stack {
    // Monta a mensagem do e-mail
    var $body {
      value = "Seu código de verificação é: " ~ $input.otp ~ ". Ele expira em 10 minutos."
    }
  
    // Chama a função básica de envio do SendGrid
    function.run "" {
      input = {
        to_email: $input.email
        subject : "Seu Código de Verificação (OTP)"
        body    : $body
      }
    } as $send_result
  }

  response = null
}