# src/components/processing_component.py
from kfp.dsl import component
from business_logic.processing_logic import run, ProcessingResults

@component(
    base_image="python:3.10",
    packages_to_install=[]
)
def processing_component(
    a: str,
    b: str
) -> ProcessingResults:
    """
    Kubeflow wrapper around DS-owned business logic.
    No transformations are implemented here.
    """
    return run(a, b)
