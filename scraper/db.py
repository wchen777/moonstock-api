def create_stock_table(cursor):
    cursor.execute("CREATE TABLE IF NOT EXISTS stocks ("
                   "company_name VARCHAR(255),"
                   "ticker VARCHAR(255),"
                   "price FLOAT(7,2),"
                   "EPS_forward FLOAT(6,2),"
                   "EPS_trailing FLOAT(6,2),"
                   "PE_forward FLOAT(6,2),"
                   "PE_trailing FLOAT(6,2),"
                   "change FLOAT(6,2),"
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