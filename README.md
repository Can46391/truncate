# Truncate

Truncate text at a word boundary rather than mid-word.

```python
from truncate import truncate

result = truncate("The quick brown fox", 14)
# "The quick"
```

## Why this library exists

Naive slicing (`text[:limit]`) often leaves a partial word at the end of a
string. That is fine for logs or fixed-width displays, but it reads badly in
user-facing copy where a sentence should not end with "qu". This library makes
the conservative choice: when the cut would split a word, it retreats to the
previous whitespace. The trade-off is that the returned string is sometimes
noticeably shorter than the limit. If you need a string that is as close to the
limit as possible regardless of word boundaries, this is the wrong tool.

## The awkward edge

If the first `limit` characters contain no whitespace at all, there is no safe
place to cut. In that case the function falls back to a hard cut at `limit`,
splitting a word, because returning an empty string would discard more than the
caller asked to discard.

## Exports

- `truncate(text: str, limit: int) -> str`
