// Cria uma nova disciplina vinculada ao usuário autenticado
query "subjects" verb=POST {
  api_group = "Subjects"
  auth = "usuarios"

  input {
    text name filters=trim
    text teacher filters=trim
    int hours
  }

  stack {
    db.add subjects {
      data = {
        created_at: "now"
        name      : $input.name
        teacher   : $input.teacher
        hours     : $input.hours
        user_id   : $auth.id
      }
    } as $subject
  }

  response = $subject
  guid = "PLET1Zyj2lnfnXGruYKFC8YJcDw"
}
