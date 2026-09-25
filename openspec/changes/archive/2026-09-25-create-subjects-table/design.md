# Technical Design: 'subjects' Table Schema in Xano

## 1. Overview & Architecture
This document designs the relational schema and indexing strategy for the `subjects` table in Xano Cloud (`x8ki-letl-twmt.xano.io`, Workspace ID: 156517). The table stores academic course metadata (name, teacher, workload hours) scoped to the authenticated student via a Foreign Key to the existing Xano auth table (`usuarios`).

## 2. Relational Schema Specification

### Target Table: `subjects`
- **Authentication**: `auth = false`
- **Location**: `tables/subjects.xs`

```xanoscript
// Armazena as disciplinas acadêmicas vinculadas aos usuários
table subjects {
  auth = false

  schema {
    int id
    timestamp created_at?=now {
      visibility = "private"
    }

    text name filters=trim
    text teacher filters=trim
    int hours

    // Relacionamento com o usuário autenticado da tabela usuarios
    int user_id {
      table = "usuarios"
    }
  }

  index = [
    {type: "primary", field: [{name: "id"}]}
    {type: "btree", field: [{name: "user_id", op: "asc"}]}
    {type: "btree", field: [{name: "created_at", op: "desc"}]}
  ]
}
```

### Detailed Field Definitions

| Field Name | Type | Modifiers / Filters | Description |
|---|---|---|---|
| `id` | `int` | Primary Key, Auto-increment | Unique identifier for each subject record. |
| `created_at` | `timestamp` | `?=now`, `visibility = "private"` | Creation timestamp. |
| `name` | `text` | `filters=trim` | Name of the subject (e.g., "Innovation Lab", "Banco de Dados & Cloud"). |
| `teacher` | `text` | `filters=trim` | Name of the assigned instructor or professor. |
| `hours` | `int` | - | Total semester workload in hours (e.g., 40, 60, 80). |
| `user_id` | `int` | `{ table = "usuarios" }` | Foreign key referencing `usuarios.id` to guarantee tenant isolation. |

## 3. Indexing Strategy & Performance
- **Primary Index**: `{type: "primary", field: [{name: "id"}]}` ensures \(O(1)\) lookup by ID.
- **User Foreign Key Index**: `{type: "btree", field: [{name: "user_id", op: "asc"}]}` ensures that queries filtered by `WHERE user_id = $auth.id` execute with an index scan rather than a full table scan.
- **Created At Index**: `{type: "btree", field: [{name: "created_at", op: "desc"}]}` accelerates sorting by most recently created courses.

## 4. Sequencing & Best Practices (from `AGENTS.md`)
According to the Xano Table Designer guidelines in `AGENTS.md`:
1. **Rule 1**: Create tables WITHOUT cross-references first, then add relationships after both tables exist.
2. **Rule 2**: Always include an `id` field (int or uuid) as primary key.
3. **Rule 3**: O desenvolvedor é responsável por revisar e fazer push manualmente para o Xano. A IA não realiza push automático.

## 5. Responsabilidade da IA
- A tarefa da IA termina na geração e validação dos arquivos (`tables/subjects.xs`, especificações e `tasks.md`).
- A IA NÃO tenta fazer push, deploy ou sync com o Xano.
