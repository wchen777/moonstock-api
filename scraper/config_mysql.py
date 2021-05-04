from mysql.connector.constants import ClientFlag

cfg = {
    'user': 'root',
    'password': 'moonstock-api-pass',
    'host': '35.196.61.97',
    'client_flags': [ClientFlag.SSL],
    'ssl_ca': 'ssl/server-ca.pem',
    'ssl_cert': 'ssl/client-cert.pem',
    'ssl_key': 'ssl/client-key.pem',
    'database': 'stock_data'
}