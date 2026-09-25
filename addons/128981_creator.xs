addon creator {
  input {
    int user_id? {
      table = ""
    }
  }

  stack {
    db.query user {
      where = $db.user.id == $input.user_id
      return = {type: "single"}
    }
  }
}