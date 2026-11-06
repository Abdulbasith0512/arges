"""arges.healing — self-healing element resolution."""
from arges.healing.similarity import (
    DEFAULT_WEIGHTS,
    Candidate,
    changed_attributes,
    compatible,
    effective_weights,
    rank,
    score,
    text_sim,
)

__all__ = [
    "DEFAULT_WEIGHTS",
    "Candidate",
    "changed_attributes",
    "compatible",
    "effective_weights",
    "rank",
    "score",
    "text_sim",
]
