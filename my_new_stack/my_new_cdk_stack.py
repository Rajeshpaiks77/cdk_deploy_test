from aws_cdk import (
    # Duration,
    Stack,
    RemovalPolicy,
    aws_s3 as s3

)
from aws_cdk import Stack, RemovalPolicy
from constructs import Construct

class MyNewCdkStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        # The code that defines your stack goes here

        bucket = s3.Bucket(self, "raj_first_bucket",
            versioned=True,  # Enable versioning
            removal_policy=RemovalPolicy.DESTROY,  # Remove bucket when stack is destroyed
            auto_delete_objects=True  # Auto-delete objects with bucket (only works with DESTROY)
        )
