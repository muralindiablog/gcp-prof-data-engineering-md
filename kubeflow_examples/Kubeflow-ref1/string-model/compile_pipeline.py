# compile_pipeline.py
from kfp import compiler
from pipeline import string_processing_pipeline

compiler.Compiler().compile(
    pipeline_func=string_processing_pipeline,
    package_path="string_processing_pipeline.yaml"
)
