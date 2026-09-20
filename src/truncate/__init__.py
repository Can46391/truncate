"""Truncate text at word boundaries.

This package provides a single function, :func:`truncate`, which shortens
a string to a maximum length without cutting a word in half.
"""

from .core import truncate

__all__ = ["truncate"]
