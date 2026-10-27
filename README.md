# Serverless S3 Analytics

A serverless AWS project that tracks file sizes in Amazon S3, stores historical data in DynamoDB, and generates plots to visualize how object sizes change over time.

## Overview

This project was built to practice designing an event-driven cloud application using AWS services.

The system uses AWS Lambda functions to respond to S3 activity, record object-size information, and generate visualizations from the stored history.

## Architecture

The project uses the following AWS services:

- **Amazon S3** — stores uploaded files and generated plots
- **AWS Lambda** — processes S3 events and runs the application logic
- **Amazon DynamoDB** — stores historical file-size information
- **Amazon CloudWatch** — provides logs for debugging and monitoring
- **Python / Boto3** — interacts with AWS services programmatically
- **Matplotlib** — generates plots from historical object-size data

A simplified workflow looks like this:

```text
File uploaded to S3
        |
        v
Size Tracking Lambda
        |
        v
    DynamoDB
        |
        v
   Driver Lambda
        |
        v
 Plotting Lambda
        |
        v
Generated Plot -> S3
```

## Project Files

```text
serverless-s3-analytics/
├── driver_lambda.py
├── plotting_lambda.py
├── setup_resources.py
├── size_tracking_lambda.py
├── .gitignore
└── README.md
```

### `setup_resources.py`

Creates or configures the AWS resources required by the project.

### `size_tracking_lambda.py`

Processes S3 object events and records object-size information in DynamoDB.

### `driver_lambda.py`

Coordinates the workflow and triggers the required processing steps.

### `plotting_lambda.py`

Reads historical object-size data and generates a visualization using Matplotlib.

## What I Learned

This project helped me gain hands-on experience with:

- Building serverless applications using AWS
- Configuring Lambda functions and event triggers
- Working with S3 events
- Designing and querying DynamoDB tables
- Using Boto3 to interact with AWS services
- Managing IAM permissions between AWS services
- Debugging Lambda functions using CloudWatch logs
- Configuring Lambda memory and timeout settings
- Generating and storing plots programmatically
- Testing an event-driven application from end to end

## Challenges

Some of the main challenges included:

- Configuring the correct IAM permissions for each Lambda function
- Understanding how S3 event notifications trigger Lambda
- Debugging failures through CloudWatch logs
- Managing dependencies required by the plotting Lambda
- Resetting S3 and DynamoDB data between tests
- Understanding the order in which the Lambda functions interact

Working through these issues helped me better understand how individual AWS services work together in a serverless architecture.

## Running the Project

This project requires an AWS account and appropriate IAM permissions.

The general setup process is:

1. Configure AWS credentials locally.
2. Create the required S3 bucket and DynamoDB table.
3. Deploy the Lambda functions.
4. Configure the required S3 event triggers.
5. Upload a file to S3.
6. Verify that object-size information is written to DynamoDB.
7. Run the plotting workflow.
8. View the generated plot in S3.

## Security

AWS credentials and sensitive configuration files should never be committed to this repository.

The `.gitignore` excludes common local and sensitive files such as:

```text
.venv/
__pycache__/
*.pyc
.env
.DS_Store
```

## Future Improvements

Possible improvements include:

- Deploying the infrastructure with AWS SAM, CDK, or Terraform
- Adding automated tests
- Adding API Gateway for an HTTP interface
- Creating a web dashboard for the generated analytics
- Adding CloudWatch alarms and monitoring
- Improving error handling and logging
- Automating deployment with GitHub Actions

## Purpose

This project is part of my ongoing learning in cloud computing, serverless architecture, Python, and AWS development.
