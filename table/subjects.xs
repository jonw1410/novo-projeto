// Armazena as disciplinas acadêmicas vinculadas aos usuários
table subjects {
  auth = false

  schema {
    int id
    timestamp created_at?=now {
      visibility = "private"
    }
  
    text name filters=trim
    text teacher filters=trim
    int hours
  
    // Referência ao usuário da tabela de autenticação usuarios
    int user_id {
      table = ""
    }
  }

  index = [
    {type: "primary", field: [{name: "id"}]}
    {type: "btree", field: [{name: "user_id", op: "asc"}]}
    {type: "btree", field: [{name: "created_at", op: "desc"}]}
  ]

  guid = "r8pbsqJDe3NYl4ru4zGy2SpI1mY"
}