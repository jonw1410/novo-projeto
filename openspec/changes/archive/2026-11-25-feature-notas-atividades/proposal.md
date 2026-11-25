# Change: feature-notas-atividades

## Why
Currently in EduTrack AI, professors have no backend mechanism to record or assign grades to students for specific academic activities and assignments. To support continuous academic assessment, a dedicated data model and grade submission API endpoint are required.

## What Changes
- Create database table `activity_grades` to store student grades and evaluation feedback for academic activities.
- Create API endpoint `POST /activity_grades` allowing instructors to submit grades for students on specific activities.

## Capabilities

### New Capabilities
- `activity-grades`: Allows instructors to record and store individual student grades and evaluations for specific academic activities.

## Impact
- **Backend Tables**: Creates `tables/activity_grades.xs` in Xano.
- **Backend APIs**: Creates `apis/activity_grades/activity_grades_POST.xs` in Xano.
