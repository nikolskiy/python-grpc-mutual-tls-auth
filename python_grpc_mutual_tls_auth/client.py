import grpc
from pathlib import Path
import mutual_tls_auth_pb2 as serializer
import mutual_tls_auth_pb2_grpc as grpc_lib


def run():
    # TODO: move this section into some kind of config
    cert_path = str(Path.joinpath(Path.home(), Path('.ssh/certs/grpc_mutual_tls_auth/server/server.crt')))
    client_path = str(Path.joinpath(Path.home(), Path('.ssh/certs/grpc_mutual_tls_auth/client/client.key')))
    client_cert_path = str(Path.joinpath(Path.home(), Path('.ssh/certs/grpc_mutual_tls_auth/client/client.crt')))
    with open(cert_path, 'rb') as f:
        server_cert = f.read()
    with open(client_path, 'rb') as f:
        client_key = f.read()
    with open(client_cert_path, 'rb') as f:
        client_cert = f.read()

    # create credentials
    credentials = grpc.ssl_channel_credentials(
        root_certificates=server_cert,
        private_key=client_key,
        certificate_chain=client_cert
    )

    with grpc.secure_channel('localhost:50051', credentials) as channel:
        stub = grpc_lib.GatewayStub(channel)
        orders = stub.loan_orders(serializer.Currency(name='LTC'))

    print('result:')
    print(orders)


if __name__ == '__main__':
    run()
