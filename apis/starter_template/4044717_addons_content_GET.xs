// An example of an addon. Extend the response of the records from content with the information of which user created each one.
query "addons/content" verb=GET {
  api_group = "Starter Template"

  input {
  }

  stack {
    db.query content {
      return = {type: "list"}
      addon = [
        {
          name  : "creator"
          output: ["id", "name"]
          input : {user_id: $output.user_id}
          as    : "_creator"
        }
      ]
    } as $content
  }

  response = $content
}