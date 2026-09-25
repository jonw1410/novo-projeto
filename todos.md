# Project TODOs

## OpenSpec Mudanças Arquivadas
- [x] `add-subjects` -> Arquivado em `openspec/changes/archive/2026-09-25-add-subjects`
  - Especificação principal consolidada em `openspec/specs/subjects/spec.md`
- [x] `create-subjects-table` -> Arquivado em `openspec/changes/archive/2026-09-25-create-subjects-table`
  - Especificação principal consolidada em `openspec/specs/subjects-table/spec.md`

## Tables (Banco de Dados Local)
- [x] Criar tabela `subjects` em `tables/subjects.xs`
  - Campos: `id`, `created_at`, `name`, `teacher`, `hours`, `user_id` (FK para `usuarios`)
  - Índices: `primary` (id), `btree` (user_id), `btree` (created_at)
  - Status: Arquivo gerado localmente. Pendente de revisão e push manual pelo desenvolvedor.

## Próximos Passos (Aguardando solicitação explícita do desenvolvedor)
- [ ] Endpoints REST da API de subjects (quando solicitado)
- [ ] Integração com frontend (quando solicitado)
