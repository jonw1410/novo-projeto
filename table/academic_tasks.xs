table {
  name = "academic_tasks"
  primary_key = "id"
  columns {
    id {
      type = "integer"
      auto_increment = true
    }
    title {
      type = "text"
    }
    description {
      type = "text"
    }
    due_date {
      type = "date"
    }
    status {
      type = "text"
    }
    subject_id {
      type = "integer"
      reference = "subjects.id"
    }
    user_id {
      type = "integer"
      description = "Owner user"
    }
    created_at {
      type = "datetime"
      default = "CURRENT_TIMESTAMP"
    }
    updated_at {
      type = "datetime"
      default = "CURRENT_TIMESTAMP"
      on_update = "CURRENT_TIMESTAMP"
    }
  }
}

