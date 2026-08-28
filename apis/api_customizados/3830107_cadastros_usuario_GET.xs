query "CADASTROS/USUARIO" verb=GET {
  api_group = "API CUSTOMIZADOS"

  input {
    text Email? filters=trim
  }

  stack {
  }

  response = null
}