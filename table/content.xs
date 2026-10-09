table content {
  auth = false

  schema {
    int id
    timestamp created_at?=now {
      visibility = "private"
    }
  
    text title? filters=trim
    text description? filters=trim
    int user_id? {
      table = "user"
    }
  
    image? image?
  }

  index = [
    {type: "primary", field: [{name: "id"}]}
    {type: "btree", field: [{name: "created_at", op: "desc"}]}
  ]

  guid = "oJKp49ObPW4hBM3634Ku0MFEqXs"
}