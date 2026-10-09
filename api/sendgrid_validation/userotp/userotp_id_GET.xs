// Get userOTP record
query "userotp/{userotp_id}" verb=GET {
  api_group = "Sendgrid Validation"

  input {
    int userotp_id? filters=min:1
  }

  stack {
    db.get userOTP {
      field_name = "id"
      field_value = $input.userotp_id
    } as $userotp
  
    precondition ($userotp != null) {
      error_type = "notfound"
      error = "Not Found."
    }
  }

  response = $userotp
  guid = "XUbR7X1t0e2M2QW4bbaUtdkPEwk"
}