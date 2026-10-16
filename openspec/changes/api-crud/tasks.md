# Tasks: api-crud

## 1. Banco de Dados

- [x] 1.1 Criar tabela `academic_tasks` em `tables/academic_tasks.xs` com FKs para `usuarios` e `subjects`

## 2. Endpoints CRUD para 'subjects'

- [x] 2.1 Criar `POST /subjects` com vinculação automática de `user_id = $auth.id` em `apis/subjects/subjects_POST.xs`
- [x] 2.2 Criar `GET /subjects` filtrando exclusivamente por `user_id = $auth.id` em `apis/subjects/subjects_GET.xs`
- [x] 2.3 Criar `PATCH /subjects/{id}` com validação de posse (`user_id = $auth.id`) em `apis/subjects/subjects_id_PATCH.xs`
- [x] 2.4 Criar `DELETE /subjects/{id}` com validação de posse (`user_id = $auth.id`) em `apis/subjects/subjects_id_DELETE.xs`

## 3. Endpoints CRUD para 'academic_tasks'

- [x] 3.1 Criar `POST /academic_tasks` com vinculação automática de `user_id = $auth.id` em `apis/academic_tasks/academic_tasks_POST.xs`
- [x] 3.2 Criar `GET /academic_tasks` filtrando exclusivamente por `user_id = $auth.id` em `apis/academic_tasks/academic_tasks_GET.xs`
- [x] 3.3 Criar `PATCH /academic_tasks/{id}` com validação de posse (`user_id = $auth.id`) em `apis/academic_tasks/academic_tasks_id_PATCH.xs`
- [x] 3.4 Criar `DELETE /academic_tasks/{id}` com validação de posse (`user_id = $auth.id`) em `apis/academic_tasks/academic_tasks_id_DELETE.xs`
