from grpc import Channel
from clients.grpc.client import GRPCClient
from clients.grpc.gateway.client import build_gateway_grpc_client
from contracts.services.gateway.operations.operations_gateway_service_pb2_grpc import OperationsGatewayServiceStub
from contracts.services.gateway.operations.rpc_get_operation_pb2 import (
    GetOperationRequest,
    GetOperationResponse
)
from contracts.services.gateway.operations.rpc_get_operation_receipt_pb2 import (
    GetOperationReceiptRequest,
    GetOperationReceiptResponse
)
from contracts.services.gateway.operations.rpc_get_operations_pb2 import (
    GetOperationsRequest,
    GetOperationsResponse
)
from contracts.services.gateway.operations.rpc_get_operations_summary_pb2 import (
    GetOperationsSummaryRequest,
    GetOperationsSummaryResponse
)
from contracts.services.gateway.operations.rpc_make_top_up_operation_pb2 import (
    MakeTopUpOperationRequest,
    MakeTopUpOperationResponse
)
from contracts.services.gateway.operations.rpc_make_fee_operation_pb2 import (
    MakeFeeOperationRequest,
    MakeFeeOperationResponse
)
from contracts.services.gateway.operations.rpc_make_cashback_operation_pb2 import (
    MakeCashbackOperationRequest,
    MakeCashbackOperationResponse
)
from contracts.services.gateway.operations.rpc_make_transfer_operation_pb2 import (
    MakeTransferOperationRequest,
    MakeTransferOperationResponse
)
from contracts.services.gateway.operations.rpc_make_purchase_operation_pb2 import (
    MakePurchaseOperationRequest,
    MakePurchaseOperationResponse
)
from contracts.services.gateway.operations.rpc_make_bill_payment_operation_pb2 import (
    MakeBillPaymentOperationRequest,
    MakeBillPaymentOperationResponse
)
from contracts.services.gateway.operations.rpc_make_cash_withdrawal_operation_pb2 import (
    MakeCashWithdrawalOperationRequest,
    MakeCashWithdrawalOperationResponse
)
from tools.fakers import fake

class OperationsGatewayGRPCClient(GRPCClient):
    def __init__(self, channel: Channel):
        super().__init__(channel)

        self.stub = OperationsGatewayServiceStub(channel)

    def get_operation_api(self, request: GetOperationRequest) -> GetOperationResponse:
        return self.stub.GetOperation(request)

    def get_operation_receipt_api(self, request: GetOperationReceiptRequest) -> GetOperationReceiptResponse:
        return self.stub.GetOperationReceipt(request)

    def get_operations_api(self, request: GetOperationsRequest) -> GetOperationsResponse:
        return self.stub.GetOperations(request)

    def get_operations_summary_api(self, request: GetOperationsSummaryRequest) -> GetOperationsSummaryResponse:
        return self.stub.GetOperationsSummary(request)

    def make_fee_operation_api(self, request: MakeFeeOperationRequest) -> MakeFeeOperationResponse:
        return self.stub.MakeFeeOperation(request)

    def make_top_up_operation_api(self, request: MakeTopUpOperationRequest) -> MakeTopUpOperationResponse:
        return self.stub.MakeTopUpOperation(request)

    def make_cashback_operation_api(self, request: MakeCashbackOperationRequest) -> MakeCashbackOperationResponse:
        return self.stub.MakeCashbackOperation(request)

    def make_transfer_operation_api(self, request: MakeTransferOperationRequest) -> MakeTransferOperationResponse:
        return self.stub.MakeTransferOperation(request)

    def make_purchase_operation_api(self, request: MakePurchaseOperationRequest) -> MakePurchaseOperationResponse:
        return self.stub.MakePurchaseOperation(request)

    def make_bill_payment_operation_api(self, request: MakeBillPaymentOperationRequest) -> MakeBillPaymentOperationResponse:
        return self.stub.MakeBillPaymentOperation(request)

    def make_cash_withdrawal_operation_api(self, request: MakeCashWithdrawalOperationRequest) -> MakeCashWithdrawalOperationResponse:
        return self.stub.MakeCashWithdrawalOperation(request)

    def get_operations(self, account_id: str) -> GetOperationsResponse:
        request = GetOperationsRequest(account_id=account_id)
        return self.get_operations_api(request)

    def get_operations_summary(self, account_id: str) -> GetOperationsSummaryResponse:
        request = GetOperationsSummaryRequest(account_id=account_id)
        return self.get_operations_summary_api(request)

    def get_operation_receipt(self, operation_id: str) -> GetOperationReceiptResponse:
        request = GetOperationReceiptRequest(operation_id=operation_id)
        return self.get_operation_receipt_api(request)

    def get_operation(self, operation_id: str) -> GetOperationResponse:
        request = GetOperationRequest(operation_id=operation_id)
        return self.get_operation_api(request)

    def make_fee_operation(self, card_id: str, account_id: str) -> MakeFeeOperationResponse:
        request = MakeFeeOperationRequest(
            card_id=card_id,
            account_id=account_id
        )
        return self.make_fee_operation_api(request)

    def make_top_up_operation(self, card_id: str, account_id: str) -> MakeTopUpOperationResponse:
        request = MakeTopUpOperationRequest(
            card_id=card_id,
            account_id=account_id
        )
        return self.make_top_up_operation_api(request)

    def make_cash_back_operation(self, card_id: str, account_id: str) -> MakeCashbackOperationResponse:
        request = MakeCashbackOperationRequest(
            card_id=card_id,
            account_id=account_id
        )
        return self.make_cashback_operation_api(request)

    def make_transfer_operation(self, card_id: str, account_id: str) -> MakeTransferOperationResponse:
        request = MakeTransferOperationRequest(
            card_id=card_id,
            account_id=account_id
        )
        return self.make_transfer_operation_api(request)

    def make_purchase_operation(self, card_id: str, account_id: str) -> MakePurchaseOperationResponse:
        request = MakePurchaseOperationRequest(
            card_id=card_id,
            account_id=account_id
        )
        return self.make_purchase_operation_api(request)

    def make_bill_payment_operation(self, card_id: str, account_id: str) -> MakeBillPaymentOperationResponse:
        request = MakeBillPaymentOperationRequest(
            card_id=card_id,
            account_id=account_id
        )
        return self.make_bill_payment_operation_api(request)

    def make_cash_withdrawal_operation(self, card_id: str, account_id: str) -> MakeCashWithdrawalOperationResponse:
        request = MakeCashWithdrawalOperationRequest(
            card_id=card_id,
            account_id=account_id
        )
        return self.make_cash_withdrawal_operation_api(request)

def build_operations_gateway_grpc_client() -> OperationsGatewayGRPCClient:
    return OperationsGatewayGRPCClient(channel=build_gateway_grpc_client())