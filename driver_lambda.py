import boto3
import time
import urllib.request

#S3 client
s3 = boto3.client("s3")

#Bucket name
bucket_name = "nelson-assignment2-testbucket"

#Plotting API
plotting_api_url = "https://53ae33ebmj.execute-api.us-east-2.amazonaws.com/prod"  # Replace with your actual API Gateway URL

def lambda_handler(event, context):
    #create assignment1
    s3.put_object(Bucket=bucket_name, Key="assignment1.txt", Body="Empty Assignment 1")
    time.sleep(2)  # Wait for 2 seconds

    #Update assignment1
    s3.put_object(Bucket=bucket_name, Key="assignment1.txt", Body="Empty Assignment 2222222222")
    time.sleep(2)  # Wait for 2 seconds

    #Delete assignment1
    s3.delete_object(Bucket=bucket_name, Key="assignment1.txt")
    time.sleep(2)  # Wait for 2 seconds

    #Create assignment2
    s3.put_object(Bucket=bucket_name, Key="assignment2.txt", Body="33")
    time.sleep(3)  # Wait for 3 seconds

    #Call plotting API
    try:
        response = urllib.request.urlopen(plotting_api_url)
        print("Plotting API response:", response.read().decode())
    except Exception as e:
        print("Error calling plotting API:", e)

    return {
        "statusCode": 200,
        "body": "Driver completed successfully"
    }