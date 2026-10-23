// Lista as disciplinas pertencentes exclusivamente ao usuário autenticado
query subjects verb=GET {
  api_group = "Subjects"
  auth = ""

  input {
  }

  stack {
    db.query subjects {
      where = $db.subjects.user_id == $auth.id
      return = {type: "list"}
    } as $subjects
  }

  response = $subjects
  guid = "AKCn-zBu2NIqG2ebBggdVLGbbBM"
}