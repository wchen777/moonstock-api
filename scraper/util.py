def convert_to_float(stonk, key):
    if stonk[key] == '-':
        return
    stonk[key] = float(stonk[key].replace(',', ''))


def convert_to_int(stonk, key):
    if stonk[key] == '-':
        return
    stonk[key] = int(stonk[key].replace(',', ''))


def fix_values(stonk):
    convert_to_float(stonk, 'EPS_forward')
    convert_to_float(stonk, 'EPS_trailing')
    convert_to_float(stonk, 'PE_forward')
    convert_to_float(stonk, 'PE_trailing')
    convert_to_float(stonk, 'change')
    convert_to_float(stonk, 'price')
    convert_to_float(stonk, 'dividend')
    convert_to_float(stonk, 'weight_sp500')
    convert_to_float(stonk, 'year_high')
    convert_to_float(stonk, 'year_low')
    convert_to_float(stonk, 'prev_close')
    convert_to_int(stonk, 'volume')

