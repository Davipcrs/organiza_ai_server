# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: api/generated/notes_service.proto
# Protobuf Python Version: 4.25.0
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n!api/generated/notes_service.proto\x12\x0borganiza_ai\"\x07\n\x05\x65mpty\"Y\n\x0bNoteMessage\x12\n\n\x02id\x18\x01 \x01(\x03\x12\r\n\x05title\x18\x02 \x01(\t\x12\x0c\n\x04\x64\x65sc\x18\x03 \x01(\t\x12\x0f\n\x07\x63reated\x18\x04 \x01(\t\x12\x10\n\x08\x64\x65\x61\x64Line\x18\x05 \x01(\t\"P\n\x0e\x41\x64\x64NoteMessage\x12\r\n\x05title\x18\x01 \x01(\t\x12\x0c\n\x04\x64\x65sc\x18\x02 \x01(\t\x12\x0f\n\x07\x63reated\x18\x03 \x01(\t\x12\x10\n\x08\x64\x65\x61\x64Line\x18\x04 \x01(\t\"6\n\x0cNoteResponse\x12&\n\x04note\x18\x01 \x03(\x0b\x32\x18.organiza_ai.NoteMessage\"\x1f\n\x11SearchNoteRequest\x12\n\n\x02id\x18\x01 \x01(\x03\x32\xdc\x02\n\rNotesServices\x12\x43\n\x07getNote\x12\x1e.organiza_ai.SearchNoteRequest\x1a\x18.organiza_ai.NoteMessage\x12<\n\x0bgetAllNotes\x12\x12.organiza_ai.empty\x1a\x19.organiza_ai.NoteResponse\x12\x46\n\x07\x61\x64\x64Note\x12\x1b.organiza_ai.AddNoteMessage\x1a\x1e.organiza_ai.SearchNoteRequest\x12@\n\nremoveNote\x12\x1e.organiza_ai.SearchNoteRequest\x1a\x12.organiza_ai.empty\x12>\n\x08\x65\x64itNote\x12\x18.organiza_ai.NoteMessage\x1a\x18.organiza_ai.NoteMessageb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'api.generated.notes_service_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  DESCRIPTOR._options = None
  _globals['_EMPTY']._serialized_start=50
  _globals['_EMPTY']._serialized_end=57
  _globals['_NOTEMESSAGE']._serialized_start=59
  _globals['_NOTEMESSAGE']._serialized_end=148
  _globals['_ADDNOTEMESSAGE']._serialized_start=150
  _globals['_ADDNOTEMESSAGE']._serialized_end=230
  _globals['_NOTERESPONSE']._serialized_start=232
  _globals['_NOTERESPONSE']._serialized_end=286
  _globals['_SEARCHNOTEREQUEST']._serialized_start=288
  _globals['_SEARCHNOTEREQUEST']._serialized_end=319
  _globals['_NOTESSERVICES']._serialized_start=322
  _globals['_NOTESSERVICES']._serialized_end=670
# @@protoc_insertion_point(module_scope)
