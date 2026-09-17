# LLM From Scratch

Chapter-wise implementations and notes based on *Build a Large Language Model (From Scratch)* by Sebastian Raschka.

The repository is intentionally built in small, runnable steps. Every chapter must document its scope, keep implementation code under `src/`, and include an executable check for the behavior it teaches.

## Repository format

```text
.
├── README.md
├── pyproject.toml
├── uv.lock
└── chapters/
   └── chapter_02/
      ├── README.md       # requirements and run commands
      ├── notes.md        # concepts and implementation decisions
      ├── src/             # importable chapter code
      └── tests/           # chapter checks
```

New chapters should follow the same layout. Keep datasets and generated artifacts out of source control unless a chapter explicitly needs them.

## Requirements

- Python 3.11 or newer
- `uv` for environment and dependency management
- No network access or external dataset is required for Chapter 2

Install and verify the environment from the repository root:

```powershell
uv sync
uv run python --version
```

## Current work

Chapter 2 implements a deterministic word-and-punctuation tokenizer with vocabulary construction, special tokens, and reversible decoding. Its detailed requirements and acceptance checks are in [chapters/chapter_02/README.md](chapters/chapter_02/README.md).

Run the Chapter 2 checks with:

```powershell
uv run python -m unittest discover -s chapters/chapter_02/tests -v
```

## Local Windows setup

These instructions target a Windows laptop using PowerShell. Install `uv` once, then run the following commands from the repository root:

```powershell
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
uv --version
uv venv
uv sync
.\.venv\Scripts\Activate.ps1
```

This creates `.venv` and installs dependencies from `pyproject.toml` and `uv.lock`. Dependencies belong in `pyproject.toml`; update `uv.lock` whenever they change.

Start notebooks only when a chapter requires them:

```powershell
uv run jupyter notebook
```

## Chapter workflow

For each chapter, add `README.md`, `notes.md`, `src/`, and `tests/`. The chapter README is the source of truth for requirements and commands. Run code from the repository root:

```bash
uv run python chapters/chapter_xx/src/<script>.py
```

## Reproducibility checklist

- Keep `pyproject.toml` and `uv.lock` in sync.
- Keep chapter folders named `chapter_XX` and self-contained.
- Make tests runnable without a notebook or hidden local files.
- Record concepts and decisions in each chapter's `notes.md`.
