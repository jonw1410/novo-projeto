// Add a record to the content table and see an example of how to upload an image in Xano.
query "upload-image/content" verb=POST {
  api_group = "Starter Template"
  auth = "user"

  input {
    file image_file?
    text title? filters=trim
    text description? filters=trim
  }

  stack {
    storage.create_image {
      value = $input.image_file
      access = "public"
    } as $image
  
    db.add content {
      enforce_hidden_fields = false
      data = {
        created_at : "now"
        title      : $input.title
        description: $input.description
        user_id    : $auth.id
        image      : $image
      }
    } as $content
  }

  response = $content
  guid = "g6hmlB8d_WAf5kNwlrXEFr9Wlms"
}