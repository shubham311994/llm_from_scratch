# Chapter 2 Notes

Language models operate on token IDs rather than raw strings. A tokenizer therefore needs two stable mappings:

- token text to integer ID for model input;
- integer ID back to token text for inspection and decoding.

The implementation keeps punctuation as separate tokens and uses explicit special tokens for unknown text and sequence boundaries. Vocabulary ordering is deterministic: tokens are sorted after collection, so the same corpus produces the same IDs on every run.

Whitespace is not stored as a token. Decoding joins ordinary word tokens with spaces and attaches punctuation to the preceding token. This is intentionally simple and makes the transformation easy to inspect before introducing subword tokenization.