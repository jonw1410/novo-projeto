// This endpoint is used to validate that sendgrid is working.
query "sendgrid/validate" verb=POST {
  api_group = "Sendgrid Validation"

  input {
    text EMAIL? filters=trim
  }

  stack {
    security.random_number {
      min = 0
      max = 9007199254740991
    } as $x1
  
    var $x2 {
      value = ""
    }
  
    db.add usuarios {
      enforce_hidden_fields = false
      data = {}
    } as $user1
  
    var $x3 {
      value = ""
    }
  
    function.run "" {
      input = {to_email: "", template_id: "", data: {}}
    } as $func1
  }

  response = {status: "success"}
}