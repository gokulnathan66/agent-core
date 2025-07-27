#agent_tools.py
from strands import Agent, tool
from strands_tools import calculator, file_read, shell, http_request
import boto3




def get_current_weather(city: str) -> str:
    """Get the current weather for a given city"""
    return f"The weather in {city} is sunny"

weather_tool = tool(
    name="get_current_weather",
    description="Get the current weather for a given city",
    func=get_current_weather,
)


def list_all_ec2_instance() -> str:
    """List all EC2 instances"""
    try:
        ec2 = boto3.client('ec2')
        response = ec2.describe_instances()
        
        instance_ids = []
        for reservation in response['Reservations']:
            for instance in reservation['Instances']:
                instance_ids.append(instance['InstanceId'])
        
        return f"EC2 instances listed: {instance_ids}"
    except Exception as e:
        return f"Error listing EC2 instances: {str(e)}"


ec2_tool = tool(
    name="list_all_ec2_instance",
    description="List all EC2 instances",
    func=list_all_ec2_instance,
)

if __name__ == "__main__":
    print(list_all_ec2_instance())