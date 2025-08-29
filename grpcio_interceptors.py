import grpc
from contracts.services.gateway.users.rpc_get_user_pb2 import GetUserRequest
from contracts.services.gateway.users.users_gateway_service_pb2_grpc import UsersGatewayServiceStub

class SimpleLoggingInterceptor(grpc.UnaryUnaryClientInterceptor):
    def intercept_unary_unary(self, continuation, client_call_details, request):
        # Печатаем имя вызываемого метода
        print(client_call_details, type(client_call_details))
        print(request)
        print(f"[gRPC Interceptor] Calling method: {client_call_details.method}")

        # Выполняем реальный RPC вызов
        response = continuation(client_call_details, request)

        return response

interceptors = [SimpleLoggingInterceptor()]
channel = grpc.insecure_channel("localhost:9003")
intercept_channel = grpc.intercept_channel(channel, *interceptors)
# intercept_channel = grpc.intercept_channel(channel, SimpleLoggingInterceptor())

# Теперь создаём клиента на основе intercept_channel
stub = UsersGatewayServiceStub(intercept_channel)


request = GetUserRequest(id="eb0254f4-bb0d-4d32-ad66-e7c58d4abc35")
response = stub.GetUser(request)
print(response)
# Все вызовы будут логгироваться:
# client.CreateUser(...)
# client.GetUser(...)
