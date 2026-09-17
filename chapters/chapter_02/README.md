# Chapter 2: Working with Text Data

This chapter covers the path from raw text to integer token IDs, which is the input format a language model can consume.

## Requirements

The implementation must:

1. Split words and punctuation deterministically.
2. Build a vocabulary from a text corpus.
3. Encode text into integer token IDs.
4. Decode token IDs back into readable text.
5. Support explicit unknown, beginning-of-text, and end-of-text tokens.
6. Reject malformed token IDs instead of silently producing incorrect text.
7. Run with only the Python 3.11+ standard library.

This is a small educational tokenizer, not a production BPE tokenizer. BPE and model input sampling will be added in later work.

## Layout

```text
chapter_02/
├── README.md
├── notes.md
├── src/
│   └── tokenizer.py
└── tests/
    └── test_tokenizer.py
```

## Run

From the repository root:

```powershell
uv run python -m unittest discover -s chapters/chapter_02/tests -v
```

Use the module directly for a quick example:

```powershell
uv run python chapters/chapter_02/src/tokenizer.py
```