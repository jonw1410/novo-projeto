// Get the record belonging to the authentication token
query "auth/me" verb=GET {
  api_group = "authetication"
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
  guid = "gst3OsNQi4qJ604WkzbeF8ctfdA"
}