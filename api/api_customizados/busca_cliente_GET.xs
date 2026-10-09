query busca_Cliente verb=GET {
  api_group = "API CUSTOMIZADOS"

  input {
    text authtoken? filters=trim
  }

  stack {
  }

  response = $api1
  guid = "0Avf0fgHHplAYl1EpHDYWZh_MNo"
}