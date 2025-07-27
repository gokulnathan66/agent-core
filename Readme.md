# About the code 

## Clone the Repo 
- Create a venv `python -m venv venv`
- Activate the venv `source venv/bin/activate`
- Install the requirements `pip install -r requirements.txt`
- Delete or move the the file of following to another folder cause, When deploying the agent these files will be recreated by the `agentcore` in you AWS account. You can keep these for your reference. For you to test the Agent you have to host the agent in your AWS account with Your IAM permissions. 
	- Dockerfile 
	- .bedrockagentcore.yaml 
	- .dockerignore 

```
- myagent.py : consist of code that calls the agent and do the work. the Bedrock SDK make so easy to Integration and Strands and Local testing.
- agent_tools.py : have all the tools required for the agent to function. You can add tools to this file , import in myagent.py to be accessed by strands.
- curl_commands.md used to test the agent locally
- requirements.txt : Required library
- Design/ : consist of this project Designs
- Attacthments/ : image attachments.
```



### Deploy Agent [AWS Docs Deploy link ](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/runtime-getting-started-toolkit.html#runtime-deploying-agent)
#### IAM role 
Configure your agent with the following command. For `YOUR_IAM_ROLE_ARN`, you need an IAM role with suitable permissions. For information see [Permissions for AgentCore Runtime](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/runtime-permissions.html).

![[IAM Role for Agent]]
Role ARN : 
```
arn:aws:iam::302263040839:role/Vesuvis_Agentcore_execution_role
```
#### Deployment steps 
```
## Deployment Steps

### Step 1: Configure Your Agent

# Run the configuration command to set up your agent:

agentcore configure --entrypoint agent_example.py -er <YOUR_IAM_ROLE_ARN>


# The command will:
##• Generate a Dockerfile and .dockerignore
##• Create a .bedrock_agentcore.yaml configuration file
```

```
agentcore configure --entrypoint myagent.py -er arn:aws:iam::302263040839:role/Vesuvis_Agentcore_execution_role
```

![[Pasted image 20250727005035.png]]


#### Deploy local mode 
```
agentcore launch -l
```

>[!ERROR] Local Running Olametary Running 
> Telemetary ERROR. This arise cause we din't deploy a telemetary service that used in Agentcore Observability cloud.

#### Deploy in Cloud 

#aws-commands 

```
agentcore launch
```

![[Pasted image 20250727080354.png]]

```
Agent Name: myagent                                                                                                                                 
Agent ARN: arn:aws:bedrock-agentcore:eu-central-1:302263040839:runtime/myagent-J4hSYhHVaX                                  
ECR URI: 302263040839.dkr.ecr.eu-central-1.amazonaws.com/bedrock-agentcore-myagent                                                          
```

- Note you Agent ARN that will be used to Invoke your agent further. 

### Invoke Agents [Agentcore Invoke agent](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/runtime-invoke-agent.html)

- From the Terminal you have you env variable as of now the agent is authenticated with IAM role so call the agent with 
```
agentcore invoke '{"prompt": "Hello"}'
```

#### Agent calls 
![[Pasted image 20250727133843.png]]

![[Pasted image 20250727133926.png]]

### Trouble Shoot [Agent troubleshoot](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/runtime-troubleshooting.html)

>[!ERROR] Local Running Olametary Running 
> Telemetary ERROR. This arise cause we din't deploy a telemetary service that used in Agentcore Observability 

### Cognito User Pool [[Cognito Guide]]
 - Use Cognito JWT and Oauth tokens to invoke the model. This will be Useful with customer Deployment 

### Deploy MCP servers [MCP](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/runtime-mcp.html)
- Deploy an MCP server 
### Create Strands Agent [Strands Agent](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/using-any-agent-framework.html#agent-runtime-frameworks-strands)

### Streaming services [Agent Core streaming](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/response-streaming.html)
