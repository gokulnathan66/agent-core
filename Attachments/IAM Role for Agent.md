[Deployment Permissions for AgentCore Runtime Link](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/runtime-permissions.html)

region : us-east-1
accountId: 302263040839
agentName: agent0.1-Vesuvius
RoleName : Vesuvis_Agentcore_execution_role : Created
PolicyName : Vesuvis_Agentcore_execution_role_policy : Created

Replace the Appropriate `region`, `accountid` and `agentname` correctly 
#### Trouble shoot : Execution role policy error 
- the policy of cross central of franfrut is not working rolling back to us-east-1: this error happen because of a little stunt i did to deploy agent on the frankfrut region eu-central-1. 

>[!NOTE] Keep your region to default to us-east-1
> When we explicitly mention any other region, like eu-central-1 the bedrock agentcall exception arise this is caused by the Strands calling the default agent in the `us-east-1` (i think) It will probably work when that mentioned explicitly in the code 


# Execution Policy
```
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "ECRImageAccess",
            "Effect": "Allow",
            "Action": [
                "ecr:BatchGetImage",
                "ecr:GetDownloadUrlForLayer"
            ],
            "Resource": [
                "arn:aws:ecr:region:accountId:repository/*"
            ]        
        },
        {
            "Effect": "Allow",
            "Action": [
                "logs:DescribeLogStreams",
                "logs:CreateLogGroup"
            ],
            "Resource": [
                "arn:aws:logs:region:accountId:log-group:/aws/bedrock-agentcore/runtimes/*"
            ]
        },
        {
            "Effect": "Allow",
            "Action": [
                "logs:DescribeLogGroups"
            ],
            "Resource": [
                "arn:aws:logs:region:accountId:log-group:*"
            ]
        },
        {
            "Effect": "Allow",
            "Action": [
                "logs:CreateLogStream",
                "logs:PutLogEvents"
            ],
            "Resource": [
                "arn:aws:logs:region:accountId:log-group:/aws/bedrock-agentcore/runtimes/*:log-stream:*"
            ]
        },
        {
            "Sid": "ECRTokenAccess",
            "Effect": "Allow",
            "Action": [
                "ecr:GetAuthorizationToken"
            ],
            "Resource": "*"
        },
        {
        "Effect": "Allow", 
        "Action": [ 
            "xray:PutTraceSegments", 
            "xray:PutTelemetryRecords", 
            "xray:GetSamplingRules", 
            "xray:GetSamplingTargets"
            ],
         "Resource": [ "*" ] 
         },
         {
            "Effect": "Allow",
            "Resource": "*",
            "Action": "cloudwatch:PutMetricData",
            "Condition": {
                "StringEquals": {
                    "cloudwatch:namespace": "bedrock-agentcore"
                }
            }
        },
        {
            "Sid": "GetAgentAccessToken",
            "Effect": "Allow",
            "Action": [
                "bedrock-agentcore:GetWorkloadAccessToken",
                "bedrock-agentcore:GetWorkloadAccessTokenForJWT",
                "bedrock-agentcore:GetWorkloadAccessTokenForUserId"
            ],
            "Resource": [
              "arn:aws:bedrock-agentcore:region:accountId:workload-identity-directory/default",
              "arn:aws:bedrock-agentcore:region:accountId:workload-identity-directory/default/workload-identity/agentName-*"
            ]
        },
         {"Sid": "BedrockModelInvocation", 
         "Effect": "Allow", 
         "Action": [ 
                "bedrock:InvokeModel", 
                "bedrock:InvokeModelWithResponseStream"
              ], 
        "Resource": [
            "arn:aws:bedrock:*::foundation-model/*",
            "arn:aws:bedrock:region:accountId:*"
        ]
        }
    ]
}
```

```
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "ECRImageAccess",
            "Effect": "Allow",
            "Action": [
                "ecr:BatchGetImage",
                "ecr:GetDownloadUrlForLayer"
            ],
            "Resource": [
                "arn:aws:ecr:eu-central-1:302263040839:repository/*"
            ]        
        },
        {
            "Effect": "Allow",
            "Action": [
                "logs:DescribeLogStreams",
                "logs:CreateLogGroup"
            ],
            "Resource": [
                "arn:aws:logs:eu-central-1:302263040839:log-group:/aws/bedrock-agentcore/runtimes/*"
            ]
        },
        {
            "Effect": "Allow",
            "Action": [
                "logs:DescribeLogGroups"
            ],
            "Resource": [
                "arn:aws:logs:eu-central-1:302263040839:log-group:*"
            ]
        },
        {
            "Effect": "Allow",
            "Action": [
                "logs:CreateLogStream",
                "logs:PutLogEvents"
            ],
            "Resource": [
                "arn:aws:logs:eu-central-1:302263040839:log-group:/aws/bedrock-agentcore/runtimes/*:log-stream:*"
            ]
        },
        {
            "Sid": "ECRTokenAccess",
            "Effect": "Allow",
            "Action": [
                "ecr:GetAuthorizationToken"
            ],
            "Resource": "*"
        },
        {
        "Effect": "Allow", 
        "Action": [ 
            "xray:PutTraceSegments", 
            "xray:PutTelemetryRecords", 
            "xray:GetSamplingRules", 
            "xray:GetSamplingTargets"
            ],
         "Resource": [ "*" ] 
         },
         {
            "Effect": "Allow",
            "Resource": "*",
            "Action": "cloudwatch:PutMetricData",
            "Condition": {
                "StringEquals": {
                    "cloudwatch:namespace": "bedrock-agentcore"
                }
            }
        },
        {
            "Sid": "GetAgentAccessToken",
            "Effect": "Allow",
            "Action": [
                "bedrock-agentcore:GetWorkloadAccessToken",
                "bedrock-agentcore:GetWorkloadAccessTokenForJWT",
                "bedrock-agentcore:GetWorkloadAccessTokenForUserId"
            ],
            "Resource": [
              "arn:aws:bedrock-agentcore:eu-central-1:302263040839:workload-identity-directory/default*",
              "arn:aws:bedrock-agentcore:eu-central-1:302263040839:workload-identity-directory/default/workload-identity/agentName-*"
            ]
        },
         {"Sid": "BedrockModelInvocation", 
         "Effect": "Allow", 
         "Action": [ 
                "bedrock:InvokeModel", 
                "bedrock:InvokeModelWithResponseStream"
              ], 
        "Resource": [
            "arn:aws:bedrock:*::foundation-model/*",
            "arn:aws:bedrock:eu-central-1:302263040839:*"
        ]
        }
    ]
}
```
# Trust Policy 
```

{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Sid": "AssumeRolePolicy",
      "Effect": "Allow",
      "Principal": {
        "Service": "bedrock-agentcore.amazonaws.com"
      },
      "Action": "sts:AssumeRole",
      "Condition": {
            "StringEquals": {
                "aws:SourceAccount": "accountId"
            },
            "ArnLike": {
                "aws:SourceArn": "arn:aws:bedrock-agentcore:region:accountId:*"
            }
       }
    }
  ]
}
      
```

# Created the Role 

```
arn:aws:iam::302263040839:role/Vesuvis_Agentcore_execution_role
```