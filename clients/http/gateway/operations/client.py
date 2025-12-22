from typing import TypedDict
from clients.http.client import HTTPClient
from httpx import Response, QueryParams

class GetOperationsQueryDict(TypedDict):
    """
    Структура query параметров запроса для получения списка операций по счёту.
    """
    accountId: str

class GetOperationsSummaryQueryDict(TypedDict):
    """
    Структура query параметров запроса для получения статистики по операциям счёта.
    """
    accountId: str

class MakeFreeOperationRequestDict(TypedDict):
    """
    Базовая структура тела запроса для создания финансовой операции.
    """
    status: str
    amount: float
    cardId: str
    accountId: str

class MakeTopUpOperationRequestDict(TypedDict):
    """
    Структура запроса для создания операции пополнения.
    """
    status: str
    amount: float
    cardId: str
    accountId: str

class MakeCashBackOperationRequestDict(TypedDict):
    """
    Структура запроса для создания операции кэшбэка.
    """
    status: str
    amount: float
    cardId: str
    accountId: str

class MakeTransferOperationRequestDict(TypedDict):
    """
    Структура запроса для создания операции перевода.
    """
    status: str
    amount: float
    cardId: str
    accountId: str

class MakePurchaseOperationRequestDict(TypedDict):
    """
    Структура запроса для создания операции покупки.

    Дополнительное поле:
    - category: категория покупки.
    """
    status: str
    amount: float
    cardId: str
    accountId: str
    category: str

class MakeBillPaymentOperationRequestDict(TypedDict):
    """
    Структура запроса для создания операции оплаты по счёту.
    """
    status: str
    amount: float
    cardId: str
    accountId: str

class MakeCashWithdrawalOperationRequestDict(TypedDict):
    """
    Структура запроса для создания операции снятия наличных.
    """
    status: str
    amount: float
    cardId: str
    accountId: str

class OperationsGatewayHTTPClient(HTTPClient):
    """
    Клиент для взаимодействия с /api/v1/operations сервиса http-gateway.
    """

    def get_operation_api(self, query: GetOperationsQueryDict) -> Response:
        """
        Получает информацию об операции по её идентификатору.

        :param operation_id: Уникальный идентификатор операции.
        :return: Объект httpx.Response с данными об операции.
        """
        return self.get("/api/v1/operations", params=QueryParams(**query))

    def get_operation_receipt_api(self, query: GetOperationsSummaryQueryDict) -> Response:
        """
        Получает чек по заданной операции.

        :param operation_id: Уникальный идентификатор операции.
        :return: Объект httpx.Response с чеком по операции.
        """
        return self.get("/api/v1/operations/operations-summary", params=QueryParams(**query))

    def get_operations_api(self, operation_id: str) -> Response:
        """
        Получает список операций по счёту.

        :param query: Словарь с параметром accountId.
        :return: Объект httpx.Response с операциями по счёту.
        """
        return self.get(f"/api/v1/operations/operation-receipts/{operation_id}")

    def get_operations_summary_api(self, operation_id: str) -> Response:
        """
        Получает сводную статистику операций по счёту.

        :param query: Словарь с параметром accountId.
        :return: Объект httpx.Response с агрегированной информацией.
        """
        return self.get(f"/api/v1/operations/{operation_id}")

    def make_fee_operation_api(self, request: MakeFreeOperationRequestDict) -> Response:
        """
        Создаёт операцию комиссии.

        :param request: Тело запроса с параметрами операции.
        :return: Объект httpx.Response с результатом операции.
        """
        return self.post("/api/v1/operations/make-fee-operation", json=request)

    def make_top_up_operation_api(self, request: MakeTopUpOperationRequestDict) -> Response:
        """
        Создаёт операцию пополнения счёта.

        :param request: Тело запроса с параметрами операции.
        :return: Объект httpx.Response с результатом операции.
        """
        return self.post("/api/v1/operations/make-top-up-operation", json=request)

    def make_cashback_operation_api(self, request: MakeCashBackOperationRequestDict) -> Response:
        """
        Создаёт операцию начисления кэшбэка.

        :param request: Тело запроса с параметрами операции.
        :return: Объект httpx.Response с результатом операции.
        """
        return self.post("/api/v1/operations/make-cashback-operation", json=request)

    def make_transfer_operation_api(self, request: MakeTransferOperationRequestDict) -> Response:
        """
        Создаёт операцию перевода средств.

        :param request: Тело запроса с параметрами операции.
        :return: Объект httpx.Response с результатом операции.
        """
        return self.post("/api/v1/operations/make-transfer-operation", json=request)

    def make_purchase_operation_api(self, request: MakePurchaseOperationRequestDict) -> Response:
        """
        Создаёт операцию покупки.

        :param request: Тело запроса с параметрами операции, включая категорию.
        :return: Объект httpx.Response с результатом операции.
        """
        return self.post("/api/v1/operations/make-purchase-operation", json=request)

    def make_bill_payment_operation_api(self, request: MakeBillPaymentOperationRequestDict) -> Response:
        """
        Создаёт операцию оплаты счёта.

        :param request: Тело запроса с параметрами операции.
        :return: Объект httpx.Response с результатом операции.
        """
        return self.post("/api/v1/operations/make-bill-payment-operation", json=request)

    def make_cash_withdrawal_operation_api(self, request: MakeCashWithdrawalOperationRequestDict) -> Response:
        """
        Создаёт операцию снятия наличных средств.

        :param request: Тело запроса с параметрами операции.
        :return: Объект httpx.Response с результатом операции.
        """
        return self.post("/api/v1/operations/make-cash-withdrawal-operation", json=request)