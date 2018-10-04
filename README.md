# Python gRPC mutual tls authentication
This is a simple python gRPC project with mutual server-client tls authentication.

## Goal
A gRPC server that would 
1) accept only trusted clients connections
2) establish encrypted communication channel

## Doc resources and examples
Official [gRPC python documentation](https://grpc.io/docs/guides/auth.html#python) has a simple example
how to establish tls encryption between client and a server. It doesn't talk about how to generate those files or
how to establish mutual authentication. In this setup any client can theoretically connect to the server. gRPC
library complains if you don't include server certificate but the server doesn't do any kind of authentication by
default.

[python gRPC reference](https://grpc.io/grpc/python/_modules/grpc.html)

[Secure gRPC with TLS/SSL](https://bbengfort.github.io/programmer/2017/03/03/secure-grpc.html) - useful article but it
still doesn't clarify confusion about tls certs.

[Using SSL with gRPC in Python](https://www.sandtable.com/using-ssl-with-grpc-in-python/comment-page-1/) -
doesn't talk about mutual tls authentication but has interesting sections on metadata and compression.

[TLS authentication in Python gRPC](https://github.com/joekottke/python-grpc-ssl/blob/master/resources/TLS-SSL%20authentication%20in%20Python%20gRPC.md) -
Very useful explanation and the [repo itself](https://github.com/joekottke/python-grpc-ssl) is an awesome example
of setting up gRPC [server](https://github.com/joekottke/python-grpc-ssl/blob/master/src/server.py) and [client](https://github.com/joekottke/python-grpc-ssl/blob/master/src/client.py).
I wonder if it's possible to generate all those keys using only `openssl` though.

[Useful openssl stackoverflow post](https://stackoverflow.com/questions/21297139/how-do-you-sign-a-certificate-signing-request-with-your-certification-authority)
that talks about setting up CA and signing certificates.

## Scope
The scope of the example should include: 
1) A very simple gRPC function
2) Server and client setup with mutual tls authentication
3) Management commands (probably using invoke) to create/manage all necessary tls files and run the server
