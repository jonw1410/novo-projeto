// Query all academic_tasks records
query academic_tasks verb=GET {
  api_group = "academic_Tasks"

  input {
  }

  stack {
    db.query academic_tasks {
      return = {type: "list"}
    } as $model
  }

  response = $model
  guid = "u15PLxiFulN9HA_-xTmQoDOUwIU"
}