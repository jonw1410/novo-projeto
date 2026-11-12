// Delete userOTP record.
query "userotp/{userotp_id}" verb=DELETE {
  api_group = "Sendgrid Validation"

  input {
    int userotp_id? filters=min:1
  }

  stack {
    db.del "" {
      field_name = "id"
      field_value = $input.userotp_id
    }
  }

  response = null
  guid = "w1vrV1HWg-3QdQMxGUt7L8ROyqY"
}