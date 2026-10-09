// codigo otp , validação
table userOTP {
  auth = false

  schema {
    int id
    timestamp created_at?=now {
      visibility = "private"
    }
  
    text Email? filters=trim
    text OTP_CODE? filters=trim
    timestamp? OTP_EXPIRES_AT?
  }

  index = [
    {type: "primary", field: [{name: "id"}]}
    {type: "btree", field: [{name: "created_at", op: "desc"}]}
  ]

  guid = "nu-NeZvdqgqK368Rr50YkpHXABU"
}