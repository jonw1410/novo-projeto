// Atualiza uma tarefa acadêmica garantindo a posse pelo usuário autenticado
query "academic_tasks/{id}" verb=PATCH {
  api_group = "academic_Tasks"
  auth = ""

  input {
    int id filters=min:1
    text? title filters=trim
    int? subject_id filters=min:1
    text? priority filters=trim
    text? status filters=trim
    timestamp? due_date?
  }

  stack {
    db.query "" {
      where = $db.academic_tasks.id == $input.id && $db.academic_tasks.user_id == $auth.id
      return = {type: "single"}
    } as $task
  
    precondition ($task != null) {
      error_type = "notfound"
      error = "Tarefa não encontrada ou acesso não autorizado."
    }
  
    db.edit "" {
      field_name = "id"
      field_value = $input.id
      data = {
        title     : $input.title
        subject_id: $input.subject_id
        priority  : $input.priority
        status    : $input.status
        due_date  : $input.due_date
      }
    } as $updated_task
  }

  response = $updated_task
  guid = "90GbOuDqxc6dm_c7oXw9BbJYuYQ"
}