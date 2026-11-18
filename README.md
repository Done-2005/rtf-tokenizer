# RTF Tokenizer (Copy-3)

Reference distribution for **version 0.2.1** of the Relational Token Framework tokenizer.

This repository distributes the exact verified `0.2.1` build. It is **not** published on PyPI and is provided for testing and evaluation. The `0.2.1` artifacts are frozen reference artifacts and will not be overwritten.

## License

MIT — see [LICENSE](LICENSE). This is the license declared in the verified package metadata and shipped inside both release artifacts.

## Install

Download `relational_token_framework-0.2.1-py3-none-any.whl` from the `v0.2.1` GitHub Release, then:

```bash
pip install relational_token_framework-0.2.1-py3-none-any.whl
python -c "import rtf; print(rtf.__version__)"   # expected: 0.2.1
```

## Verified API facts

| Fact | Status |
|---|---|
| `from rtf import RTFTokenizer` | Works |
| `rtf.__version__` | `"0.2.1"` |
| `RTFTokenizer.encode_text` and `decode` | Exist |
| `RTFTokenizer.encode` | Does **not** exist (`RTF.encode` does) |
| `RTFTokenizer()` + `encode_text(...)` | **Fails** with `ValueError: tokenizer is not fitted` |

### Working usage today

An explicit `kind="atoms"` and a prior `fit_texts()` are required:

```python
from rtf import RTFTokenizer

tok = RTFTokenizer(kind="atoms")
tok.fit_texts(["def add(x, y):\n    return x + y"])

text = "def add(x, y):\n    return x + y"
ids = tok.encode_text(text)
print(ids[:8])
print(tok.decode(ids)[:8])
```

See [`examples/basic_usage.py`](examples/basic_usage.py) for a runnable version.

An ordinary constructor with no configuration is **not** supported by this release. Do not advertise `RTFTokenizer()` + `encode_text()` as usable.

## Known limitations (measured, not fixed in 0.2.1)

- **Closed vocabulary:** the atom vocabulary is fitted from the texts passed to `fit_texts()`. Unseen values (identifiers, numbers, words) decode as `<unk>`.
- **Automatic domain detection is unreliable:** plain prose can be tagged `T:PYTHON`, and TeX can be tagged `T:ENGLISH`.
- **File handling is not included:** the tokenizer accepts text/structured input, not files. There is no automatic detection or extraction layer, and no PDF/DOCX support.
- **Learning results are limited:** in a bounded synthetic test, a tiny model trained on the tokens (loss fell), but held-out reconstruction was weak and generations were repetitive. Training on these tokens does not by itself prove information preservation.

These are documented limitations of the frozen `0.2.1` reference release, not claims of correctness.

## Integrity

SHA-256 checksums are in [`checksums/SHA256SUMS.txt`](checksums/SHA256SUMS.txt):

| Artifact | SHA-256 |
|---|---|
| `relational_token_framework-0.2.1-py3-none-any.whl` | `143E77BA1F5C1991E39AFD3ABF900A04B0BFAE8D311F1CD80B5152D33CC79945` |
| `relational_token_framework-0.2.1.tar.gz` | `94634DDECFEBB80AE692D5DB7702CE631C542469812D6F324474203F85D249E2` |

Verify before use:

```bash
sha256sum -c checksums/SHA256SUMS.txt
```

Do not use the stale `0.2.0` builds that appear in other directories.

## Scope of this repository

This repository contains only the verified package artifacts, license, checksums, documentation and a small usage example. It contains no datasets, research archives, credentials or unrelated project files.
