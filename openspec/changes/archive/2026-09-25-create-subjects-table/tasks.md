# Tasks: Create 'subjects' Table Schema (create-subjects-table)

- [x] 1. Criar especificação da tabela `subjects` em `specs/subjects-table/spec.md`
- [x] 2. Criar arquivo de esquema `tables/subjects.xs` com os campos:
  - [x] `id` (int, auto-increment, primary key)
  - [x] `created_at` (timestamp, default now, visibility private)
  - [x] `name` (text, trim)
  - [x] `teacher` (text, trim)
  - [x] `hours` (int)
  - [x] `user_id` (int, FK para tabela `usuarios`)
- [x] 3. Configurar índices da tabela em `tables/subjects.xs`:
  - [x] Índice primário em `id`
  - [x] Índice btree em `user_id` (asc)
  - [x] Índice btree em `created_at` (desc)
