// Add academic_tasks record
query academic_tasks verb=POST {
  api_group = "academic_Tasks"

  input {
    dblink {
      table = "academic_tasks"
    }
  }

  stack {
    db.add academic_tasks {
      enforce_hidden_fields = false
      data = {
        title      : $input.title
        description: $input.description
        due_date   : $input.due_date
        status     : $input.status
        subject_id : $input.subject_id
        user_id    : $input.user_id
        created_at : $input.created_at
        updated_at : $input.updated_at
      }
    } as $model
  }

  response = $model
  guid = "W8Hl2jW3nnColYD8sllJe-FWBp0"
}