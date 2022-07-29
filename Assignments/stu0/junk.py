import boto3


def aws():
    # https://boto3.amazonaws.com/v1/documentation/api/latest/guide/s3-example-creating-buckets.html
    s3 = boto3.client('s3')
    r = s3.list_buckets()
    for bucket in r['Buckets']:
        print(f'{bucket["Name"]}')

    s3 = boto3.client('s3')
    with open("uploadme.txt", "rb") as f:
        s3.upload_fileobj(f, "siu-ex1", "uploadme.txt")


if __name__ == '__main__':
    aws()
