import time
import grpc
from concurrent import futures
import mutual_tls_auth_pb2 as serializer
import mutual_tls_auth_pb2_grpc as grpc_lib
from utils import secrets, config


class GatewayServicer(grpc_lib.GatewayServicer):
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


def serve(cfg):
    # Client will verify the server using server cert and the server
    # will verify the client using client cert.
    server_credentials = grpc.ssl_server_credentials(
        [(secrets.load(cfg['credentials']['server']['key']),
          secrets.load(cfg['credentials']['server']['cert']))],
        root_certificates=secrets.load(cfg['credentials']['client']['cert']),
        require_client_auth=True
    )

    # this statement needs to be tested:
    # it's okay to have multiple threads because poloniex api call uses thread lock
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    grpc_lib.add_GatewayServicer_to_server(GatewayServicer(), server)
    server.add_secure_port('[::]:50051', server_credentials)
    server.start()
    try:
        while True:
            time.sleep(60 * 60 * 24)
    except KeyboardInterrupt:
        server.stop(0)


if __name__ == '__main__':
    serve(config.invoke_config())
