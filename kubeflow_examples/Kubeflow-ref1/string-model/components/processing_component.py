# components/processing_component.py
from typing import NamedTuple
from kfp.dsl import component

class ProcessingResults(NamedTuple):
    combined: str
    reversed: str
    uppercased: str

@component(
    base_image="python:3.10",
    packages_to_install=[]
)
def processing_component(
    a: str,
    b: str
) -> ProcessingResults:
    def concat(a: str, b: str) -> str:
        return a + b

    def reverse(text: str) -> str:
        return text[::-1]

    def to_upper(text: str) -> str:
        return text.upper()

    combined_val = concat(a, b)
    reversed_val = reverse(combined_val)
    uppercased_val = to_upper(combined_val)

    return ProcessingResults(
        combined=combined_val,
        reversed=reversed_val,
        uppercased=uppercased_val
    )
