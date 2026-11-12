// Consulta e disponibiliza os dados de desempenho acadêmico do aluno autenticado
query "reports/student_performance" verb=GET {
  api_group = "Reports"
  auth = "user"

  input {
  }

  stack {
    // Recupera dados do estudante autenticado
    db.get user {
      field_name = "id"
      field_value = $auth.id
      output = ["id", "name", "email"]
    } as $student

    // Consulta disciplinas cadastradas pelo usuário
    db.query subjects {
      where = $db.subjects.user_id == $auth.id
      return = {type: "list"}
    } as $subjects

    // Consulta tarefas acadêmicas do usuário
    db.query academic_tasks {
      where = $db.academic_tasks.user_id == $auth.id
      sort = {academic_tasks.created_at: "desc"}
      return = {type: "list"}
    } as $tasks
  }

  response = {
    student : $student
    subjects: $subjects
    tasks   : $tasks
  }
}
