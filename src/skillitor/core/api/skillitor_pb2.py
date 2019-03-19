# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: skillitor/core/api/skillitor.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='skillitor/core/api/skillitor.proto',
  package='',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n\"skillitor/core/api/skillitor.proto\"?\n\x10SkillAssociation\x12\x0f\n\x07user_id\x18\x01 \x01(\t\x12\x1a\n\x06skills\x18\x02 \x03(\x0b\x32\n.SkillSpec\"+\n\tSkillList\x12\x1e\n\nskill_list\x18\x01 \x03(\x0b\x32\n.SkillSpec\"\x96\x01\n\tSkillSpec\x12\x12\n\nskill_name\x18\x01 \x01(\t\x12*\n\x0bskill_level\x18\x02 \x01(\x0e\x32\x15.SkillSpec.SkillLevel\"I\n\nSkillLevel\x12\r\n\tUNDEFINED\x10\x00\x12\x0c\n\x08\x42\x45GINNER\x10\x01\x12\x10\n\x0cINTERMEDIATE\x10\x02\x12\x0c\n\x08\x41\x44VANCED\x10\x03\"5\n\x0f\x41\x63knowledgement\x12\x0f\n\x07success\x18\x01 \x01(\x08\x12\x11\n\terror_msg\x18\x02 \x01(\t\"\xba\x01\n\x0cRegistration\x12/\n\x0cservice_type\x18\x01 \x01(\x0e\x32\x19.Registration.ServiceType\x12\x14\n\x0cservice_name\x18\x02 \x01(\t\x12\x14\n\x0c\x61\x63\x63\x65ss_token\x18\x03 \x01(\t\x12\x0f\n\x07\x61\x64\x64ress\x18\x04 \x01(\t\"<\n\x0bServiceType\x12\r\n\tUNDEFINED\x10\x00\x12\x0f\n\x0bQUERY_AGENT\x10\x01\x12\r\n\tDATASTORE\x10\x02\x32\xa5\x01\n\x0eSkillitorQuery\x12\x30\n\tSetSkills\x12\x11.SkillAssociation\x1a\x10.Acknowledgement\x12\x32\n\x0bUnsetSkills\x12\x11.SkillAssociation\x1a\x10.Acknowledgement\x12-\n\nFindSkills\x12\n.SkillList\x1a\x11.SkillAssociation0\x01\x32\x41\n\x12SkillitorRegistrar\x12+\n\x08Register\x12\r.Registration\x1a\x10.Acknowledgementb\x06proto3')
)



_SKILLSPEC_SKILLLEVEL = _descriptor.EnumDescriptor(
  name='SkillLevel',
  full_name='SkillSpec.SkillLevel',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='UNDEFINED', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='BEGINNER', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='INTERMEDIATE', index=2, number=2,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ADVANCED', index=3, number=3,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=226,
  serialized_end=299,
)
_sym_db.RegisterEnumDescriptor(_SKILLSPEC_SKILLLEVEL)

_REGISTRATION_SERVICETYPE = _descriptor.EnumDescriptor(
  name='ServiceType',
  full_name='Registration.ServiceType',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='UNDEFINED', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='QUERY_AGENT', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='DATASTORE', index=2, number=2,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=483,
  serialized_end=543,
)
_sym_db.RegisterEnumDescriptor(_REGISTRATION_SERVICETYPE)


_SKILLASSOCIATION = _descriptor.Descriptor(
  name='SkillAssociation',
  full_name='SkillAssociation',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='user_id', full_name='SkillAssociation.user_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='skills', full_name='SkillAssociation.skills', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
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
  serialized_start=38,
  serialized_end=101,
)


_SKILLLIST = _descriptor.Descriptor(
  name='SkillList',
  full_name='SkillList',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='skill_list', full_name='SkillList.skill_list', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
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
  serialized_start=103,
  serialized_end=146,
)


_SKILLSPEC = _descriptor.Descriptor(
  name='SkillSpec',
  full_name='SkillSpec',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='skill_name', full_name='SkillSpec.skill_name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='skill_level', full_name='SkillSpec.skill_level', index=1,
      number=2, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _SKILLSPEC_SKILLLEVEL,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=149,
  serialized_end=299,
)


_ACKNOWLEDGEMENT = _descriptor.Descriptor(
  name='Acknowledgement',
  full_name='Acknowledgement',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='success', full_name='Acknowledgement.success', index=0,
      number=1, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='error_msg', full_name='Acknowledgement.error_msg', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
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
  serialized_start=301,
  serialized_end=354,
)


_REGISTRATION = _descriptor.Descriptor(
  name='Registration',
  full_name='Registration',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='service_type', full_name='Registration.service_type', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='service_name', full_name='Registration.service_name', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='access_token', full_name='Registration.access_token', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='address', full_name='Registration.address', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _REGISTRATION_SERVICETYPE,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=357,
  serialized_end=543,
)

