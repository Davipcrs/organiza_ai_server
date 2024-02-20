from concurrent import futures
import grpc
from api.generated import notes_service_pb2_grpc, notes_service_pb2, todo_service_pb2, todo_service_pb2_grpc, appointment_service_pb2, appointment_service_pb2_grpc
from database.insert import insertNote, insertTodo
from database.select import selectAllNotes, selectAllTodos, selectOneNote, selectOneTodo
from database.delete import deleteNote, deleteTodo
from database.update import updateNote, updateTodo


class TodoServicesServicer(todo_service_pb2_grpc.TodoServicesServicer):
    def getTodo(self, request, context):
        result = selectOneTodo(request.id)[0]
        todo = todo_service_pb2.TodoMessage(id=result[0], title=result[1])
        return todo

    def getAllTodo(self, request, context):
        allTodos = selectAllTodos()

        message = todo_service_pb2.TodoResponse()
        for todo in allTodos:
            auxiliar = todo_service_pb2.TodoMessage(id=todo[0], title=todo[1])
            message.todo.append(auxiliar)
        return message

    def addTodo(self, request, context):
        id = insertTodo(request.title)[0][0]
        return todo_service_pb2.SearchTodoMessage(id=id)

    def editTodo(self, request, context):
        updateTodo(int_id=request.id,
                   str_title=request.title)
        result = selectOneTodo(id=request.id)[0]
        todo = todo_service_pb2.TodoMessage(id=result[0], title=result[1])
        return todo

    def removeTodo(self, request, context):
        deleteTodo(request.id)
        return todo_service_pb2.emptyTodo()


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


class AppointmentServicesServicer(appointment_service_pb2_grpc.AppointmentServicesServicer):
    def getAppointment(self, request, context):
        return super().getAppointment(request, context)

    def getAllAppointments(self, request, context):
        return super().getAllAppointments(request, context)

    def addAppointment(self, request, context):
        return super().addAppointment(request, context)

    def editAppointment(self, request, context):
        return super().editAppointment(request, context)

    def removeAppointment(self, request, context):
        return super().removeAppointment(request, context)

    pass


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    notes_service_pb2_grpc.add_NotesServicesServicer_to_server(
        NotesServicesServicer(), server)
    todo_service_pb2_grpc.add_TodoServicesServicer_to_server(
        TodoServicesServicer(), server)
    server.add_insecure_port("0.0.0.0:50052")
    server.start()
    server.wait_for_termination()
