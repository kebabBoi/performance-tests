import httpx

response = httpx.get("https://jsonplaceholder.typicode.com/todos/1")

print(response.status_code)
print(response.text) #словарь
print(response.json()) #пайтон объект

data = {
    "tittle": "Новая задача",
    "completed": False,
    "UserId": 1
}

response = httpx.post("https://jsonplaceholder.typicode.com/todos")

print(response.status_code)
print(response.text) #словарь
print(response.json()) #пайтон объект

headers = {"Authorization": "Bearer my_secret_token"}
response = httpx.get("https://httpbin.org/get", headers=headers)

print(response.status_code)
print(response.text) #словарь
print(response.request.headers)
print(response.headers) #словарь
print(response.json()) #пайтон объект

params = {"userId": 1}
response = httpx.get("https://jsonplaceholder.typicode.com/todos", params=params)

print(response.status_code)
print(response.text) #словарь
print(response.json()) #пайтон объект
print(response.request.url, response.request.url.query)

files = {"file": ("example.txt", open("example.txt", "rb"))}
response = httpx.post("https://httpbin.org/post", files=files)

print(response.status_code)
print(response.text) #словарь
print(response.json()) #пайтон объект

with httpx.Client() as client:
    response1 = client.get("https://jsonplaceholder.typicode.com/todos/1")
    response2 = client.get("https://jsonplaceholder.typicode.com/todos/2")

print(response1.json())
print(response2.json())

client = httpx.Client(
    base_url="https://jsonplaceholder.typicode.com",
    headers={"Authorization": "Bearer my_secret_token"}
)
response1 = client.get("/todos/1")
response2 = client.get("/todos/2")

print(response1.json())
print(response1.headers)
print(response2.json())

try:
    response = httpx.get("https://jsonplaceholder.typicode.com/invalid-url")
    response.raise_for_status()
except httpx.HTTPStatusError as e:
    print(f"Error request: {e}")

try:
    response = httpx.get("https://httpbin.org/delay/5", timeout=2)
except httpx.ReadTimeout as e:
    print("Превышен лимит времени")