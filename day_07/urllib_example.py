from urllib.request import urlopen
from urllib.parse import urlencode

import json

res = urlopen('http://apis.is/car?number=KI966')

print(json.loads(res.read()))


def get_car_info(license):
    enc = urlencode({'number': license})
    res = urlopen(f'http://apis.is/car?{enc}')
    return json.loads(res.read())
