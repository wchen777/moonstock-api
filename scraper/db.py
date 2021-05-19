def create_stock_table(cursor):
    cursor.execute("CREATE TABLE IF NOT EXISTS stocks ("
                   "company_name VARCHAR(255),"
                   "ticker VARCHAR(255),"
                   "price FLOAT(7,2),"
                   "EPS_forward FLOAT(6,2),"
                   "EPS_trailing FLOAT(6,2),"
                   "PE_forward FLOAT(6,2),"
                   "PE_trailing FLOAT(6,2),"
                   "`change` FLOAT(6,2),"
                   "change_percent VARCHAR(255),"
                   "dividend FLOAT(6,2),"
                   "dividend_yield VARCHAR(255),"
                   "market_cap VARCHAR(255),"
                   "prev_close FLOAT(7,2),"
                   "volume INT,"
                   "weight_sp500 FLOAT(8,6),"
                   "year_high FLOAT(6,2),"
                   "year_low FLOAT(6,2),"
                   "date_time DATETIME )")


def tuple_from_dict(stonk):
    return (
        stonk['company_name'],
        stonk['ticker'],
        stonk['price'],
        stonk['EPS_forward'],
        stonk['EPS_trailing'],
        stonk['PE_forward'],
        stonk['PE_trailing'],
        stonk['change'],
        stonk['change_percent'],
        stonk['dividend'],
        stonk['dividend_yield'],
        stonk['market_cap'],
        stonk['prev_close'],
        stonk['volume'],
        stonk['weight_sp500'],
        stonk['year_high'],
        stonk['year_low'],
        stonk['date_time']
    )


def insert_quote(cursor, stonk):
    query = ("INSERT INTO stocks (company_name, ticker, price, EPS_forward, EPS_trailing"
             ", PE_forward, PE_trailing, `change`, change_percent, dividend, dividend_yield,"
             "market_cap, prev_close, volume, weight_sp500, year_high, year_low, date_time) "
         "VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)")
    data = tuple_from_dict(stonk)
    cursor.execute(query, data)


def delete(cursor):
    cursor.execute("DELETE FROM stocks")


# CREATE TABLE IF NOT EXISTS stocks (company_name VARCHAR(255), ticker VARCHAR(255), price FLOAT(7,2), EPS_forward FLOAT(6,2), EPS_trailing FLOAT(6,2),"
#                    "PE_forward FLOAT(6,2),"
#                    "PE_trailing FLOAT(6,2),"
#                    "`change` FLOAT(6,2),"
#                    "change_percent VARCHAR(255),"
#                    "dividend FLOAT(6,2),"
#                    "dividend_yield VARCHAR(255),"
#                    "market_cap VARCHAR(255),"
#                    "prev_close FLOAT(7,2),"
#                    "volume INT,"
#                    "weight_sp500 FLOAT(8,6),"
#                    "year_high FLOAT(6,2),"
#                    "year_low FLOAT(6,2),"
#                    "date_time DATETIME );