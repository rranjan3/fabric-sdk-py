# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: hfc/protos/peer/chaincode_event.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='hfc/protos/peer/chaincode_event.proto',
  package='protos',
  syntax='proto3',
  serialized_options=b'\n\"org.hyperledger.fabric.protos.peerB\025ChaincodeEventPackageZ,github.com/hyperledger/fabric-protos-go/peer',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n%hfc/protos/peer/chaincode_event.proto\x12\x06protos\"Z\n\x0e\x43haincodeEvent\x12\x14\n\x0c\x63haincode_id\x18\x01 \x01(\t\x12\r\n\x05tx_id\x18\x02 \x01(\t\x12\x12\n\nevent_name\x18\x03 \x01(\t\x12\x0f\n\x07payload\x18\x04 \x01(\x0c\x42i\n\"org.hyperledger.fabric.protos.peerB\x15\x43haincodeEventPackageZ,github.com/hyperledger/fabric-protos-go/peerb\x06proto3'
)




_CHAINCODEEVENT = _descriptor.Descriptor(
  name='ChaincodeEvent',
  full_name='protos.ChaincodeEvent',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='chaincode_id', full_name='protos.ChaincodeEvent.chaincode_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='tx_id', full_name='protos.ChaincodeEvent.tx_id', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='event_name', full_name='protos.ChaincodeEvent.event_name', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='payload', full_name='protos.ChaincodeEvent.payload', index=3,
      number=4, type=12, cpp_type=9, label=1,
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
  serialized_start=49,
  serialized_end=139,
)

DESCRIPTOR.message_types_by_name['ChaincodeEvent'] = _CHAINCODEEVENT
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

ChaincodeEvent = _reflection.GeneratedProtocolMessageType('ChaincodeEvent', (_message.Message,), {
  'DESCRIPTOR' : _CHAINCODEEVENT,
  '__module__' : 'hfc.protos.peer.chaincode_event_pb2'
  # @@protoc_insertion_point(class_scope:protos.ChaincodeEvent)
  })
_sym_db.RegisterMessage(ChaincodeEvent)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
