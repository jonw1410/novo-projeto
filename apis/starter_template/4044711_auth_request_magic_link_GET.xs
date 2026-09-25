// The user requests a Magic Link via their Email address. Magic Links provide a user a method to login without a password.
query "auth/request-magic-link" verb=GET {
  api_group = "Starter Template"

  input {
    email email?
  }

  stack {
    function.run generate_magic_link {
      input = {email: $input.email}
    } as $magic_link
  
    precondition ($magic_link != null) {
      error = "Magic link could not be created. Try again."
    }
  
    function.run sendgrid_dynamic_send {
      input = {
        to_email   : $input.email
        template_id: $env.sendgrid_magic_link_template
        data       : {}|set:"magic_link":$magic_link
      }
    } as $sendgrid_send_magic_link
  }

  response = {
    message: {}|set:"success":true|set:"message":"magic link sent"
  }
}