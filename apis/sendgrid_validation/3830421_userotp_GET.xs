// Query all userOTP records
query userotp verb=GET {
  api_group = "Sendgrid Validation"

  input {
  }

  stack {
    db.query userOTP {
      return = {type: "list"}
    } as $userotp
  }

  response = $userotp
}