_SKILLASSOCIATION.fields_by_name['skills'].message_type = _SKILLSPEC
_SKILLLIST.fields_by_name['skill_list'].message_type = _SKILLSPEC
_SKILLSPEC.fields_by_name['skill_level'].enum_type = _SKILLSPEC_SKILLLEVEL
_SKILLSPEC_SKILLLEVEL.containing_type = _SKILLSPEC
_REGISTRATION.fields_by_name['service_type'].enum_type = _REGISTRATION_SERVICETYPE
_REGISTRATION_SERVICETYPE.containing_type = _REGISTRATION
DESCRIPTOR.message_types_by_name['SkillAssociation'] = _SKILLASSOCIATION
DESCRIPTOR.message_types_by_name['SkillList'] = _SKILLLIST
DESCRIPTOR.message_types_by_name['SkillSpec'] = _SKILLSPEC
DESCRIPTOR.message_types_by_name['Acknowledgement'] = _ACKNOWLEDGEMENT
DESCRIPTOR.message_types_by_name['Registration'] = _REGISTRATION
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

SkillAssociation = _reflection.GeneratedProtocolMessageType('SkillAssociation', (_message.Message,), dict(
  DESCRIPTOR = _SKILLASSOCIATION,
  __module__ = 'skillitor.core.api.skillitor_pb2'
  # @@protoc_insertion_point(class_scope:SkillAssociation)
  ))
_sym_db.RegisterMessage(SkillAssociation)

SkillList = _reflection.GeneratedProtocolMessageType('SkillList', (_message.Message,), dict(
  DESCRIPTOR = _SKILLLIST,
  __module__ = 'skillitor.core.api.skillitor_pb2'
  # @@protoc_insertion_point(class_scope:SkillList)
  ))
_sym_db.RegisterMessage(SkillList)

SkillSpec = _reflection.GeneratedProtocolMessageType('SkillSpec', (_message.Message,), dict(
  DESCRIPTOR = _SKILLSPEC,
  __module__ = 'skillitor.core.api.skillitor_pb2'
  # @@protoc_insertion_point(class_scope:SkillSpec)
  ))
_sym_db.RegisterMessage(SkillSpec)

Acknowledgement = _reflection.GeneratedProtocolMessageType('Acknowledgement', (_message.Message,), dict(
  DESCRIPTOR = _ACKNOWLEDGEMENT,
  __module__ = 'skillitor.core.api.skillitor_pb2'
  # @@protoc_insertion_point(class_scope:Acknowledgement)
  ))
_sym_db.RegisterMessage(Acknowledgement)

Registration = _reflection.GeneratedProtocolMessageType('Registration', (_message.Message,), dict(
  DESCRIPTOR = _REGISTRATION,
  __module__ = 'skillitor.core.api.skillitor_pb2'
  # @@protoc_insertion_point(class_scope:Registration)
  ))
_sym_db.RegisterMessage(Registration)



_SKILLITORQUERY = _descriptor.ServiceDescriptor(
  name='SkillitorQuery',
  full_name='SkillitorQuery',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  serialized_start=546,
  serialized_end=711,
  methods=[
  _descriptor.MethodDescriptor(
    name='SetSkills',
    full_name='SkillitorQuery.SetSkills',
    index=0,
    containing_service=None,
    input_type=_SKILLASSOCIATION,
    output_type=_ACKNOWLEDGEMENT,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='UnsetSkills',
    full_name='SkillitorQuery.UnsetSkills',
    index=1,
    containing_service=None,
    input_type=_SKILLASSOCIATION,
    output_type=_ACKNOWLEDGEMENT,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='FindSkills',
    full_name='SkillitorQuery.FindSkills',
    index=2,
    containing_service=None,
    input_type=_SKILLLIST,
    output_type=_SKILLASSOCIATION,
    serialized_options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_SKILLITORQUERY)

DESCRIPTOR.services_by_name['SkillitorQuery'] = _SKILLITORQUERY


_SKILLITORREGISTRAR = _descriptor.ServiceDescriptor(
  name='SkillitorRegistrar',
  full_name='SkillitorRegistrar',
  file=DESCRIPTOR,
  index=1,
  serialized_options=None,
  serialized_start=713,
  serialized_end=778,
  methods=[
  _descriptor.MethodDescriptor(
    name='Register',
    full_name='SkillitorRegistrar.Register',
    index=0,
    containing_service=None,
    input_type=_REGISTRATION,
    output_type=_ACKNOWLEDGEMENT,
    serialized_options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_SKILLITORREGISTRAR)

DESCRIPTOR.services_by_name['SkillitorRegistrar'] = _SKILLITORREGISTRAR

# @@protoc_insertion_point(module_scope)
