# Call the Agent 
curl -X POST http://localhost:8080/invocations \
-H "Content-Type: application/json" \
-d '{"prompt": "what can you do"}'

curl -X POST http://localhost:8080/invocations \
-H "Content-Type: application/json" \
-d '{"prompt": "what Tell me the weather on chennai"}'

# Listing instance in the Agent

curl -X POST http://localhost:8080/invocations \
-H "Content-Type: application/json" \
-d '{"prompt": "what list the instance in my account: use the list instacne tool i given you "}'


curl -X POST http://localhost:8080/invocations \
-H "Content-Type: application/json" \
-d '{"prompt": "what list the instance in my account"}'
