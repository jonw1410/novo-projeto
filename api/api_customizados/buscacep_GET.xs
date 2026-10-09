query BUSCACEP verb=GET {
  api_group = "API CUSTOMIZADOS"

  input {
    text CEP? filters=trim
  }

  stack {
  }

  response = $input.CEP
  guid = "3zVL4vF8O6w9gWWzCyYPr4cTwlg"
}