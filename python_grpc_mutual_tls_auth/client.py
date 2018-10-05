import grpc
import mutual_tls_auth_pb2 as serializer
import mutual_tls_auth_pb2_grpc as grpc_lib
from utils import secrets, config


def run(cfg):
    # Verify we are talking to the right server and provide our own
    # certificate for verification
    credentials = grpc.ssl_channel_credentials(
        root_certificates=secrets.load(cfg['credentials']['server']['cert']),
        private_key=secrets.load(cfg['credentials']['client']['key']),
        certificate_chain=secrets.load(cfg['credentials']['client']['cert'])
    )

    with grpc.secure_channel('localhost:50051', credentials) as channel:
        stub = grpc_lib.GatewayStub(channel)
        orders = stub.loan_orders(serializer.Currency(name='LTC'))

    print('result:')
    print(orders)


if __name__ == '__main__':
    run(config.invoke_config())
