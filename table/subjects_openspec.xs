// Armazena as disciplinas acadêmicas vinculadas aos usuários, academic_tasks testando
table subjects_Openspec {
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
      table = "usuarios"
    }
  }

  index = [
    {type: "primary", field: [{name: "id"}]}
    {type: "btree", field: [{name: "user_id", op: "asc"}]}
    {type: "btree", field: [{name: "created_at", op: "desc"}]}
  ]

  guid = "Hou8POrgjwAroUqaWVinW_tZmaU"
}