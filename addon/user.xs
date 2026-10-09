addon user {
  input {
    int user_id? {
      table = "usuarios"
    }
  }

  stack {
    db.query usuarios {
      where = $db.usuarios.id == $input.user_id
      return = {type: "single"}
    }
  }

  guid = "fI5VpxYryCJpzhx40j0gOMcUebI"
}