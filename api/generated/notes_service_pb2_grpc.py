# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from api.generated import notes_service_pb2 as api_dot_generated_dot_notes__service__pb2


class NotesServicesStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.getNote = channel.unary_unary(
                '/organiza_ai.NotesServices/getNote',
                request_serializer=api_dot_generated_dot_notes__service__pb2.SearchNoteRequest.SerializeToString,
                response_deserializer=api_dot_generated_dot_notes__service__pb2.NoteMessage.FromString,
                )
        self.getAllNotes = channel.unary_unary(
                '/organiza_ai.NotesServices/getAllNotes',
                request_serializer=api_dot_generated_dot_notes__service__pb2.empty.SerializeToString,
                response_deserializer=api_dot_generated_dot_notes__service__pb2.NoteResponse.FromString,
                )
        self.addNote = channel.unary_unary(
                '/organiza_ai.NotesServices/addNote',
                request_serializer=api_dot_generated_dot_notes__service__pb2.AddNoteMessage.SerializeToString,
                response_deserializer=api_dot_generated_dot_notes__service__pb2.SearchNoteRequest.FromString,
                )
        self.removeNote = channel.unary_unary(
                '/organiza_ai.NotesServices/removeNote',
                request_serializer=api_dot_generated_dot_notes__service__pb2.SearchNoteRequest.SerializeToString,
                response_deserializer=api_dot_generated_dot_notes__service__pb2.empty.FromString,
                )
        self.editNote = channel.unary_unary(
                '/organiza_ai.NotesServices/editNote',
                request_serializer=api_dot_generated_dot_notes__service__pb2.NoteMessage.SerializeToString,
                response_deserializer=api_dot_generated_dot_notes__service__pb2.NoteMessage.FromString,
                )


class NotesServicesServicer(object):
    """Missing associated documentation comment in .proto file."""

    def getNote(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def getAllNotes(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def addNote(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def removeNote(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def editNote(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_NotesServicesServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'getNote': grpc.unary_unary_rpc_method_handler(
                    servicer.getNote,
                    request_deserializer=api_dot_generated_dot_notes__service__pb2.SearchNoteRequest.FromString,
                    response_serializer=api_dot_generated_dot_notes__service__pb2.NoteMessage.SerializeToString,
            ),
            'getAllNotes': grpc.unary_unary_rpc_method_handler(
                    servicer.getAllNotes,
                    request_deserializer=api_dot_generated_dot_notes__service__pb2.empty.FromString,
                    response_serializer=api_dot_generated_dot_notes__service__pb2.NoteResponse.SerializeToString,
            ),
            'addNote': grpc.unary_unary_rpc_method_handler(
                    servicer.addNote,
                    request_deserializer=api_dot_generated_dot_notes__service__pb2.AddNoteMessage.FromString,
                    response_serializer=api_dot_generated_dot_notes__service__pb2.SearchNoteRequest.SerializeToString,
            ),
            'removeNote': grpc.unary_unary_rpc_method_handler(
                    servicer.removeNote,
                    request_deserializer=api_dot_generated_dot_notes__service__pb2.SearchNoteRequest.FromString,
                    response_serializer=api_dot_generated_dot_notes__service__pb2.empty.SerializeToString,
            ),
            'editNote': grpc.unary_unary_rpc_method_handler(
                    servicer.editNote,
                    request_deserializer=api_dot_generated_dot_notes__service__pb2.NoteMessage.FromString,
                    response_serializer=api_dot_generated_dot_notes__service__pb2.NoteMessage.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'organiza_ai.NotesServices', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class NotesServices(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def getNote(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/organiza_ai.NotesServices/getNote',
            api_dot_generated_dot_notes__service__pb2.SearchNoteRequest.SerializeToString,
            api_dot_generated_dot_notes__service__pb2.NoteMessage.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def getAllNotes(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/organiza_ai.NotesServices/getAllNotes',
            api_dot_generated_dot_notes__service__pb2.empty.SerializeToString,
            api_dot_generated_dot_notes__service__pb2.NoteResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def addNote(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/organiza_ai.NotesServices/addNote',
            api_dot_generated_dot_notes__service__pb2.AddNoteMessage.SerializeToString,
            api_dot_generated_dot_notes__service__pb2.SearchNoteRequest.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def removeNote(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/organiza_ai.NotesServices/removeNote',
            api_dot_generated_dot_notes__service__pb2.SearchNoteRequest.SerializeToString,
            api_dot_generated_dot_notes__service__pb2.empty.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def editNote(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/organiza_ai.NotesServices/editNote',
            api_dot_generated_dot_notes__service__pb2.NoteMessage.SerializeToString,
            api_dot_generated_dot_notes__service__pb2.NoteMessage.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
