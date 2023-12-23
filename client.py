import grpc
from api.generated import notes_service_pb2_grpc, notes_service_pb2

channel = grpc.insecure_channel('localhost:50051')
stub = notes_service_pb2_grpc.NotesServicesStub(channel)

stmt = stub.addNote(notes_service_pb2.AddNoteMessage(
    title="TEste", desc="TEsrewa1dwa", created=None, deadLine=None))

print(stmt)
