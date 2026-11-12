// Tabela de tarefas acadêmicas
table academic_tasks {
  auth = false

  schema {
    int id
    text title
    text description
    date due_date
    text status
    int subject_id {
      table = "subjects"
    }
  
    // Owner user
    int user_id
  
    timestamp created_at?=now
    timestamp updated_at?=now
  }

  index = [{type: "primary", field: [{name: "id"}]}]
  guid = "qxF2OmcGtD2o98GQIXeu1sbx79U"
}