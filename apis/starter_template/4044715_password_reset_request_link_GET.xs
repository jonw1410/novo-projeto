// Endpoint for requesting a password reset link
query "password_reset/request-link" verb=GET {
  api_group = "Starter Template"

  input {
    email email?
  }

  stack {
    function.run generate_magic_link_pw_reset {
      input = {email: $input.email}
    } as $pw_reset_magic_link
  
    precondition ($pw_reset_magic_link != null) {
      error = "Magic link could not be created. Try again."
    }
  
    function.run sendgrid_dynamic_send {
      input = {
        to_email   : $input.email
        template_id: $env.sendgrid_pw_reset_template
        data       : {}|set:"magic_link":$pw_reset_magic_link
      }
    } as $sendgrid_send_magic_link
  }

  response = {
    message: {}|set:"success":true|set:"message":"magic link sent"
  }
}