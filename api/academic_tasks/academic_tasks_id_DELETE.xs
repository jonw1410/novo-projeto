// Deleta uma tarefa acadêmica garantindo a posse pelo usuário autenticado
query "academic_tasks/{id}" verb=DELETE {
  api_group = "academic_Tasks"
  auth = "user"

  input {
    int id filters=min:1
  }

  stack {
    db.query academic_tasks {
      where = $db.academic_tasks.id == $input.id && $db.academic_tasks.user_id == $auth.id
      return = {type: "single"}
    } as $task

    precondition ($task != null) {
      error_type = "notfound"
      error = "Tarefa não encontrada ou acesso não autorizado."
    }

    db.del academic_tasks {
      field_name = "id"
      field_value = $input.id
    }
  }

  response = {success: true}
  guid = "tE1HU3XJnqnNhEHCBUtRgO5LAoc"
}
