// This endpoint showcases conditional logic by doing a temperature conversion calculation. If Fahrenheit base, convert to Celsius. If Celsius base, convert to Fahrenheit
query "conditional/temperature_conversion" verb=GET {
  api_group = "Starter Template"

  input {
    decimal degrees?
    text convert_from? filters=trim|lower
  }

  stack {
    conditional {
      if ($input.convert_from == "fahrenheit") {
        var $converted_results {
          value = $input.degrees
            |subtract:32
            |multiply:(5|divide:9)
            |round:0
            |concat:"Celsius":" "
        }
      }
    
      else {
        var $converted_results {
          value = $input.degrees
            |multiply:(9|divide:5)
            |add:32
            |round:0
            |concat:"Fahrenheit":" "
        }
      }
    }
  }

  response = $converted_results
}