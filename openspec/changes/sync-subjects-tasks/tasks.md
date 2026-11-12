# Tasks: sync-subjects-tasks

## 1. Ajuste de Autenticação dos Endpoints Xano

- [x] 1.1 Configurar `auth = "user"` nos endpoints de `api/subjects/` e `api/academic_tasks/` para garantir validação correta do token JWT

## 2. Integração e Sincronização da Tela de Disciplinas

- [x] 2.1 Conectar a tela de Disciplinas (`pages/1_📚_Disciplinas.py`) aos endpoints CRUD de `subjects` utilizando o token JWT
- [x] 2.2 Implementar reatividade em tempo real para refletir criação e exclusão instantaneamente na tela de Disciplinas
- [x] 2.3 Adicionar funcionalidade para exportar o resumo da disciplina e suas tarefas em PDF

## 3. Integração e Sincronização da Tela de Tarefas

- [x] 3.1 Conectar a tela de Tarefas (`pages/2_📝_Tarefas.py`) aos endpoints CRUD de `academic_tasks` utilizando o token JWT
- [x] 3.2 Implementar reatividade em tempo real para criação, alteração de status e exclusão de tarefas sem recarregamento manual
