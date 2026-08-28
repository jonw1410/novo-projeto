query BUSCACEP verb=GET {
  api_group = "API CUSTOMIZADOS"

  input {
    text CEP? filters=trim
  }

  stack {
  }

  response = $input.CEP
}