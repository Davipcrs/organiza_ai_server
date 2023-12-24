from database.insert import insertNote
from datetime import datetime
from api.api import serve
from database.select import selectAllNotes

if __name__ == "__main__":
    # serve()
    selectAllNotes()
