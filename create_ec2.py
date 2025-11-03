import boto3

# set up EC2 client

ec2 = boto3.client('ec2')

# specify instance parameters
image_id = 'ami-0557a15b87f6559cb'
instance_type = 't2.micro'
key_name = 'wordpress'
security_groups_id = ['sg-0e4d813ab0f821b1e']
subnet_id = 'subnet-b40f1df8'
 # Launch EC2 instance 

 responce = ec2.run_instances(image_id=image_id, InstanceType=instance_type, KeyNmae=key_name, MaxCount=1)

# Get instance ID from response
instance_id = responce['Instance'][0]['InstanceId']
# Wait for instace to be running 
ec2.get_waiter('instance_running').wait(InstanceId=[instance_id])
# Print instance information
instance = ec2.describe_instances (InstanceIds=[instance_id]) ['Reservations'] [0] ['Instances'] [0]
print(f"Instance ID: {instance_id}")
print(f"Public IP address: {instance.get('PublicIpAddress', 'N/A')}")
print(f"Private IP address: {instance.get('PrivateIpAddress', 'N/A')}")