// Add userOTP record
query user_envio_OTP verb=POST {
  api_group = "Sendgrid Validation"

  input {
    dblink {
      table = ""
    }
  }

  stack {
    db.add "" {
      enforce_hidden_fields = false
      data = {created_at: "now"}
    } as $userotp
  }

  response = $userotp
  guid = "uhMPLmpoIZoQjsRK3WOpzFDUPvs"
}