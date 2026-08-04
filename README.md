# LLM From Scratch (Chapter-wise Learning Repo)

Repository to track and implement the book **"Build a Large Language Model (From Scratch)" by Sebastian Raschka** in a chapter-wise, reproducible, and presentable way.

## Goals

- Learn and implement concepts chapter by chapter
- Keep notes, code, and experiments organized per chapter
- Maintain reproducible environments across multiple platforms

## Suggested Repository Structure

```text
.
├── README.md
├── pyproject.toml
├── uv.lock
├── chapters/
│   ├── chapter_01/
│   │   ├── notes.md
│   │   ├── exercises/
│   │   └── src/
│   ├── chapter_02/
│   │   ├── notes.md
│   │   ├── exercises/
│   │   └── src/
│   └── ...
├── datasets/
├── notebooks/
└── scripts/
```

> Keep each chapter self-contained with notes, exercises, and source code.

## Environment Setup with `uv` (Reproducible Across Platforms)

### 1) Install `uv`

- **Windows (PowerShell):**

```powershell
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
```

- **macOS/Linux (for SageMaker terminal as well):**

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

Verify installation:

```bash
uv --version
```

### 2) Initialize project metadata (first time only)

From repository root:

```bash
uv init --name llm_from_scratch
```

If `pyproject.toml` already exists, skip this step.

### 3) Create and sync the environment

```bash
uv venv
uv sync
```

This creates `.venv` and installs dependencies from `pyproject.toml` / `uv.lock`.

### 4) Add dependencies (example)

```bash
uv add numpy pandas matplotlib jupyter ipykernel
```

Commit both `pyproject.toml` and `uv.lock` for reproducibility.

---

## Platform-specific Usage

### Windows Laptop

1. Open PowerShell in repository root.
2. Run:

```powershell
uv venv
uv sync
.\.venv\Scripts\Activate.ps1
```

3. Start notebooks if needed:

```powershell
uv run jupyter notebook
```

### SageMaker Notebooks

1. Open a terminal in the notebook instance.
2. In repo root:

```bash
uv venv
uv sync
source .venv/bin/activate
uv run python -m ipykernel install --user --name llm-from-scratch
```

3. Select `llm-from-scratch` kernel in Jupyter.

### Google Colab

Colab does not persist local virtual environments between sessions, so use `uv` for fast, repeatable dependency sync at session start:

```python
!pip install -q uv
!uv pip install -r <(uv export --format requirements-txt)
```

If `uv.lock`/`pyproject.toml` is updated, this keeps installs aligned with the repo state.

---

## Chapter-wise Workflow

For each chapter:

1. Create chapter folder in `chapters/chapter_xx/`
2. Add:
   - `notes.md` for learning summary
   - `src/` for implementation
   - `exercises/` for practice
3. Run chapter code with:

```bash
uv run python chapters/chapter_xx/src/<script>.py
```

## Reproducibility Checklist

- Commit `pyproject.toml`
- Commit `uv.lock`
- Keep chapter folders organized and named consistently
- Record chapter notes and key learnings in `notes.md`
