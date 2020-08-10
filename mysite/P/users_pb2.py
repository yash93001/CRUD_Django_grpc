# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: users.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='users.proto',
  package='',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x0busers.proto\"X\n\x11\x43reateUserRequest\x12\x10\n\x08username\x18\x01 \x01(\t\x12\r\n\x05\x65mail\x18\x02 \x01(\t\x12\x10\n\x08password\x18\x03 \x01(\t\x12\x10\n\x08phone_no\x18\x04 \x01(\x05\"\"\n\x10\x43reateUserResult\x12\x0e\n\x06status\x18\x01 \x01(\x05\"/\n\x0c\x43heckRequest\x12\r\n\x05\x65mail\x18\x01 \x01(\t\x12\x10\n\x08password\x18\x02 \x01(\t\"\x1e\n\x0b\x43heckResult\x12\x0f\n\x07success\x18\x01 \x01(\x08\"A\n\x11UpdateUserRequest\x12\r\n\x05\x65mail\x18\x01 \x01(\t\x12\r\n\x05uname\x18\x02 \x01(\t\x12\x0e\n\x06uphone\x18\x03 \x01(\x05\"#\n\x10UpdateUserResult\x12\x0f\n\x07success\x18\x01 \x01(\x08\"\"\n\x11\x44\x65leteUserRequest\x12\r\n\x05\x65mail\x18\x01 \x01(\t\"#\n\x10\x44\x65leteUserResult\x12\x0f\n\x07success\x18\x01 \x01(\x08\"\x11\n\x0fListUserRequest\"C\n\x0eListUserResult\x12\x10\n\x08username\x18\x01 \x01(\t\x12\r\n\x05\x65mail\x18\x02 \x01(\t\x12\x10\n\x08phone_no\x18\x04 \x01(\x05\x32\x86\x02\n\x05Users\x12\x33\n\nCreateUser\x12\x12.CreateUserRequest\x1a\x11.CreateUserResult\x12*\n\x0b\x43heck_login\x12\r.CheckRequest\x1a\x0c.CheckResult\x12\x34\n\x0bUpdate_User\x12\x12.UpdateUserRequest\x1a\x11.UpdateUserResult\x12\x34\n\x0b\x44\x65lete_User\x12\x12.DeleteUserRequest\x1a\x11.DeleteUserResult\x12\x30\n\tList_User\x12\x10.ListUserRequest\x1a\x0f.ListUserResult0\x01\x62\x06proto3'
)




_CREATEUSERREQUEST = _descriptor.Descriptor(
  name='CreateUserRequest',
  full_name='CreateUserRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='username', full_name='CreateUserRequest.username', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='email', full_name='CreateUserRequest.email', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='password', full_name='CreateUserRequest.password', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='phone_no', full_name='CreateUserRequest.phone_no', index=3,
      number=4, type=5, cpp_type=1, label=1,
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
  serialized_start=15,
  serialized_end=103,
)


_CREATEUSERRESULT = _descriptor.Descriptor(
  name='CreateUserResult',
  full_name='CreateUserResult',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='status', full_name='CreateUserResult.status', index=0,
      number=1, type=5, cpp_type=1, label=1,
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
  serialized_start=105,
  serialized_end=139,
)


_CHECKREQUEST = _descriptor.Descriptor(
  name='CheckRequest',
  full_name='CheckRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='email', full_name='CheckRequest.email', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='password', full_name='CheckRequest.password', index=1,
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
  serialized_start=141,
  serialized_end=188,
)


_CHECKRESULT = _descriptor.Descriptor(
  name='CheckResult',
  full_name='CheckResult',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='success', full_name='CheckResult.success', index=0,
      number=1, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
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
  serialized_start=190,
  serialized_end=220,
)


_UPDATEUSERREQUEST = _descriptor.Descriptor(
  name='UpdateUserRequest',
  full_name='UpdateUserRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='email', full_name='UpdateUserRequest.email', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='uname', full_name='UpdateUserRequest.uname', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='uphone', full_name='UpdateUserRequest.uphone', index=2,
      number=3, type=5, cpp_type=1, label=1,
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
  serialized_start=222,
  serialized_end=287,
)


_UPDATEUSERRESULT = _descriptor.Descriptor(
  name='UpdateUserResult',
  full_name='UpdateUserResult',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='success', full_name='UpdateUserResult.success', index=0,
      number=1, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
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
  serialized_start=289,
  serialized_end=324,
)


_DELETEUSERREQUEST = _descriptor.Descriptor(
  name='DeleteUserRequest',
  full_name='DeleteUserRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='email', full_name='DeleteUserRequest.email', index=0,
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
  serialized_start=326,
  serialized_end=360,
)


_DELETEUSERRESULT = _descriptor.Descriptor(
  name='DeleteUserResult',
  full_name='DeleteUserResult',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='success', full_name='DeleteUserResult.success', index=0,
      number=1, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
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
  serialized_start=362,
  serialized_end=397,
)


_LISTUSERREQUEST = _descriptor.Descriptor(
  name='ListUserRequest',
  full_name='ListUserRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
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
  serialized_start=399,
  serialized_end=416,
)


_LISTUSERRESULT = _descriptor.Descriptor(
  name='ListUserResult',
  full_name='ListUserResult',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='username', full_name='ListUserResult.username', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='email', full_name='ListUserResult.email', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='phone_no', full_name='ListUserResult.phone_no', index=2,
      number=4, type=5, cpp_type=1, label=1,
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
  serialized_start=418,
  serialized_end=485,
)

