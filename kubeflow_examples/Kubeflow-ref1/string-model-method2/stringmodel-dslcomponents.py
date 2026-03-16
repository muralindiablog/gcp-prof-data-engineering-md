"""
Single-file Kubeflow Pipeline (KFP v2)
- Data Scientist logic (unchanged)
- Kubeflow wrapper using dsl.component
- Pipeline definition
- Compilation entry point
"""

from typing import NamedTuple
from kfp import dsl, compiler


# ============================================================
# 1️⃣ DATA SCIENTIST OWNED CODE (NO KUBEFLOW DEPENDENCY)
# ============================================================

class ProcessingResults(NamedTuple):
    """
    Standardized output schema for the string processing logic.
    """
    combined: str
    reversed: str
    uppercased: str


def run(a: str = "Hello", b: str = "World") -> ProcessingResults:
    """
    Executes core string transformations (Concat -> Reverse -> Upper).
    """
    combined_val = a + b
    reversed_val = combined_val[::-1]
    uppercased_val = combined_val.upper()

    return ProcessingResults(
        combined=combined_val,
        reversed=reversed_val,
        uppercased=uppercased_val
    )


# ============================================================
# 2️⃣ KUBEFLOW COMPONENT (dsl.component – THIN WRAPPER)
# ============================================================

@dsl.component(
    base_image="python:3.10",
    packages_to_install=[]
)
def processing_component(
    a: str,
    b: str
) -> ProcessingResults:
    """
    Kubeflow wrapper around DS logic.
    NO business logic is implemented here.
    """
    return run(a, b)


# ============================================================
# 3️⃣ KUBEFLOW PIPELINE (KFP v2)
# ============================================================

@dsl.pipeline(
    name="string-processing-pipeline",
    description="Single-file Kubeflow pipeline using dsl.component"
)
def string_processing_pipeline(
    a: str = "Hello",
    b: str = "World"
):
    processing_component(a=a, b=b)


# ============================================================
# 4️⃣ PIPELINE COMPILATION ENTRY POINT
# ============================================================

if __name__ == "__main__":
    compiler.Compiler().compile(
        pipeline_func=string_processing_pipeline,
        package_path="string_processing_pipeline.yaml"
    )
