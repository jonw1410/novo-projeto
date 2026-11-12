// Get academic_tasks record
query "academic_tasks/{academic_tasks_id}" verb=GET {
  api_group = "academic_Tasks"

  input {
    int academic_tasks_id? filters=min:1
  }

  stack {
    db.get academic_tasks {
      field_name = "id"
      field_value = $input.academic_tasks_id
    } as $model
  
    precondition ($model != null) {
      error_type = "notfound"
      error = "Not Found"
    }
  }

  response = $model
  guid = "GsS_SIwR-TSXCU1ovR5PYvgwWnc"
}