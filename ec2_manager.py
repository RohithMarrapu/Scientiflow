import boto3
import time

ec2 = boto3.resource('ec2')
client = boto3.client('ec2')

def launch_instance():
    script = '''#!/bin/bash
    echo "Starting Script" > /home/ec2-user/output.txt
    sleep 5
    echo "Done Sleeping" >> /home/ec2-user/output.txt
    '''

    instance = ec2.create_instances(
        ImageId='ami-03f4878755434977f',  # Amazon Linux 2 AMI (adjust region)
        MinCount=1,
        MaxCount=1,
        InstanceType='t2.micro',
        KeyName='cli-key',  # Replace with your existing key
        UserData=script,
        TagSpecifications=[{
            'ResourceType': 'instance',
            'Tags': [{'Key': 'Name', 'Value': 'AutomationInstance'}]
        }],
    )[0]

    print("Launching instance...")
    instance.wait_until_running()
    instance.load()
    print(f"Instance {instance.id} is running at {instance.public_dns_name}")
    return instance

def get_output(instance):
    print("Waiting for script to complete...")
    time.sleep(60)  # Wait for user-data script to finish
    ssm_client = boto3.client('ssm')
    
    # Make instance SSM ready
    print("Ensure instance has IAM role allowing SSM to fetch commands")

def terminate_instance(instance_id):
    print(f"Terminating instance {instance_id}")
    client.terminate_instances(InstanceIds=[instance_id])
    waiter = client.get_waiter('instance_terminated')
    waiter.wait(InstanceIds=[instance_id])
    print("Instance terminated.")

if __name__ == "__main__":
    instance = launch_instance()
    # get_output(instance) # Optional, can fetch SSM or log output
    terminate_instance(instance.id)
