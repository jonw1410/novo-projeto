// Learn how to use a For Each Loop to manipulate a list (array) of data by formatting a timestamp into human readable format.
query "loop-and-format-date/content" verb=GET {
  api_group = "Starter Template"

  input {
  }

  stack {
    db.query content {
      return = {type: "list"}
    } as $content
  
    foreach ($content) {
      each as $item {
        var.update $item.created_at {
          value = $item.created_at|format_timestamp:"r":"UTC"
        }
      }
    }
  }

  response = $content
}