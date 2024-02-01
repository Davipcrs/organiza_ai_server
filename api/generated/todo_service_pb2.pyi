from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class empty(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class TodoMessage(_message.Message):
    __slots__ = ("id", "title")
    ID_FIELD_NUMBER: _ClassVar[int]
    TITLE_FIELD_NUMBER: _ClassVar[int]
    id: int
    title: str
    def __init__(self, id: _Optional[int] = ..., title: _Optional[str] = ...) -> None: ...

class TodoResponse(_message.Message):
    __slots__ = ("todo",)
    TODO_FIELD_NUMBER: _ClassVar[int]
    todo: _containers.RepeatedCompositeFieldContainer[TodoMessage]
    def __init__(self, todo: _Optional[_Iterable[_Union[TodoMessage, _Mapping]]] = ...) -> None: ...

class AddTodoMessage(_message.Message):
    __slots__ = ("title",)
    TITLE_FIELD_NUMBER: _ClassVar[int]
    title: str
    def __init__(self, title: _Optional[str] = ...) -> None: ...

class SearchTodoMessage(_message.Message):
    __slots__ = ("id",)
    ID_FIELD_NUMBER: _ClassVar[int]
    id: int
    def __init__(self, id: _Optional[int] = ...) -> None: ...
