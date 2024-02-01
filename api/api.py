from concurrent import futures
import grpc
from api.generated import notes_service_pb2_grpc, notes_service_pb2, todo_service_pb2, todo_service_pb2_grpc
from database.insert import insertNote
from database.select import selectAllNotes, selectOneNote
from database.delete import deleteNote
from database.update import updateNote


class TodoServicesServicer(todo_service_pb2_grpc.TodoServicesServicer):
    def getTodo(self, request, context):
        return super().getTodo(request, context)

    def getAllTodo(self, request, context):
        return super().getAllTodo(request, context)

    def addTodo(self, request, context):
        return super().addTodo(request, context)

    def editTodo(self, request, context):
        return super().editTodo(request, context)

    def deleteTodo(self, request, context):
        return super().deleteTodo(request, context)


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
    todo_service_pb2_grpc.add_TodoServicesServicer_to_server(
        TodoServicesServicer(), server)
    server.add_insecure_port("0.0.0.0:50051")
    server.start()
    server.wait_for_termination()
