import boto3
import time
import matplotlib.pyplot as plt
from boto3.dynamodb.conditions import Key

#DynamoDB resource
dynamodb = boto3.resource("dynamodb")

#S3 client
s3 = boto3.client("s3")

#History table
table = dynamodb.Table("S3-object-size-history")

def lambda_handler(event, context):

    #Bucket name
    bucket_name = "nelson-assignment2-testbucket"

    #Current time
    current_time = int(time.time() * 1000)

    #10 seconds ago
    start_time = current_time - 10000

    #Query recent history
    response = table.query(
        KeyConditionExpression=
            Key("bucket_name").eq(bucket_name) &
            Key("timestamp").between(start_time, current_time)
    )

    items = response["Items"]

    #Sort by time
    items.sort(key=lambda x: int(x["timestamp"]))

    #Get plot values
    timestamps = []
    sizes = []

    for item in items:
        timestamps.append(int(item["timestamp"]))
        sizes.append(int(item["total_size"]))

    #Query max size
    max_response = table.query(
        IndexName="GlobalSizeIndex",
        KeyConditionExpression=Key("global_key").eq("ALL_BUCKETS"),
        ScanIndexForward=False,
        Limit=1
    )

    #Get max value
    if len(max_response["Items"]) > 0:
        max_size = int(max_response["Items"][0]["total_size"])
    else:
        max_size = 0

    #Create plot
    plt.figure()

    plt.plot(
        timestamps,
        sizes,
        marker="o"
    )

    #Max line
    plt.axhline(
        y=max_size,
        linestyle="--",
        label="Historical Max"
    )

    #Labels
    plt.xlabel("Timestamp")
    plt.ylabel("Size (bytes)")
    plt.title("S3 Bucket Size")

    plt.legend()

    #Save plot
    file_path = "/tmp/plot.png"
    plt.savefig(file_path)

    plt.close()

    #Upload plot
    s3.upload_file(
        file_path,
        bucket_name,
        "plot"
    )

    return {
        "statusCode": 200,
        "body": "Plot created successfully"
    }