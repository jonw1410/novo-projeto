// Get the user record belonging to the authentication token
query "basic_auth/me" verb=GET {
  api_group = "Starter Template"
  auth = "user"

  input {
  }

  stack {
    db.get user {
      field_name = "id"
      field_value = $auth.id
      output = ["id", "created_at", "name", "email"]
    } as $user
  }

  response = $user
  guid = "8xmbVkHlGyCa6iFsCzKemgxc05I"
}