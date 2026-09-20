"""Core implementation for word-boundary truncation."""

from __future__ import annotations


def truncate(text: str, limit: int) -> str:
    """Return *text* shortened so it fits within *limit* characters.

    The result never splits a word: if the naive cut would land in the
    middle of a word, the cut moves left to the preceding whitespace.  This
    means the returned string can be shorter than *limit*, sometimes by a
    noticeable amount.  That is intentional: the caller asked for
    word-boundary truncation, not packing as many characters as possible.

    Rules (in this order):

    1. ``limit <= 0`` returns ``""``.
    2. If ``text`` is already ``limit`` characters or shorter, return it
       unchanged.
    3. Otherwise, cut at the last whitespace character at or before index
       ``limit``.  Whitespace is anything for which ``str.isspace()`` is
       true.
    4. If there is no whitespace in the first ``limit`` characters, cut at
       ``limit`` exactly.  This is the one case where a word may be split,
       because there is no safe boundary to retreat to.

    Trailing whitespace on the returned string is removed.  This keeps the
    result tidy and is what most callers expect from a truncation helper.
    """
    if limit <= 0:
        return ""

    if len(text) <= limit:
        return text

    window = text[:limit]
    cut = limit

    # Walk backwards through the window looking for the last whitespace
    # character.  rfind with a custom predicate is not available in the
    # standard library, so a simple loop is clearest and fast enough for
    # typical strings.
    for idx in range(limit - 1, -1, -1):
        if window[idx].isspace():
            cut = idx
            break

    return text[:cut].rstrip()
