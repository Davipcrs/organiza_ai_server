# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: api/generated/appointment_service.proto
# Protobuf Python Version: 4.25.0
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\'api/generated/appointment_service.proto\x12\x0borganiza_ai\"\x12\n\x10\x65mptyAppointment\"z\n\x12\x41ppointmentMessage\x12\n\n\x02id\x18\x01 \x01(\x03\x12\r\n\x05title\x18\x02 \x01(\t\x12\x0c\n\x04\x64\x65sc\x18\x03 \x01(\t\x12\r\n\x05start\x18\x04 \x01(\t\x12\x0b\n\x03\x65nd\x18\x05 \x01(\t\x12\x10\n\x08\x63\x61nceled\x18\x06 \x01(\x08\x12\r\n\x05\x63olor\x18\x07 \x01(\x03\"K\n\x13\x41ppointmentResponse\x12\x34\n\x0b\x61ppointment\x18\x01 \x03(\x0b\x32\x1f.organiza_ai.AppointmentMessage\"q\n\x15\x41\x64\x64\x41ppointmentMessage\x12\r\n\x05title\x18\x01 \x01(\t\x12\x0c\n\x04\x64\x65sc\x18\x02 \x01(\t\x12\r\n\x05start\x18\x03 \x01(\t\x12\x0b\n\x03\x65nd\x18\x04 \x01(\t\x12\x10\n\x08\x63\x61nceled\x18\x05 \x01(\x08\x12\r\n\x05\x63olor\x18\x06 \x01(\x03\"&\n\x18SearchAppointmentRequest\x12\n\n\x02id\x18\x01 \x01(\x03\x32\xd3\x03\n\x13\x41ppointmentServices\x12X\n\x0egetAppointment\x12%.organiza_ai.SearchAppointmentRequest\x1a\x1f.organiza_ai.AppointmentMessage\x12U\n\x12getAllAppointments\x12\x1d.organiza_ai.emptyAppointment\x1a .organiza_ai.AppointmentResponse\x12[\n\x0e\x61\x64\x64\x41ppointment\x12\".organiza_ai.AddAppointmentMessage\x1a%.organiza_ai.SearchAppointmentRequest\x12Y\n\x11removeAppointment\x12%.organiza_ai.SearchAppointmentRequest\x1a\x1d.organiza_ai.emptyAppointment\x12S\n\x0f\x65\x64itAppointment\x12\x1f.organiza_ai.AppointmentMessage\x1a\x1f.organiza_ai.AppointmentMessageb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'api.generated.appointment_service_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  DESCRIPTOR._options = None
  _globals['_EMPTYAPPOINTMENT']._serialized_start=56
  _globals['_EMPTYAPPOINTMENT']._serialized_end=74
  _globals['_APPOINTMENTMESSAGE']._serialized_start=76
  _globals['_APPOINTMENTMESSAGE']._serialized_end=198
  _globals['_APPOINTMENTRESPONSE']._serialized_start=200
  _globals['_APPOINTMENTRESPONSE']._serialized_end=275
  _globals['_ADDAPPOINTMENTMESSAGE']._serialized_start=277
  _globals['_ADDAPPOINTMENTMESSAGE']._serialized_end=390
  _globals['_SEARCHAPPOINTMENTREQUEST']._serialized_start=392
  _globals['_SEARCHAPPOINTMENTREQUEST']._serialized_end=430
  _globals['_APPOINTMENTSERVICES']._serialized_start=433
  _globals['_APPOINTMENTSERVICES']._serialized_end=900
# @@protoc_insertion_point(module_scope)
