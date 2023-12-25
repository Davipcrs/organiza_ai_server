from database.insert import insertNote
from datetime import datetime
from api.api import serve
from database.select import selectAllNotes, selectOneNote

if __name__ == "__main__":
    serve()
   # selectAllNotes()
    # a = selectOneNote(1)
    # print(a)
    # print(type(a))
    # print(a[0])
