from api.api import serve
from database.database import initDatabase

if __name__ == "__main__":
    initDatabase()
    serve()
   # selectAllNotes()
    # a = selectOneNote(1)
    # print(a)
    # print(type(a))
    # print(a[0])
