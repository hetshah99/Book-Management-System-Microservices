# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: support.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='support.proto',
  package='',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\rsupport.proto\")\n\tuserQuery\x12\r\n\x05\x65mail\x18\x01 \x01(\t\x12\r\n\x05query\x18\x02 \x01(\t\"\"\n\x0esystemResponse\x12\x10\n\x08response\x18\x01 \x01(\t2=\n\x0f\x63ustomerSupport\x12*\n\x0buserSupport\x12\n.userQuery\x1a\x0f.systemResponseb\x06proto3'
)




_USERQUERY = _descriptor.Descriptor(
  name='userQuery',
  full_name='userQuery',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='email', full_name='userQuery.email', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='query', full_name='userQuery.query', index=1,
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
  serialized_start=17,
  serialized_end=58,
)


_SYSTEMRESPONSE = _descriptor.Descriptor(
  name='systemResponse',
  full_name='systemResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='response', full_name='systemResponse.response', index=0,
      number=1, type=9, cpp_type=9, label=1,
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
  serialized_start=60,
  serialized_end=94,
)

DESCRIPTOR.message_types_by_name['userQuery'] = _USERQUERY
DESCRIPTOR.message_types_by_name['systemResponse'] = _SYSTEMRESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

userQuery = _reflection.GeneratedProtocolMessageType('userQuery', (_message.Message,), {
  'DESCRIPTOR' : _USERQUERY,
  '__module__' : 'support_pb2'
  # @@protoc_insertion_point(class_scope:userQuery)
  })
_sym_db.RegisterMessage(userQuery)

systemResponse = _reflection.GeneratedProtocolMessageType('systemResponse', (_message.Message,), {
  'DESCRIPTOR' : _SYSTEMRESPONSE,
  '__module__' : 'support_pb2'
  # @@protoc_insertion_point(class_scope:systemResponse)
  })
_sym_db.RegisterMessage(systemResponse)



_CUSTOMERSUPPORT = _descriptor.ServiceDescriptor(
  name='customerSupport',
  full_name='customerSupport',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=96,
  serialized_end=157,
  methods=[
  _descriptor.MethodDescriptor(
    name='userSupport',
    full_name='customerSupport.userSupport',
    index=0,
    containing_service=None,
    input_type=_USERQUERY,
    output_type=_SYSTEMRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_CUSTOMERSUPPORT)

DESCRIPTOR.services_by_name['customerSupport'] = _CUSTOMERSUPPORT

# @@protoc_insertion_point(module_scope)
