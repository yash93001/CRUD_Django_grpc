# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from P import users_pb2 as users__pb2


class UsersStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.CreateUser = channel.unary_unary(
                '/Users/CreateUser',
                request_serializer=users__pb2.CreateUserRequest.SerializeToString,
                response_deserializer=users__pb2.CreateUserResult.FromString,
                )
        self.Check_login = channel.unary_unary(
                '/Users/Check_login',
                request_serializer=users__pb2.CheckRequest.SerializeToString,
                response_deserializer=users__pb2.CheckResult.FromString,
                )
        self.Update_User = channel.unary_unary(
                '/Users/Update_User',
                request_serializer=users__pb2.UpdateUserRequest.SerializeToString,
                response_deserializer=users__pb2.UpdateUserResult.FromString,
                )
        self.Delete_User = channel.unary_unary(
                '/Users/Delete_User',
                request_serializer=users__pb2.DeleteUserRequest.SerializeToString,
                response_deserializer=users__pb2.DeleteUserResult.FromString,
                )
        self.List_User = channel.unary_stream(
                '/Users/List_User',
                request_serializer=users__pb2.ListUserRequest.SerializeToString,
                response_deserializer=users__pb2.ListUserResult.FromString,
                )


class UsersServicer(object):
    """Missing associated documentation comment in .proto file."""

    def CreateUser(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Check_login(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Update_User(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Delete_User(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def List_User(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_UsersServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'CreateUser': grpc.unary_unary_rpc_method_handler(
                    servicer.CreateUser,
                    request_deserializer=users__pb2.CreateUserRequest.FromString,
                    response_serializer=users__pb2.CreateUserResult.SerializeToString,
            ),
            'Check_login': grpc.unary_unary_rpc_method_handler(
                    servicer.Check_login,
                    request_deserializer=users__pb2.CheckRequest.FromString,
                    response_serializer=users__pb2.CheckResult.SerializeToString,
            ),
            'Update_User': grpc.unary_unary_rpc_method_handler(
                    servicer.Update_User,
                    request_deserializer=users__pb2.UpdateUserRequest.FromString,
                    response_serializer=users__pb2.UpdateUserResult.SerializeToString,
            ),
            'Delete_User': grpc.unary_unary_rpc_method_handler(
                    servicer.Delete_User,
                    request_deserializer=users__pb2.DeleteUserRequest.FromString,
                    response_serializer=users__pb2.DeleteUserResult.SerializeToString,
            ),
            'List_User': grpc.unary_stream_rpc_method_handler(
                    servicer.List_User,
                    request_deserializer=users__pb2.ListUserRequest.FromString,
                    response_serializer=users__pb2.ListUserResult.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'Users', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class Users(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def CreateUser(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/Users/CreateUser',
            users__pb2.CreateUserRequest.SerializeToString,
            users__pb2.CreateUserResult.FromString,
            options, channel_credentials,
            call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Check_login(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/Users/Check_login',
            users__pb2.CheckRequest.SerializeToString,
            users__pb2.CheckResult.FromString,
            options, channel_credentials,
            call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Update_User(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/Users/Update_User',
            users__pb2.UpdateUserRequest.SerializeToString,
            users__pb2.UpdateUserResult.FromString,
            options, channel_credentials,
            call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Delete_User(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/Users/Delete_User',
            users__pb2.DeleteUserRequest.SerializeToString,
            users__pb2.DeleteUserResult.FromString,
            options, channel_credentials,
            call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def List_User(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_stream(request, target, '/Users/List_User',
            users__pb2.ListUserRequest.SerializeToString,
            users__pb2.ListUserResult.FromString,
            options, channel_credentials,
            call_credentials, compression, wait_for_ready, timeout, metadata)
