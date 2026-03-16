# pipeline.py
from kfp import dsl
from kfp.dsl import pipeline
from components.processing_component import processing_component

@pipeline(
    name="data-scientist-string-processing-pipeline",
    description="Kubeflow pipeline wrapping DS string processing logic"
)
def string_processing_pipeline(
    a: str = "Hello",
    b: str = "World"
):
    processing_task = processing_component(
        a=a,
        b=b
    )

    # Optional: expose outputs for downstream components -- old incorrect
    # dsl.get_pipeline_conf().set_ttl_seconds_after_finished(3600)
