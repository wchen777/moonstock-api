from mysql.connector.constants import ClientFlag
import os

cfg = {
    'user': 'root',
    'password': 'moonstock-api-pass',
    'host': '35.196.83.194',
    'client_flags': [ClientFlag.SSL],
    'ssl_ca': os.path.join('ssl', 'server-ca.pem'),
    'ssl_cert': os.path.join('ssl', 'client-cert.pem'),
    'ssl_key': os.path.join('ssl', 'client-key.pem'),
    'database': 'stock_data'
}