# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc
import warnings

from TinkoffPy.grpc import users_pb2 as TinkoffPy_dot_grpc_dot_users__pb2

GRPC_GENERATED_VERSION = '1.70.0'
GRPC_VERSION = grpc.__version__
_version_not_supported = False

try:
    from grpc._utilities import first_version_is_lower
    _version_not_supported = first_version_is_lower(GRPC_VERSION, GRPC_GENERATED_VERSION)
except ImportError:
    _version_not_supported = True

if _version_not_supported:
    raise RuntimeError(
        f'The grpc package installed is at version {GRPC_VERSION},'
        + f' but the generated code in TinkoffPy/grpc/users_pb2_grpc.py depends on'
        + f' grpcio>={GRPC_GENERATED_VERSION}.'
        + f' Please upgrade your grpc module to grpcio>={GRPC_GENERATED_VERSION}'
        + f' or downgrade your generated code using grpcio-tools<={GRPC_VERSION}.'
    )


class UsersServiceStub(object):
    """С помощью сервиса можно получить: <br/> 1.
    список счетов пользователя; <br/> 2. маржинальные показатели по счeту.
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.GetAccounts = channel.unary_unary(
                '/tinkoff.public.invest.api.contract.v1.UsersService/GetAccounts',
                request_serializer=TinkoffPy_dot_grpc_dot_users__pb2.GetAccountsRequest.SerializeToString,
                response_deserializer=TinkoffPy_dot_grpc_dot_users__pb2.GetAccountsResponse.FromString,
                _registered_method=True)
        self.GetMarginAttributes = channel.unary_unary(
                '/tinkoff.public.invest.api.contract.v1.UsersService/GetMarginAttributes',
                request_serializer=TinkoffPy_dot_grpc_dot_users__pb2.GetMarginAttributesRequest.SerializeToString,
                response_deserializer=TinkoffPy_dot_grpc_dot_users__pb2.GetMarginAttributesResponse.FromString,
                _registered_method=True)
        self.GetUserTariff = channel.unary_unary(
                '/tinkoff.public.invest.api.contract.v1.UsersService/GetUserTariff',
                request_serializer=TinkoffPy_dot_grpc_dot_users__pb2.GetUserTariffRequest.SerializeToString,
                response_deserializer=TinkoffPy_dot_grpc_dot_users__pb2.GetUserTariffResponse.FromString,
                _registered_method=True)
        self.GetInfo = channel.unary_unary(
                '/tinkoff.public.invest.api.contract.v1.UsersService/GetInfo',
                request_serializer=TinkoffPy_dot_grpc_dot_users__pb2.GetInfoRequest.SerializeToString,
                response_deserializer=TinkoffPy_dot_grpc_dot_users__pb2.GetInfoResponse.FromString,
                _registered_method=True)


class UsersServiceServicer(object):
    """С помощью сервиса можно получить: <br/> 1.
    список счетов пользователя; <br/> 2. маржинальные показатели по счeту.
    """

    def GetAccounts(self, request, context):
        """GetAccounts — счета пользователя
        Получить список счетов.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetMarginAttributes(self, request, context):
        """GetMarginAttributes — маржинальные показатели по счeту
        Метод позволяет получить маржинальные показатели и ликвидность по заданному счeту.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetUserTariff(self, request, context):
        """GetUserTariff — тариф пользователя
        Получить информацию о текущих лимитах на подклчение, согласно текущему тарифу пользователя.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetInfo(self, request, context):
        """GetInfo — информация о пользователе
        Получить информацию о пользователе: тариф, признак квалификации, пройденные тесты и др.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_UsersServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'GetAccounts': grpc.unary_unary_rpc_method_handler(
                    servicer.GetAccounts,
                    request_deserializer=TinkoffPy_dot_grpc_dot_users__pb2.GetAccountsRequest.FromString,
                    response_serializer=TinkoffPy_dot_grpc_dot_users__pb2.GetAccountsResponse.SerializeToString,
            ),
            'GetMarginAttributes': grpc.unary_unary_rpc_method_handler(
                    servicer.GetMarginAttributes,
                    request_deserializer=TinkoffPy_dot_grpc_dot_users__pb2.GetMarginAttributesRequest.FromString,
                    response_serializer=TinkoffPy_dot_grpc_dot_users__pb2.GetMarginAttributesResponse.SerializeToString,
            ),
            'GetUserTariff': grpc.unary_unary_rpc_method_handler(
                    servicer.GetUserTariff,
                    request_deserializer=TinkoffPy_dot_grpc_dot_users__pb2.GetUserTariffRequest.FromString,
                    response_serializer=TinkoffPy_dot_grpc_dot_users__pb2.GetUserTariffResponse.SerializeToString,
            ),
            'GetInfo': grpc.unary_unary_rpc_method_handler(
                    servicer.GetInfo,
                    request_deserializer=TinkoffPy_dot_grpc_dot_users__pb2.GetInfoRequest.FromString,
                    response_serializer=TinkoffPy_dot_grpc_dot_users__pb2.GetInfoResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'tinkoff.public.invest.api.contract.v1.UsersService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))
    server.add_registered_method_handlers('tinkoff.public.invest.api.contract.v1.UsersService', rpc_method_handlers)


 # This class is part of an EXPERIMENTAL API.
class UsersService(object):
    """С помощью сервиса можно получить: <br/> 1.
    список счетов пользователя; <br/> 2. маржинальные показатели по счeту.
    """

    @staticmethod
    def GetAccounts(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/tinkoff.public.invest.api.contract.v1.UsersService/GetAccounts',
            TinkoffPy_dot_grpc_dot_users__pb2.GetAccountsRequest.SerializeToString,
            TinkoffPy_dot_grpc_dot_users__pb2.GetAccountsResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def GetMarginAttributes(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/tinkoff.public.invest.api.contract.v1.UsersService/GetMarginAttributes',
            TinkoffPy_dot_grpc_dot_users__pb2.GetMarginAttributesRequest.SerializeToString,
            TinkoffPy_dot_grpc_dot_users__pb2.GetMarginAttributesResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def GetUserTariff(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/tinkoff.public.invest.api.contract.v1.UsersService/GetUserTariff',
            TinkoffPy_dot_grpc_dot_users__pb2.GetUserTariffRequest.SerializeToString,
            TinkoffPy_dot_grpc_dot_users__pb2.GetUserTariffResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def GetInfo(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/tinkoff.public.invest.api.contract.v1.UsersService/GetInfo',
            TinkoffPy_dot_grpc_dot_users__pb2.GetInfoRequest.SerializeToString,
            TinkoffPy_dot_grpc_dot_users__pb2.GetInfoResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)
