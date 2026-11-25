table activity_grades {
  auth = false

  schema {
    int id
    timestamp created_at?=now {
      visibility = "private"
    }
    int activity_id
    int student_id {
      table = "user"
    }
    int professor_id
    decimal grade filters=min:0|max:10
    text? feedback
  }

  index = [
    {type: "primary", field: [{name: "id"}]}
    {type: "btree", field: [{name: "student_id", op: "asc"}]}
    {type: "btree", field: [{name: "activity_id", op: "asc"}]}
  ]
}
