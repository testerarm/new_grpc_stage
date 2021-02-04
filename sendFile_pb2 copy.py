# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: sendFile.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='sendFile.proto',
  package='uploadFile',
  syntax='proto3',
  serialized_options=b'\n\007ex.grpc\242\002\003HSW',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x0esendFile.proto\x12\nuploadFile\"P\n\x04Task\x12\x10\n\x08taskName\x18\x01 \x01(\t\x12\x0e\n\x06nodeId\x18\x02 \x01(\t\x12&\n\x0c\x66\x65\x61ture_pair\x18\x03 \x01(\x0b\x32\x10.uploadFile.Pair\"$\n\x04Pair\x12\r\n\x05pair1\x18\x01 \x01(\t\x12\r\n\x05pair2\x18\x02 \x01(\t\"0\n\x0cTaskResponse\x12\x10\n\x08taskName\x18\x01 \x01(\t\x12\x0e\n\x06nodeId\x18\x02 \x01(\t\"-\n\x08NewChunk\x12\x10\n\x08\x66ilename\x18\x01 \x01(\t\x12\x0f\n\x07\x63ontent\x18\x02 \x01(\x0c\"\x18\n\x05\x43hunk\x12\x0f\n\x07\x63ontent\x18\x01 \x01(\x0c\"K\n\x0cUploadStatus\x12\x0f\n\x07message\x18\x01 \x01(\t\x12*\n\x04\x63ode\x18\x02 \x01(\x0e\x32\x1c.uploadFile.UploadStatusCode*3\n\x10UploadStatusCode\x12\x0b\n\x07Unknown\x10\x00\x12\x06\n\x02Ok\x10\x01\x12\n\n\x06\x46\x61iled\x10\x02\x32\xbc\x01\n\x0b\x46ileService\x12\x39\n\x06upload\x12\x11.uploadFile.Chunk\x1a\x18.uploadFile.UploadStatus\"\x00(\x01\x12\x36\n\x08sendTask\x12\x10.uploadFile.Task\x1a\x14.uploadFile.NewChunk\"\x00\x30\x01\x12:\n\tbidupload\x12\x11.uploadFile.Chunk\x1a\x14.uploadFile.NewChunk\"\x00(\x01\x30\x01\x42\x0f\n\x07\x65x.grpc\xa2\x02\x03HSWb\x06proto3'
)

