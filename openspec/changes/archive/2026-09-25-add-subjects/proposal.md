# Change: Add Academic Subjects Management (add-subjects)

## Why
Currently in EduTrack AI, subjects (disciplinas) are partially mocked in-memory and lack persistent lifecycle management (creation, update, deletion, and local/backend persistence). Students need to dynamically add, edit, configure evaluation weights (P1, P2, Trabalhos) and track attendance for their semester subjects, with automatic updates reflected across the dashboard KPIs, performance charts, and grade simulator.

## What Changes
- Add full Subject management capability: create new subject with name, professor, semester, workload, attendance, and exam grades.
- Enable editing and deleting existing subjects from the dashboard interface.
- Add persistent storage mechanism (browser `localStorage` with offline-first support and preparation for Xano backend sync).
- Ensure real-time recalculation of academic metrics (Overall GPA/CR, active subject count, class attendance %, and chart datasets).
- Update subject selectors across Tasks and AI Grade Simulator to dynamically reflect available subjects.

## Impact
- Affected specs: `specs/subjects/spec.md`, `specs/dashboard/spec.md`
- Affected code: `dashboard.html`, `app.py`, `tables/` (future Xano subjects table schema if delegated)

