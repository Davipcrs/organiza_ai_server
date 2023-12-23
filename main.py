from database.insert import insertNote
from datetime import datetime

if __name__ == "__main__":
    insertNote(str_title="Test", str_desc="dewst",
               str_created=str(datetime.now()))
