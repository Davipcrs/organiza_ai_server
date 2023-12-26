import grpc
from api.generated import notes_service_pb2_grpc, notes_service_pb2

channel = grpc.insecure_channel(
    'localhost:50051', options=(('grpc.enable_http_proxy', 0),))
stub = notes_service_pb2_grpc.NotesServicesStub(channel)

stmt = stub.addNote(request=notes_service_pb2.AddNoteMessage(
    title="TEste", desc="TEsrewa1dwa", created=None, deadLine=None))

print(stub.getAllNotes(notes_service_pb2.empty()))
# print(stub.getAllNotes(notes_service_pb2.empty())[0])
print(type(stub.getAllNotes(notes_service_pb2.empty())))

aux = stub.getAllNotes(notes_service_pb2.empty())
# aux.note.extend()
"""
for note in aux.note:
    print(note.title)
aux = stub.getNote(notes_service_pb2.SearchNoteRequest(id=1))
print(aux.deadLine)


stub.removeNote(notes_service_pb2.SearchNoteRequest(id=1))
"""
print(stub.editNote(notes_service_pb2.NoteMessage(
    id=2, title="Uhullll", desc="etain", created="sad", deadLine="kk")))
