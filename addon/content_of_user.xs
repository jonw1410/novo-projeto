addon content_of_user {
  input {
    int user_id? {
      table = ""
    }
  }

  stack {
    db.query content {
      where = $db.content.user_id == $input.user_id
      return = {type: "list"}
    }
  }

  guid = "CwetHqfF33ZK9n1V71LyHkhLSj0"
}