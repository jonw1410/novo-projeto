// Atualiza uma disciplina garantindo a posse pelo usuário autenticado
query "subjects/{id}" verb=PATCH {
  api_group = "Subjects"
  auth = "usuarios"

  input {
    int id filters=min:1
    text? name filters=trim
    text? teacher filters=trim
    int? hours
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

    db.edit subjects {
      field_name = "id"
      field_value = $input.id
      data = {
        name   : $input.name
        teacher: $input.teacher
        hours  : $input.hours
      }
    } as $updated_subject
  }

  response = $updated_subject
}
