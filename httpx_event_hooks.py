from httpx import Client, Request, Response
from datetime import datetime

def log_request(request: Request):
    request.extensions['start time'] = datetime.now()
    print(f"request: {request.method}")

def log_response(response: Response):
    duration = datetime.now() - response.request.extensions['start time']
    print(f"response: {response.status_code}, {duration}")


client = Client(
    base_url="http://localhost:8003/",
    event_hooks={"request": [log_request], "response": [log_response]}
)
response = client.get("/api/v1/users/569bf699-0f25-4a6e-b248-54e6c43d6737")
print(response)