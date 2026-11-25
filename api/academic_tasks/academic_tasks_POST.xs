// Add academic_tasks record
query academic_tasks verb=POST {
  api_group = "academic_Tasks"
  auth = "user"

  input {
    text title filters=trim
    text description filters=trim
    date due_date
    text status filters=trim
    int subject_id
  }

  stack {
    db.add academic_tasks {
      data = {
        created_at : "now"
        title      : $input.title
        description: $input.description
        due_date   : $input.due_date
        status     : $input.status
        subject_id : $input.subject_id
        user_id    : $auth.id
      }
    } as $model
  }

  response = $model
  guid = "W8Hl2jW3nnColYD8sllJe-FWBp0"
}