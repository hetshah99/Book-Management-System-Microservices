// GENERATED CODE -- DO NOT EDIT!

'use strict';
var grpc = require('grpc');
var support_pb = require('./support_pb.js');

function serialize_systemResponse(arg) {
  if (!(arg instanceof support_pb.systemResponse)) {
    throw new Error('Expected argument of type systemResponse');
  }
  return Buffer.from(arg.serializeBinary());
}

function deserialize_systemResponse(buffer_arg) {
  return support_pb.systemResponse.deserializeBinary(new Uint8Array(buffer_arg));
}

function serialize_userQuery(arg) {
  if (!(arg instanceof support_pb.userQuery)) {
    throw new Error('Expected argument of type userQuery');
  }
  return Buffer.from(arg.serializeBinary());
}

function deserialize_userQuery(buffer_arg) {
  return support_pb.userQuery.deserializeBinary(new Uint8Array(buffer_arg));
}


var customerSupportService = exports.customerSupportService = {
  userSupport: {
    path: '/customerSupport/userSupport',
    requestStream: false,
    responseStream: false,
    requestType: support_pb.userQuery,
    responseType: support_pb.systemResponse,
    requestSerialize: serialize_userQuery,
    requestDeserialize: deserialize_userQuery,
    responseSerialize: serialize_systemResponse,
    responseDeserialize: deserialize_systemResponse,
  },
};

exports.customerSupportClient = grpc.makeGenericClientConstructor(customerSupportService);
