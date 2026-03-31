"""Simple compliance engine for the ClearCompliance demo.

This module exposes functions to evaluate a document based on
dummy compliance rules.  The rules here are intentionally simple
to illustrate workflow; they are not suitable for production use.
"""

from __future__ import annotations

from typing import Dict, Any

from .document_analyzer import analyze_document


def evaluate_fields(fields: Dict[str, Any]) -> Dict[str, Any]:
    """Apply a trivial set of compliance rules to extracted fields.

    The rule implemented here flags any document with an ``amount``
    greater than 1000 as non‑compliant.

    Parameters
    ----------
    fields: Dict[str, Any]
        Parsed fields from the document.

    Returns
    -------
    Dict[str, Any]
        A result dictionary containing a boolean ``passed`` flag and
        an explanatory message.
    """
    amount = 0.0
    raw_amount = fields.get("amount")
    if raw_amount is not None:
        try:
            amount = float(raw_amount)
        except (TypeError, ValueError):
            pass
    risk = amount > 1000.0
    return {
        "passed": not risk,
        "message": "Amount exceeds threshold" if risk else "No issues detected",
    }


def evaluate_document(path: str) -> Dict[str, Any]:
    """Analyse a document and evaluate it for compliance.

    Parameters
    ----------
    path: str
        Path to the document file to analyse.

    Returns
    -------
    Dict[str, Any]
        Compliance result dictionary.
    """
    fields = analyze_document(path)
    result = evaluate_fields(fields)
    result["fields"] = fields
    return result


__all__ = ["evaluate_document", "evaluate_fields"]