// Query all userOTP records
query userotp verb=GET {
  api_group = "Sendgrid Validation"

  input {
  }

  stack {
    db.query "" {
      return = {type: "list"}
    } as $userotp
  }

  response = $userotp
  guid = "ibI0kmgM0f_v4Q7mnhWylFVvjfg"
}