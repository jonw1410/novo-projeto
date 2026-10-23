// Get the record belonging to the authentication token
query "auth/me" verb=GET {
  api_group = "Authentication"
  auth = "user"

  input {
  }

  stack {
    db.get user {
      field_name = "id"
      field_value = $auth.id
      output = ["id", "created_at", "name", "email", "magic_link", "role"]
    } as $user
  }

  response = $user
  guid = "7wloKjH1J_tpUZNwxR6iOxMvG7w"
}