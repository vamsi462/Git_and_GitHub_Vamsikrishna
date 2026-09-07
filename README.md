# Git and GitHub DevOps Assignment - Vamsikrishna Adusumalli

## Project Overview
This repository contains my submission for the Version Control Git and GitHub assignment, integrating a Flask web application with a MongoDB database and demonstrating advanced Git workflows.

## Task Breakdown & Implementation

### Task 1: Repository Setup & Branching
- Cloned the repository securely using SSH.
- Created a dedicated feature branch (`vamsikrishna`).
- Added the actual Flask application files and merged the branch back into `main`.

### Task 2: Merge Conflict Simulation
- Created a new branch (`vamsikrishna_new`) and modified `data.json`.
- Switched back to `main` and made a conflicting change to the exact same file.
- Handled and resolved the merge conflict in VS Code by accepting incoming changes, then committed and pushed the resolution.

### Task 3: Parallel Development & Integration
- Developed a frontend form component on `master_1` to capture To-Do items (Name and Description).
- Developed the backend `/submittodoitem` POST route on `master_2` using PyMongo to store submissions in MongoDB Atlas.
- Sequentially merged both feature branches into `main`.

### Task 4: Advanced Git Operations (Reset & Rebase)
- Updated the HTML form on `master_1` with sequential commits for Item ID, Item UUID, and Item Hash.
- Used `git reset --soft` to roll back commits while keeping changes staged, then re-committed them cleanly.
- Performed a rebase to keep a linear and clean commit history.