DESCRIPTOR.message_types_by_name['CreateUserRequest'] = _CREATEUSERREQUEST
DESCRIPTOR.message_types_by_name['CreateUserResult'] = _CREATEUSERRESULT
DESCRIPTOR.message_types_by_name['CheckRequest'] = _CHECKREQUEST
DESCRIPTOR.message_types_by_name['CheckResult'] = _CHECKRESULT
DESCRIPTOR.message_types_by_name['UpdateUserRequest'] = _UPDATEUSERREQUEST
DESCRIPTOR.message_types_by_name['UpdateUserResult'] = _UPDATEUSERRESULT
DESCRIPTOR.message_types_by_name['DeleteUserRequest'] = _DELETEUSERREQUEST
DESCRIPTOR.message_types_by_name['DeleteUserResult'] = _DELETEUSERRESULT
DESCRIPTOR.message_types_by_name['ListUserRequest'] = _LISTUSERREQUEST
DESCRIPTOR.message_types_by_name['ListUserResult'] = _LISTUSERRESULT
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

CreateUserRequest = _reflection.GeneratedProtocolMessageType('CreateUserRequest', (_message.Message,), {
  'DESCRIPTOR' : _CREATEUSERREQUEST,
  '__module__' : 'users_pb2'
  # @@protoc_insertion_point(class_scope:CreateUserRequest)
  })
_sym_db.RegisterMessage(CreateUserRequest)

CreateUserResult = _reflection.GeneratedProtocolMessageType('CreateUserResult', (_message.Message,), {
  'DESCRIPTOR' : _CREATEUSERRESULT,
  '__module__' : 'users_pb2'
  # @@protoc_insertion_point(class_scope:CreateUserResult)
  })
_sym_db.RegisterMessage(CreateUserResult)

CheckRequest = _reflection.GeneratedProtocolMessageType('CheckRequest', (_message.Message,), {
  'DESCRIPTOR' : _CHECKREQUEST,
  '__module__' : 'users_pb2'
  # @@protoc_insertion_point(class_scope:CheckRequest)
  })
_sym_db.RegisterMessage(CheckRequest)

CheckResult = _reflection.GeneratedProtocolMessageType('CheckResult', (_message.Message,), {
  'DESCRIPTOR' : _CHECKRESULT,
  '__module__' : 'users_pb2'
  # @@protoc_insertion_point(class_scope:CheckResult)
  })
_sym_db.RegisterMessage(CheckResult)

UpdateUserRequest = _reflection.GeneratedProtocolMessageType('UpdateUserRequest', (_message.Message,), {
  'DESCRIPTOR' : _UPDATEUSERREQUEST,
  '__module__' : 'users_pb2'
  # @@protoc_insertion_point(class_scope:UpdateUserRequest)
  })
_sym_db.RegisterMessage(UpdateUserRequest)

UpdateUserResult = _reflection.GeneratedProtocolMessageType('UpdateUserResult', (_message.Message,), {
  'DESCRIPTOR' : _UPDATEUSERRESULT,
  '__module__' : 'users_pb2'
  # @@protoc_insertion_point(class_scope:UpdateUserResult)
  })
_sym_db.RegisterMessage(UpdateUserResult)

DeleteUserRequest = _reflection.GeneratedProtocolMessageType('DeleteUserRequest', (_message.Message,), {
  'DESCRIPTOR' : _DELETEUSERREQUEST,
  '__module__' : 'users_pb2'
  # @@protoc_insertion_point(class_scope:DeleteUserRequest)
  })
_sym_db.RegisterMessage(DeleteUserRequest)

DeleteUserResult = _reflection.GeneratedProtocolMessageType('DeleteUserResult', (_message.Message,), {
  'DESCRIPTOR' : _DELETEUSERRESULT,
  '__module__' : 'users_pb2'
  # @@protoc_insertion_point(class_scope:DeleteUserResult)
  })
_sym_db.RegisterMessage(DeleteUserResult)

ListUserRequest = _reflection.GeneratedProtocolMessageType('ListUserRequest', (_message.Message,), {
  'DESCRIPTOR' : _LISTUSERREQUEST,
  '__module__' : 'users_pb2'
  # @@protoc_insertion_point(class_scope:ListUserRequest)
  })
_sym_db.RegisterMessage(ListUserRequest)

ListUserResult = _reflection.GeneratedProtocolMessageType('ListUserResult', (_message.Message,), {
  'DESCRIPTOR' : _LISTUSERRESULT,
  '__module__' : 'users_pb2'
  # @@protoc_insertion_point(class_scope:ListUserResult)
  })
_sym_db.RegisterMessage(ListUserResult)



_USERS = _descriptor.ServiceDescriptor(
  name='Users',
  full_name='Users',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=488,
  serialized_end=750,
  methods=[
  _descriptor.MethodDescriptor(
    name='CreateUser',
    full_name='Users.CreateUser',
    index=0,
    containing_service=None,
    input_type=_CREATEUSERREQUEST,
    output_type=_CREATEUSERRESULT,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='Check_login',
    full_name='Users.Check_login',
    index=1,
    containing_service=None,
    input_type=_CHECKREQUEST,
    output_type=_CHECKRESULT,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='Update_User',
    full_name='Users.Update_User',
    index=2,
    containing_service=None,
    input_type=_UPDATEUSERREQUEST,
    output_type=_UPDATEUSERRESULT,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='Delete_User',
    full_name='Users.Delete_User',
    index=3,
    containing_service=None,
    input_type=_DELETEUSERREQUEST,
    output_type=_DELETEUSERRESULT,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='List_User',
    full_name='Users.List_User',
    index=4,
    containing_service=None,
    input_type=_LISTUSERREQUEST,
    output_type=_LISTUSERRESULT,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_USERS)

DESCRIPTOR.services_by_name['Users'] = _USERS

# @@protoc_insertion_point(module_scope)
