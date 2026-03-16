# processing_logic.py
from typing import NamedTuple

class ProcessingResults(NamedTuple):
    combined: str
    reversed: str
    uppercased: str

def concat(a: str, b: str) -> str:
    return a + b

def reverse(text: str) -> str:
    return text[::-1]

def to_upper(text: str) -> str:
    return text.upper()

def run(a: str = "Hello", b: str = "World") -> ProcessingResults:
    combined_val = concat(a, b)
    reversed_val = reverse(combined_val)
    uppercased_val = to_upper(combined_val)

    return ProcessingResults(
        combined=combined_val,
        reversed=reversed_val,
        uppercased=uppercased_val
    )
