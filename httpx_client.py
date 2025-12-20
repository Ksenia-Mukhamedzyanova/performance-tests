import httpx
import time

client = httpx.Client(
    base_url="http://localhost:8003",
    timeout=10,
    headers={"Authorization": "Bearer ..."}
)

payload = {
    "email": f"user.{time.time()}9990@example.com",
    "lastName": "string",
    "firstName": "string",
    "middleName": "string",
    "phoneNumber": "string"
}

response = client.post("/api/v1/users", json=payload)
print(response.text)