// Deleta uma disciplina garantindo a posse pelo usuário autenticado
query "subjects/{id}" verb=DELETE {
  api_group = "Subjects"
  auth = "usuarios"

  input {
    int id filters=min:1
  }

  stack {
    db.query subjects {
      where = $db.subjects.id == $input.id && $db.subjects.user_id == $auth.id
      return = {type: "single"}
    } as $subject

    precondition ($subject != null) {
      error_type = "notfound"
      error = "Disciplina não encontrada ou acesso não autorizado."
    }

    db.del subjects {
      field_name = "id"
      field_value = $input.id
    }
  }

  response = {success: true}
}
