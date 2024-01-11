from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class emptyTodo(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class NoteMessage(_message.Message):
    __slots__ = ("id", "title", "desc", "created", "deadLine")
    ID_FIELD_NUMBER: _ClassVar[int]
    TITLE_FIELD_NUMBER: _ClassVar[int]
    DESC_FIELD_NUMBER: _ClassVar[int]
    CREATED_FIELD_NUMBER: _ClassVar[int]
    DEADLINE_FIELD_NUMBER: _ClassVar[int]
    id: int
    title: str
    desc: str
    created: str
    deadLine: str
    def __init__(self, id: _Optional[int] = ..., title: _Optional[str] = ..., desc: _Optional[str] = ..., created: _Optional[str] = ..., deadLine: _Optional[str] = ...) -> None: ...

class AddNoteMessage(_message.Message):
    __slots__ = ("title", "desc", "created", "deadLine")
    TITLE_FIELD_NUMBER: _ClassVar[int]
    DESC_FIELD_NUMBER: _ClassVar[int]
    CREATED_FIELD_NUMBER: _ClassVar[int]
    DEADLINE_FIELD_NUMBER: _ClassVar[int]
    title: str
    desc: str
    created: str
    deadLine: str
    def __init__(self, title: _Optional[str] = ..., desc: _Optional[str] = ..., created: _Optional[str] = ..., deadLine: _Optional[str] = ...) -> None: ...

class NoteResponse(_message.Message):
    __slots__ = ("note",)
    NOTE_FIELD_NUMBER: _ClassVar[int]
    note: _containers.RepeatedCompositeFieldContainer[NoteMessage]
    def __init__(self, note: _Optional[_Iterable[_Union[NoteMessage, _Mapping]]] = ...) -> None: ...

class SearchNoteRequest(_message.Message):
    __slots__ = ("id",)
    ID_FIELD_NUMBER: _ClassVar[int]
    id: int
    def __init__(self, id: _Optional[int] = ...) -> None: ...
