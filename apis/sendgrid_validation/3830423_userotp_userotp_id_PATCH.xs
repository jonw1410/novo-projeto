// Edit userOTP record
query "userotp/{userotp_id}" verb=PATCH {
  api_group = "Sendgrid Validation"

  input {
    int userotp_id? filters=min:1
    dblink {
      table = "userOTP"
    }
  }

  stack {
    util.get_raw_input {
      encoding = "json"
      exclude_middleware = false
    } as $raw_input
  
    db.patch userOTP {
      field_name = "id"
      field_value = $input.userotp_id
      data = `$input|pick:($raw_input|keys)`|filter_null|filter_empty_text
    } as $userotp
  }

  response = $userotp
}