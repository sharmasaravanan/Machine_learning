import boto3

ec2 = boto3.client('ec2')

autoscale = boto3.client('autoscaling')
rdbs = boto3.client('rds')

s3 = boto3.client('s3')

s3 = boto3.resource('s3')

ec2.start_instances(InstanceIds=["i-0b69242e2e717b5d5"], DryRun=False)
ec2.stop_instances(InstanceIds=[id], DryRun=False)
rdbs.start_db_instance(DBInstanceIdentifier=name)
rdbs.stop_db_instance(DBInstanceIdentifier=name)
ec2.describe_instances(InstanceIds=[instant])

s3.Bucket(bucket).upload_file(local_file, s3_file)
s3.Bucket(bucket).download_file(s3_file, local_file)
