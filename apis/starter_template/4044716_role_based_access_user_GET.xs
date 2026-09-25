// An example of enforcing a role to execute an endpoint... Only admins can run this endpoint. An Addon is also included so you can see the content each user has created. 
query "role-based-access/user" verb=GET {
  api_group = "Starter Template"
  auth = "user"

  input {
  }

  stack {
    db.get user {
      field_name = "id"
      field_value = $auth.id
    } as $user_check
  
    precondition ($user_check.role == "admin") {
      error_type = "accessdenied"
      error = "You do not have admin access!"
    }
  
    db.query user {
      return = {type: "list"}
      output = ["id", "created_at", "name", "email", "role"]
      addon = [
        {
          name : "content_of_user"
          input: {user_id: $output.id}
          as   : "_content_of_user"
        }
      ]
    } as $user
  }

  response = $user
}