from api.api import serve
from database.database import initDatabase

if __name__ == "__main__":
    print("==================================================================================================")
    print("Server init: Listen on Port 50052")
    print("Wating requests...")
    print("==================================================================================================")
    initDatabase()
    serve()
   # selectAllNotes()
    # a = selectOneNote(1)
    # print(a)
    # print(type(a))
    # print(a[0])
