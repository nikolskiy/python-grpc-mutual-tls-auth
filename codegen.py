"""Runs protoc with the gRPC plugin to generate messages and gRPC stubs."""

from grpc_tools import protoc

protoc.main((
    '',
    '-I./protos',
    '--python_out=python_grpc_mutual_tls_auth',
    '--grpc_python_out=python_grpc_mutual_tls_auth',
    './protos/mutual_tls_auth.proto',
))
