// Cria uma nova tarefa acadêmica vinculada ao usuário autenticado
query "academic_tasks" verb=POST {
  api_group = "academic_Tasks"
  auth = "usuarios"

  input {
    text title filters=trim
    int subject_id filters=min:1
    text? priority?="Média" filters=trim
    text? status?="Pendente" filters=trim
    timestamp? due_date?
  }

  stack {
    // Valida se a disciplina pertence ao usuário autenticado
    db.query subjects {
      where = $db.subjects.id == $input.subject_id && $db.subjects.user_id == $auth.id
      return = {type: "single"}
    } as $subject

    precondition ($subject != null) {
      error_type = "notfound"
      error = "Disciplina associada não encontrada ou não pertence a este usuário."
    }

    db.add academic_tasks {
      data = {
        created_at: "now"
        title     : $input.title
        subject_id: $input.subject_id
        priority  : $input.priority
        status    : $input.status
        due_date  : $input.due_date
        user_id   : $auth.id
      }
    } as $task
  }

  response = $task
  guid = "if_Uq2ODYVMZ2Lgxl9g1DvkQVJc"
}
