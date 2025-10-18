## Purpose

This file gives focused, actionable guidance for code-assistant agents working in this repository. The project is a very small Python workspace with a single entry file `main.py`. The repository currently appears incomplete; treat changes as proposals and ask the human for intent when uncertain.

## Big picture / discovered architecture

- Single-module Python script: `main.py` is the only source file present. There are no packages, tests, or CI config files in the repo root.
- Because the repository is minimal, expect the human to be iteratively developing features. Small, reversible edits (fix formatting, add a clear program entry point) are preferred.

## Key files

- `main.py` — entry point. Current contents are minimal/invalid (see Example section). Use this file as the primary touchpoint for fixes or feature additions.

## How to run / debug (what I can infer)

- Run locally with the user's default shell on Windows PowerShell:

  - python main.py

- There are no build or test commands discoverable. If you add tests or dependencies, add a `requirements.txt` or `pyproject.toml` and update these instructions.

## Project-specific conventions / patterns (discoverable only)

- Naming and layout: flat single-file project. Prefer small, explicit changes that keep the top-level layout flat unless the user requests a package reorganization.
- Ask before introducing new third‑party dependencies — none are present now.

## Integration points & external dependencies

- None found in the repository. Assume no network, DB, or external service integrations unless the user adds configuration files or code that reference them.

## Examples & small guidance (concrete actionable items)

- The current `main.py` contains a code fence and an incomplete assignment (`name =`). Example safe edits an agent can propose or perform:

  1. Remove the Markdown-style triple backticks from `main.py` so it becomes valid Python.
  2. If the intent is a simple demo, replace the file with a minimal runnable script, e.g.:

     - Set `name = "your_name"` and print it under a `if __name__ == '__main__':` guard.

- When making edits, keep changes minimal and explain them in the commit message. If the fix is uncertain (e.g., what should `name` be?), include a question in the PR description.

## When to ask for clarification

- If code intent is unclear (placeholder variables, partial blocks, or commented TODOs), create a short PR that documents the assumption and leaves a comment for the maintainer.

## Safety and non-goals

- Do not introduce large refactors or add new infrastructure (CI, packaging) without an explicit request.

## Next steps an agent might take

1. Propose a minimal, runnable replacement for `main.py` in a PR with a short description of the assumption.
2. If requested, scaffold tests (`tests/test_main.py`) and a `requirements.txt`.

---
If any part of this guidance is unclear or you'd like the agent to take an explicit next step (apply a concrete fix to `main.py`, scaffold tests, or initialize packaging), tell me which and I'll proceed.
