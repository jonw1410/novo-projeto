// The endpoint that allows a user to choose a new password.
query "password_reset/update_password" verb=POST {
  api_group = "Starter Template"
  auth = "user"

  input {
    password password? filters=min:8|minUpperAlpha:1|minLowerAlpha:1|minDigit:1 {
      visibility = "internal"
    }
  
    password confirm_password? {
      visibility = "internal"
    }
  }

  stack {
    precondition ($input.password == $input.confirm_password) {
      error = "Passwords do not match!"
    }
  
    db.get user {
      field_name = "id"
      field_value = ""
    } as $user
  
    precondition ($user.id == $auth.id) {
      error_type = "accessdenied"
    }
  
    db.edit user {
      field_name = "id"
      field_value = $auth.id
      enforce_hidden_fields = false
      data = {password: $input.password}
    } as $user
  }

  response = {}
    |set:"message":({}
      |set:"success":"true"
      |set:"message":"Password updated"
    )
  guid = "PHpSRcolT3wutmOPIP0D3shkXBk"
}