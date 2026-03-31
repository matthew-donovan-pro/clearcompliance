"""Document analyzer for the ClearCompliance demo.

This module contains a very simple parser that extracts
key/value pairs from plain text documents.  The implementation
assumes documents contain lines of the form ``Field: value``.
In production, document analysis may include OCR, NLP and
domain‑specific logic; those capabilities are not included here.
"""

from __future__ import annotations

from typing import Dict, Any


def analyze_document(path: str) -> Dict[str, Any]:
    """Parse a text document into a dictionary of fields.

    Parameters
    ----------
    path: str
        Path to the document file.

    Returns
    -------
    Dict[str, Any]
        Mapping of field names to values.  Only simple
        ``Field: value`` lines are recognised.
    """
    fields: Dict[str, Any] = {}
    try:
        with open(path, "r", encoding="utf-8") as f:
            for line in f:
                if ":" not in line:
                    continue
                name, _, value = line.partition(":")
                name = name.strip().lower().replace(" ", "_")
                fields[name] = value.strip()
    except FileNotFoundError:
        pass
    return fields


__all__ = ["analyze_document"]