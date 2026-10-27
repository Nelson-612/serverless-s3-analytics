import boto3

#AWS region
region = "us-east-2"

#Create session
session = boto3.Session(region_name=region)

#Create clients
s3_client = session.client("s3")
dynamodb_client = session.client("dynamodb")

#Create bucket name
bucket_name = "nelson-assignment2-testbucket"
print("Bucket name:", bucket_name)

#Create S3 bucket
s3_client.create_bucket(
    Bucket=bucket_name,
    CreateBucketConfiguration={
        "LocationConstraint": region
    }
)

print("S3 bucket created")

#Create table
dynamodb_client.create_table(
    TableName="S3-object-size-history",

    KeySchema=[
        {
            "AttributeName": "bucket_name",
            "KeyType": "HASH"
        },
        {
            "AttributeName": "timestamp",
            "KeyType": "RANGE"
        }
    ],

    AttributeDefinitions=[
        {
            "AttributeName": "bucket_name",
            "AttributeType": "S"
        },
        {
            "AttributeName": "timestamp",
            "AttributeType": "N"
        },
        {
            "AttributeName": "global_key",
            "AttributeType": "S"
        },
        {
            "AttributeName": "total_size",
            "AttributeType": "N"
        }
    ],

    GlobalSecondaryIndexes=[
        {
            "IndexName": "GlobalSizeIndex",

            "KeySchema": [
                {
                    "AttributeName": "global_key",
                    "KeyType": "HASH"
                },
                {
                    "AttributeName": "total_size",
                    "KeyType": "RANGE"
                }
            ],

            "Projection": {
                "ProjectionType": "ALL"
            }
        }
    ],

    BillingMode="PAY_PER_REQUEST"
)

print("Table creation started")

#Wait for table
waiter = dynamodb_client.get_waiter("table_exists")
waiter.wait(TableName="S3-object-size-history")

print("DynamoDB table created")