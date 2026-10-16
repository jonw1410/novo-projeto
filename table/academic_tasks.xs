// Armazena as tarefas acadêmicas vinculadas aos usuários e disciplinas
table academic_tasks {
  auth = false

  schema {
    int id
    timestamp created_at?=now {
      visibility = "private"
    }

    text title filters=trim
    text? description filters=trim
    timestamp? due_date?
    text status?="Pendente" filters=trim

    // Referência à disciplina
    int subject_id {
      table = "subjects"
    }

    // Referência ao usuário da tabela de autenticação usuarios
    int user_id {
      table = "usuarios"
    }
  }

  index = [
    {type: "primary", field: [{name: "id"}]}
    {type: "btree", field: [{name: "user_id", op: "asc"}]}
    {type: "btree", field: [{name: "subject_id", op: "asc"}]}
    {type: "btree", field: [{name: "created_at", op: "desc"}]}
  ]
}
