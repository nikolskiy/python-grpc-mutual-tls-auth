from concurrent import futures
import time
from pathlib import Path

import grpc

import mutual_tls_auth_pb2 as serializer
import mutual_tls_auth_pb2_grpc as grpc_lib


class PoloniexServicer(grpc_lib.GatewayServicer):
    def loan_orders(self, request, context):
        point = serializer.LoanPoint(
            rate='0.010000',
            amount='5.250',
            range_min=2,
            range_max=2
        )
        orders = serializer.Orders(
            offers=[point, point, point],
            demands=[point]
        )
        return orders


def serve():
    # TODO: move this section into some kind of config
    private_key_path = str(Path.joinpath(Path.home(), Path('.ssh/certs/grpc_mutual_tls_auth/server/server.key')))
    cert_path = str(Path.joinpath(Path.home(), Path('.ssh/certs/grpc_mutual_tls_auth/server/server.crt')))
    client_path = str(Path.joinpath(Path.home(), Path('.ssh/certs/grpc_mutual_tls_auth/client/client.crt')))
    with open(private_key_path, 'rb') as f:
        private_key = f.read()
    with open(cert_path, 'rb') as f:
        certificate_chain = f.read()
    with open(client_path, 'rb') as f:
        client_pub_key = f.read()

    # create server credentials
    server_credentials = grpc.ssl_server_credentials(
        [(private_key, certificate_chain)],
        root_certificates=client_pub_key,
        require_client_auth=True
    )

    # this statement needs to be tested:
    # it's okay to have multiple threads because poloniex api call uses thread lock
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    grpc_lib.add_GatewayServicer_to_server(PoloniexServicer(), server)
    server.add_secure_port('[::]:50051', server_credentials)
    server.start()
    try:
        while True:
            time.sleep(60 * 60 * 24)
    except KeyboardInterrupt:
        server.stop(0)


if __name__ == '__main__':
    serve()
