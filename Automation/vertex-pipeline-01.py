from kfp.v2 import dsl
from google_cloud_pipeline_components import aiplatform as gcc_aip

@dsl.pipeline(
  name='automl-tabular-classification-pipeline',
  pipeline_root='gs://my-pipeline-root/pipeline'
)
def pipeline(project_id: str):
    dataset_create_op = gcc_aip.TabularDatasetCreateOp(
        project=project_id,
        display_name='my-dataset',
        gcs_source='gs://my-dataset-bucket/my-dataset.csv'
    )

    training_op = gcc_aip.AutoMLTabularTrainingJobRunOp(
        project=project_id,
        display_name='train-automl-model',
        dataset=dataset_create_op.outputs['dataset'],
        target_column='target',
        prediction_type='classification'
    )

    deploy_op = gcc_aip.ModelDeployOp(  
        model=training_op.outputs['model'],
        project=project_id,
        machine_type='n1-standard-4'
    )

# Compile the pipeline
from kfp.v2 import compiler
compiler.Compiler().compile(pipeline_func=pipeline, package_path='pipeline.json')

