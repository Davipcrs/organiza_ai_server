from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class emptyAppointment(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class AppointmentMessage(_message.Message):
    __slots__ = ("id", "title", "desc", "start", "end", "canceled", "color")
    ID_FIELD_NUMBER: _ClassVar[int]
    TITLE_FIELD_NUMBER: _ClassVar[int]
    DESC_FIELD_NUMBER: _ClassVar[int]
    START_FIELD_NUMBER: _ClassVar[int]
    END_FIELD_NUMBER: _ClassVar[int]
    CANCELED_FIELD_NUMBER: _ClassVar[int]
    COLOR_FIELD_NUMBER: _ClassVar[int]
    id: int
    title: str
    desc: str
    start: str
    end: str
    canceled: bool
    color: int
    def __init__(self, id: _Optional[int] = ..., title: _Optional[str] = ..., desc: _Optional[str] = ..., start: _Optional[str] = ..., end: _Optional[str] = ..., canceled: bool = ..., color: _Optional[int] = ...) -> None: ...

class AppointmentResponse(_message.Message):
    __slots__ = ("appointment",)
    APPOINTMENT_FIELD_NUMBER: _ClassVar[int]
    appointment: _containers.RepeatedCompositeFieldContainer[AppointmentMessage]
    def __init__(self, appointment: _Optional[_Iterable[_Union[AppointmentMessage, _Mapping]]] = ...) -> None: ...

class AddAppointmentMessage(_message.Message):
    __slots__ = ("title", "desc", "start", "end", "canceled", "color")
    TITLE_FIELD_NUMBER: _ClassVar[int]
    DESC_FIELD_NUMBER: _ClassVar[int]
    START_FIELD_NUMBER: _ClassVar[int]
    END_FIELD_NUMBER: _ClassVar[int]
    CANCELED_FIELD_NUMBER: _ClassVar[int]
    COLOR_FIELD_NUMBER: _ClassVar[int]
    title: str
    desc: str
    start: str
    end: str
    canceled: bool
    color: int
    def __init__(self, title: _Optional[str] = ..., desc: _Optional[str] = ..., start: _Optional[str] = ..., end: _Optional[str] = ..., canceled: bool = ..., color: _Optional[int] = ...) -> None: ...

class SearchAppointmentRequest(_message.Message):
    __slots__ = ("id",)
    ID_FIELD_NUMBER: _ClassVar[int]
    id: int
    def __init__(self, id: _Optional[int] = ...) -> None: ...
