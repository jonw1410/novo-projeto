query activity_grades verb=POST {
  api_group = "activity_grades"
  auth = true

  input {
    int activity_id {
      description = "ID of the academic activity"
    }

    int student_id {
      description = "ID of the student receiving the grade"
    }

    decimal grade filters=min:0|max:10 {
      description = "Grade from 0 to 10"
    }

    text? feedback {
      description = "Optional feedback for the student"
    }
  }

  stack {
    precondition ($input.grade >= 0 && $input.grade <= 10) {
      description = "Ensure the grade is between 0 and 10"
      error_type = "input"
      error = "Grade must be between 0 and 10."
    }

    var $professor_id {
      value = $auth.id
    }

    db.add activity_grades {
      data = {
        created_at  : "now"
        activity_id : $input.activity_id
        student_id  : $input.student_id
        professor_id: $professor_id
        grade       : $input.grade
        feedback    : $input.feedback
      }
    } as $created_grade
  }

  response = $created_grade
}
