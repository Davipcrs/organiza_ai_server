from concurrent import futures
import grpc
from api.generated import notes_service_pb2_grpc, notes_service_pb2
from database.insert import insertNote
from database.select import selectAllNotes, selectOneNote
from database.delete import deleteNote
from database.update import updateNote


class NotesServicesServicer(notes_service_pb2_grpc.NotesServicesServicer):
    def getNote(self, request, context):
        result = selectOneNote(request.id)[0]
        note = notes_service_pb2.NoteMessage(
            id=result[0], title=result[1], desc=result[2], created=result[3], deadLine=result[4])
        return note

    def addNote(self, request, context):
        id = insertNote(str_title=request.title,
                        str_desc=request.desc,
                        str_created=request.created,
                        str_deadLine=request.deadLine)[0][0]

        return notes_service_pb2.SearchNoteRequest(id=id)

    def getAllNotes(self, request, context):
        # Need implementation.
        allNotes = selectAllNotes()

        message = notes_service_pb2.NoteResponse()
        for note in allNotes:
            auxiliar = notes_service_pb2.NoteMessage(
                id=note[0],
                title=note[1],
                desc=note[2],
                created=note[3],
                deadLine=note[4]
            )
            message.note.append(auxiliar)

        return message

    def removeNote(self, request, context):
        deleteNote(id=request.id)
        return notes_service_pb2.empty()

    def editNote(self, request, context):
        updateNote(int_id=request.id,
                   str_title=request.title,
                   str_desc=request.desc,
                   str_created=request.created,
                   str_deadLine=request.deadLine)
        result = selectOneNote(request.id)[0]
        note = notes_service_pb2.NoteMessage(
            id=result[0], title=result[1], desc=result[2], created=result[3], deadLine=result[4])
        return note


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    notes_service_pb2_grpc.add_NotesServicesServicer_to_server(
        NotesServicesServicer(), server)
    server.add_insecure_port("0.0.0.0:50051")
    server.start()
    server.wait_for_termination()
