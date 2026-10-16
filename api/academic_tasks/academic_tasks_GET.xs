// Lista todas as tarefas acadêmicas do usuário autenticado
query "academic_tasks" verb=GET {
  api_group = "Academic Tasks"
  auth = "usuarios"

  input {
  }

  stack {
    db.query academic_tasks {
      where = $db.academic_tasks.user_id == $auth.id
      sort = {academic_tasks.created_at: "desc"}
      return = {type: "list"}
    } as $tasks
  }

  response = $tasks
}
