from concurrent import futures
import grpc
from api.generated import notes_service_pb2_grpc
from database.insert import insertNote


class NotesServicesServicer(notes_service_pb2_grpc.NotesServicesServicer):
    def getNote(self, request, context):
        return super().getNote(request, context)

    def addNote(self, request, context):
        insertNote(str_title=request.title,
                   str_desc=request.desc,
                   str_created=request.created,
                   str_deadLine=request.deadLine)

    def getAllNotes(self, request, context):
        return super().getAllNotes(request, context)

    def removeNote(self, request, context):
        return super().removeNote(request, context)

    def editNote(self, request, context):
        return super().editNote(request, context)


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    notes_service_pb2_grpc.add_NotesServicesServicer_to_server(
        NotesServicesServicer(), server)
    server.add_insecure_port("0.0.0.0:50051")
    server.start()
    server.wait_for_termination()
