from concurrent import futures
import grpc
from api.generated import notes_service_pb2_grpc, notes_service_pb2, todo_service_pb2, todo_service_pb2_grpc, appointment_service_pb2, appointment_service_pb2_grpc
from database.insert import insertNote, insertTodo, insertAppointment
from database.select import selectAllNotes, selectAllTodos, selectOneAppointment, selectOneNote, selectOneTodo, selectAllAppointments
from database.delete import deleteNote, deleteTodo, deleteAppointment
from database.update import updateNote, updateTodo, updateAppointment


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
        result = selectOneAppointment(request.id)[0]
        appointment = appointment_service_pb2.AppointmentMessage(
            id=result[0], title=result[1], desc=result[2], start=result[3], end=result[4], color=result[5], canceled=result[6])
        return appointment

    def getAllAppointments(self, request, context):
        allAppointments = selectAllAppointments()

        message = appointment_service_pb2.AppointmentResponse()
        for appointment in allAppointments:
            auxiliar = appointment_service_pb2.AddAppointmentMessage(
                id=appointment[0],
                title=appointment[1],
                desc=appointment[2],
                start=appointment[3],
                end=appointment[4],
                color=appointment[5],
                canceled=appointment[6]

            )
            message.appointment.append(auxiliar)

        return message

    def addAppointment(self, request, context):
        id = insertAppointment(str_title=request.title,
                               str_desc=request.desc,
                               str_end=request.end,
                               str_start=request.start,
                               int_color=request.color,
                               bool_canceled=request.canceled
                               )[0][0]

        return notes_service_pb2.SearchNoteRequest(id=id)

    def editAppointment(self, request, context):
        updateAppointment(int_id=request.id, str_title=request.title,
                          str_desc=request.desc,
                          str_end=request.end,
                          str_start=request.start,
                          int_color=request.color,
                          bool_canceled=request.canceled)
        result = selectOneAppointment(id=request.id)[0]
        appointment = appointment_service_pb2.AppointmentMessage(
            id=result[0], title=result[1], desc=result[2], start=result[3], end=result[4], color=result[5], canceled=result[6])
        return appointment

    def removeAppointment(self, request, context):
        deleteAppointment(request.id)
        return appointment_service_pb2.emptyAppointment()


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    notes_service_pb2_grpc.add_NotesServicesServicer_to_server(
        NotesServicesServicer(), server)
    todo_service_pb2_grpc.add_TodoServicesServicer_to_server(
        TodoServicesServicer(), server)
    appointment_service_pb2_grpc.add_AppointmentServicesServicer_to_server(
        AppointmentServicesServicer(), server)
    server.add_insecure_port("0.0.0.0:50052")
    server.start()
    server.wait_for_termination()
