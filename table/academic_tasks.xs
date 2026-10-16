// Armazena as tarefas acadêmicas vinculadas aos usuários e matérias
table academic_tasks {
  auth = false

  schema {
    int id
    timestamp created_at?=now {
      visibility = "private"
    }

    text title filters=trim
    text priority?="Média" filters=trim
    text status?="Pendente" filters=trim
    timestamp? due_date?

    // Referência à disciplina
    int subject_id {
      table = "subjects"
    }

    // Referência ao usuário autenticado da tabela usuarios
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
