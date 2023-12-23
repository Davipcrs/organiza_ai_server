from api.generated import notes_service_pb2_grpc


class NotesServicesServicer(notes_service_pb2_grpc.NotesServicesServicer):
    def getNote(self, request, context):
        return super().getNote(request, context)

    def addNote(self, request, context):
        return super().addNote(request, context)

    def getAllNotes(self, request, context):
        return super().getAllNotes(request, context)

    def removeNote(self, request, context):
        return super().removeNote(request, context)

    def editNote(self, request, context):
        return super().editNote(request, context)
