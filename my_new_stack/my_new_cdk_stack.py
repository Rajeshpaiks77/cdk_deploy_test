from aws_cdk import (
    # Duration,
    Stack,
    aws_s3 as s3
)
from constructs import Construct

class MyNewCdkStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)
        
       s3.Bucket(id="RjBucket",bucket_name="rj-bucket") # new bucket
    

