# Agent Core POC

A Proof of Concept implementation for AWS Bedrock AgentCore runtime with custom tools and deployment automation.

## 🚀 Quick Start

### Prerequisites
- AWS Account with appropriate permissions
- Python 3.8+
- AWS CLI configured
- Docker (for containerized deployment)

### Installation

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd agent-core
   ```

2. **Set up Python environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   pip install -r requirements.txt
   ```

3. **Clean up auto-generated files**
   
   > **Note**: Delete or move the following files before deployment as they will be recreated by AgentCore:
   > - `Dockerfile`
   > - `.bedrockagentcore.yaml`
   > - `.dockerignore`

## 📁 Project Structure

```
agent-core/
├── myagent.py              # Main agent code with Bedrock SDK integration
├── agent_tools.py          # Custom tools for agent functionality
├── curl_commands.md        # Local testing commands
├── requirements.txt        # Python dependencies
├── Design/                 # Project design documents
├── Attachments/           # Documentation images and IAM configurations
└── venv/                  # Python virtual environment
```

### File Descriptions

- **`myagent.py`**: Core agent implementation using Bedrock SDK for integration with Strands and local testing
- **`agent_tools.py`**: Collection of tools that extend agent functionality. Add new tools here and import them in `myagent.py`
- **`curl_commands.md`**: Commands for testing the agent locally
- **`requirements.txt`**: Required Python libraries
- **`Design/`**: Project design documents and implementation plans
- **`Attachments/`**: Image attachments and IAM role configurations

## 🔐 IAM Configuration

### Required IAM Role

The agent requires specific IAM permissions. Use the pre-configured role:

**Role ARN**: `arn:aws:iam::302263040839:role/Vesuvis_Agentcore_execution_role`

For detailed IAM configuration, see [IAM Role for Agent](./Attachments/IAM%20Role%20for%20Agent.md).

> **Important**: Configure your agent with suitable IAM permissions. See [AWS AgentCore Runtime Permissions](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/runtime-permissions.html) for details.

## 🚢 Deployment

### Step 1: Configure Your Agent

```bash
agentcore configure --entrypoint myagent.py -er arn:aws:iam::302263040839:role/Vesuvis_Agentcore_execution_role
```

This command will:
- Generate a `Dockerfile` and `.dockerignore`
- Create a `.bedrock_agentcore.yaml` configuration file

![Configuration Result](./Attachments/Pasted%20image%2020250727005035.png)

### Step 2: Deploy Locally (Development)

```bash
agentcore launch -l
```

> **Warning**: Local deployment may show telemetry errors. This occurs because we haven't deployed a telemetry service used in AgentCore Observability cloud.

### Step 3: Deploy to AWS Cloud

```bash
agentcore launch
```

![Cloud Deployment](./Attachments/Pasted%20image%2020250727080354.png)

**Deployment Output Example:**
```
Agent Name: myagent
Agent ARN: arn:aws:bedrock-agentcore:eu-central-1:302263040839:runtime/myagent-J4hSYhHVaX
ECR URI: 302263040839.dkr.ecr.eu-central-1.amazonaws.com/bedrock-agentcore-myagent
```

> **Important**: Save your Agent ARN as it will be needed to invoke your agent.

## 🎯 Invoking the Agent

### Terminal Invocation

Once deployed, invoke your agent using:

```bash
agentcore invoke '{"prompt": "Hello"}'
```

### Example Agent Calls

![Agent Call Example 1](./Attachments/Pasted%20image%2020250727133843.png)

![Agent Call Example 2](./Attachments/Pasted%20image%2020250727133926.png)

## 🔧 Troubleshooting

### Common Issues

> **Error**: Telemetry issues during local deployment
> 
> **Solution**: This error occurs because we haven't deployed a telemetry service used in AgentCore Observability. This is expected for local development.

> **Error**: Execution role policy error (Frankfurt region)
> 
> **Solution**: Keep your region set to `us-east-1`. When explicitly mentioning other regions like `eu-central-1`, Bedrock agent call exceptions may arise because Strands calls the default agent in `us-east-1`.

For more troubleshooting guidance, see [AWS AgentCore Troubleshooting](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/runtime-troubleshooting.html).

## 🔗 Additional Resources

### Authentication & Security
- **Cognito User Pool**: Use Cognito JWT and OAuth tokens to invoke the model for customer deployments

### Advanced Features
- **[MCP Servers](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/runtime-mcp.html)**: Deploy Model Context Protocol servers
- **[Strands Agent](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/using-any-agent-framework.html#agent-runtime-frameworks-strands)**: Create Strands-based agents
- **[Streaming Services](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/response-streaming.html)**: Implement response streaming

## 📚 Documentation Links

- [AWS AgentCore Runtime Getting Started](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/runtime-getting-started-toolkit.html#runtime-deploying-agent)
- [AgentCore Runtime Permissions](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/runtime-permissions.html)
- [Invoking Agents](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/runtime-invoke-agent.html)
- [Troubleshooting Guide](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/runtime-troubleshooting.html)

---

**Region**: us-east-1  
**Account ID**: 302263040839  
**Agent Name**: agent0.1-Vesuvius 