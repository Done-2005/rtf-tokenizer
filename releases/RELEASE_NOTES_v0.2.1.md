# RTF Tokenizer (Copy-3) — v0.2.1 (reference release)

This is the verified reference build. It is frozen and will not be overwritten. It is for testing and evaluation only.

## Install

```bash
pip install relational_token_framework-0.2.1-py3-none-any.whl
```

```python
from rtf import RTFTokenizer
```

## Verified API facts

- `__version__ == "0.2.1"`
- `RTFTokenizer.encode_text` and `decode` exist
- `RTFTokenizer.encode` does not exist (`RTF.encode` does)
- `RTFTokenizer()` + `encode_text(...)` raises `ValueError: tokenizer is not fitted`

Working configuration:

```python
tok = RTFTokenizer(kind="atoms")
tok.fit_texts(train_texts)
ids = tok.encode_text(text)
```

## SHA-256

```
relational_token_framework-0.2.1-py3-none-any.whl
143E77BA1F5C1991E39AFD3ABF900A04B0BFAE8D311F1CD80B5152D33CC79945

relational_token_framework-0.2.1.tar.gz
94634DDECFEBB80AE692D5DB7702CE631C542469812D6F324474203F85D249E2
```

## Known limitations (measured, not fixed in this release)

- Closed vocabulary: unseen values decode as `<unk>`
- Automatic domain detection can mis-tag prose as `PYTHON` and TeX as `ENGLISH`
- No file detection/extraction layer; PDF/DOCX and binary formats are unsupported

This release contains no tokenizer implementation changes, architecture changes or dataset material.
