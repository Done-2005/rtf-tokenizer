"""Minimal verified usage for relational-token-framework 0.2.1.

The working path requires kind="atoms" and fit_texts(). An ordinary
RTFTokenizer() constructor does not support encode_text() in this release.
"""
from rtf import RTFTokenizer, __version__

assert __version__ == "0.2.1", f"unexpected version: {__version__}"

train_texts = [
    "def add(x, y):\n    return x + y",
    "def scale(x, k):\n    return x * k",
]

tok = RTFTokenizer(kind="atoms")
tok.fit_texts(train_texts)

text = "def add(x, y):\n    return x + y"
ids = tok.encode_text(text)
symbols = tok.decode(ids)

print("version:", __version__)
print("ids:", ids[:8])
print("symbols:", symbols[:8])
