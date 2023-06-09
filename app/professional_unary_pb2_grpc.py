# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import professional_unary_pb2 as professional__unary__pb2


class ProfessionalUnaryStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.GetProContactInfo = channel.unary_unary(
            "/unary.ProfessionalUnary/GetProContactInfo",
            request_serializer=professional__unary__pb2.ProId.SerializeToString,
            response_deserializer=professional__unary__pb2.ContactDetails.FromString,
        )


class ProfessionalUnaryServicer(object):
    """Missing associated documentation comment in .proto file."""

    def GetProContactInfo(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")


def add_ProfessionalUnaryServicer_to_server(servicer, server):
    rpc_method_handlers = {
        "GetProContactInfo": grpc.unary_unary_rpc_method_handler(
            servicer.GetProContactInfo,
            request_deserializer=professional__unary__pb2.ProId.FromString,
            response_serializer=professional__unary__pb2.ContactDetails.SerializeToString,
        ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
        "unary.ProfessionalUnary", rpc_method_handlers
    )
    server.add_generic_rpc_handlers((generic_handler,))


# This class is part of an EXPERIMENTAL API.
class ProfessionalUnary(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def GetProContactInfo(
        request,
        target,
        options=(),
        channel_credentials=None,
        call_credentials=None,
        insecure=False,
        compression=None,
        wait_for_ready=None,
        timeout=None,
        metadata=None,
    ):
        return grpc.experimental.unary_unary(
            request,
            target,
            "/unary.ProfessionalUnary/GetProContactInfo",
            professional__unary__pb2.ProId.SerializeToString,
            professional__unary__pb2.ContactDetails.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
        )
