#myagent.py
from bedrock_agentcore.runtime import BedrockAgentCoreApp
from strands import Agent
from agent_tools import weather_tool, ec2_tool

app = BedrockAgentCoreApp()
agent = Agent(tools=[weather_tool, ec2_tool])

@app.entrypoint
def invoke(payload):
    """Process user input and return a response"""
    user_message = payload.get("prompt", "Hello")
    result = agent(user_message)
    return {"result": result.message}

if __name__ == "__main__":
    app.run()