_UPLOADSTATUSCODE = _descriptor.EnumDescriptor(
  name='UploadStatusCode',
  full_name='uploadFile.UploadStatusCode',
  filename=None,
  file=DESCRIPTOR,
  create_key=_descriptor._internal_create_key,
  values=[
    _descriptor.EnumValueDescriptor(
      name='Unknown', index=0, number=0,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='Ok', index=1, number=1,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='Failed', index=2, number=2,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=350,
  serialized_end=401,
)
_sym_db.RegisterEnumDescriptor(_UPLOADSTATUSCODE)

UploadStatusCode = enum_type_wrapper.EnumTypeWrapper(_UPLOADSTATUSCODE)
Unknown = 0
Ok = 1
Failed = 2



_TASK = _descriptor.Descriptor(
  name='Task',
  full_name='uploadFile.Task',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='taskName', full_name='uploadFile.Task.taskName', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='nodeId', full_name='uploadFile.Task.nodeId', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='feature_pair', full_name='uploadFile.Task.feature_pair', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=30,
  serialized_end=110,
)


_PAIR = _descriptor.Descriptor(
  name='Pair',
  full_name='uploadFile.Pair',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='pair1', full_name='uploadFile.Pair.pair1', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='pair2', full_name='uploadFile.Pair.pair2', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=112,
  serialized_end=148,
)


_TASKRESPONSE = _descriptor.Descriptor(
  name='TaskResponse',
  full_name='uploadFile.TaskResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='taskName', full_name='uploadFile.TaskResponse.taskName', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='nodeId', full_name='uploadFile.TaskResponse.nodeId', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=150,
  serialized_end=198,
)


_NEWCHUNK = _descriptor.Descriptor(
  name='NewChunk',
  full_name='uploadFile.NewChunk',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='filename', full_name='uploadFile.NewChunk.filename', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='content', full_name='uploadFile.NewChunk.content', index=1,
      number=2, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=b"",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=200,
  serialized_end=245,
)


_CHUNK = _descriptor.Descriptor(
  name='Chunk',
  full_name='uploadFile.Chunk',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='content', full_name='uploadFile.Chunk.content', index=0,
      number=1, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=b"",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=247,
  serialized_end=271,
)


_UPLOADSTATUS = _descriptor.Descriptor(
  name='UploadStatus',
  full_name='uploadFile.UploadStatus',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='message', full_name='uploadFile.UploadStatus.message', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='code', full_name='uploadFile.UploadStatus.code', index=1,
      number=2, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=273,
  serialized_end=348,
)

_TASK.fields_by_name['feature_pair'].message_type = _PAIR
_UPLOADSTATUS.fields_by_name['code'].enum_type = _UPLOADSTATUSCODE
DESCRIPTOR.message_types_by_name['Task'] = _TASK
DESCRIPTOR.message_types_by_name['Pair'] = _PAIR
DESCRIPTOR.message_types_by_name['TaskResponse'] = _TASKRESPONSE
DESCRIPTOR.message_types_by_name['NewChunk'] = _NEWCHUNK
DESCRIPTOR.message_types_by_name['Chunk'] = _CHUNK
DESCRIPTOR.message_types_by_name['UploadStatus'] = _UPLOADSTATUS
DESCRIPTOR.enum_types_by_name['UploadStatusCode'] = _UPLOADSTATUSCODE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Task = _reflection.GeneratedProtocolMessageType('Task', (_message.Message,), {
  'DESCRIPTOR' : _TASK,
  '__module__' : 'sendFile_pb2'
  # @@protoc_insertion_point(class_scope:uploadFile.Task)
  })
_sym_db.RegisterMessage(Task)

Pair = _reflection.GeneratedProtocolMessageType('Pair', (_message.Message,), {
  'DESCRIPTOR' : _PAIR,
  '__module__' : 'sendFile_pb2'
  # @@protoc_insertion_point(class_scope:uploadFile.Pair)
  })
_sym_db.RegisterMessage(Pair)

TaskResponse = _reflection.GeneratedProtocolMessageType('TaskResponse', (_message.Message,), {
  'DESCRIPTOR' : _TASKRESPONSE,
  '__module__' : 'sendFile_pb2'
  # @@protoc_insertion_point(class_scope:uploadFile.TaskResponse)
  })
_sym_db.RegisterMessage(TaskResponse)

NewChunk = _reflection.GeneratedProtocolMessageType('NewChunk', (_message.Message,), {
  'DESCRIPTOR' : _NEWCHUNK,
  '__module__' : 'sendFile_pb2'
  # @@protoc_insertion_point(class_scope:uploadFile.NewChunk)
  })
_sym_db.RegisterMessage(NewChunk)

Chunk = _reflection.GeneratedProtocolMessageType('Chunk', (_message.Message,), {
  'DESCRIPTOR' : _CHUNK,
  '__module__' : 'sendFile_pb2'
  # @@protoc_insertion_point(class_scope:uploadFile.Chunk)
  })
_sym_db.RegisterMessage(Chunk)

UploadStatus = _reflection.GeneratedProtocolMessageType('UploadStatus', (_message.Message,), {
  'DESCRIPTOR' : _UPLOADSTATUS,
  '__module__' : 'sendFile_pb2'
  # @@protoc_insertion_point(class_scope:uploadFile.UploadStatus)
  })
_sym_db.RegisterMessage(UploadStatus)


DESCRIPTOR._options = None

_FILESERVICE = _descriptor.ServiceDescriptor(
  name='FileService',
  full_name='uploadFile.FileService',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=404,
  serialized_end=592,
  methods=[
  _descriptor.MethodDescriptor(
    name='upload',
    full_name='uploadFile.FileService.upload',
    index=0,
    containing_service=None,
    input_type=_CHUNK,
    output_type=_UPLOADSTATUS,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='sendTask',
    full_name='uploadFile.FileService.sendTask',
    index=1,
    containing_service=None,
    input_type=_TASK,
    output_type=_NEWCHUNK,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='bidupload',
    full_name='uploadFile.FileService.bidupload',
    index=2,
    containing_service=None,
    input_type=_CHUNK,
    output_type=_NEWCHUNK,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_FILESERVICE)

DESCRIPTOR.services_by_name['FileService'] = _FILESERVICE

# @@protoc_insertion_point(module_scope)
