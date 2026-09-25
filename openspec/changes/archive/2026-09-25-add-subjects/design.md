# Design Document: Academic Subjects Management

## Context
EduTrack AI is an academic monitoring dashboard built with Streamlit and an interactive HTML/JS front-end. Currently, default subjects are pre-loaded into an in-memory array (`state.disciplinas`). When a user adds a new subject via the modal, the item is inserted in memory only, disappearing upon page refresh. Furthermore, subjects cannot yet be edited or deleted, and evaluation weights are fixed.

## Technical Decisions

### 1. Offline-First Storage Layer
- Utilize browser `localStorage` (`edutrack_subjects_v1`) to persist the collection of subjects.
- On initialization:
  1. Attempt to load from `localStorage`.
  2. If empty, seed with initial realistic Impacta Innovation Lab curriculum subjects.
  3. Provide a "Restaurar Padrões" (Reset to default) option in settings.
- Structure data layer with clear serialization/deserialization functions (`loadSubjects()`, `saveSubjects()`).

### 2. Data Model
```typescript
interface Subject {
  id: number | string;
  nome: string;
  professor: string;
  p1: number;
  p2: number | null;
  trabalho?: number | null;
  media: number;
  presenca: number;       // percentage (0 - 100)
  cargaHoraria: number;   // default 80h
  status: "Aprovado" | "Atenção" | "Reprovado";
  pesoP1?: number;        // default 40%
  pesoP2?: number;        // default 60%
}
```

### 3. Metric Propagation & Reactive Chart Updates
- When a subject is added, updated, or removed:
  - Recalculate global GPA: `GPA = sum(media) / count`
  - Recalculate average attendance: `Freq = sum(presenca) / count`
  - Re-render HTML5 canvas bar chart dynamically adjusting bar widths and labels.
  - Repopulate `<select>` elements for Task creation and the AI Simulator.

### 4. UI/UX Interaction
- Modal form for "Cadastrar Disciplina" with instant input validation (0 <= grades <= 10, 0 <= attendance <= 100).
- Action buttons on each subject card:
  - "✏️ Editar" (opens edit modal with prefilled data)
  - "🗑️ Excluir" (with confirmation)
- Toast / notification feedback on successful addition.

