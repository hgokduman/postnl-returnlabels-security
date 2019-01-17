import requests

Company = 'Zalando' # Zalando of MANGO
nr_calls = 50
	
if Company == 'Zalando':
	API_URL = 'https://jouw.postnl.nl/web/api/default/shipmentStatus/3SEAGK0141%05d-NL-5140WR'
	start_no = 0
elif Company == 'MANGO':
	API_URL = 'https://jouw.postnl.nl/web/api/default/shipmentStatus/3SEASY0002%05d-NL-4800VB'
	start_no = 48950
else:
	print('Onjuiste bedrijfsnaam')
	exit()
	
def xstr(s):
    if s is None:
        return ''
    return str(s)

print('barcode, bezorgstatus, naam, adres, postcode, plaats')
for x in range(start_no, start_no+nr_calls):
	request_url = API_URL % (x)
	result = requests.get(request_url)
	if result.status_code == requests.codes.ok:
		result = result.json()
		barcode = result['barcode']
		shipment = result['shipments'][barcode]
		delivery_status = shipment['delivery']['status']
		if shipment['sender']['firstName'] != None:
			cust_name = '%s %s' % (shipment['sender']['firstName'], shipment['sender']['lastName'])
		else:
			cust_name = shipment['sender']['companyName']
		cust_address = '%s %s%s' % (shipment['sender']['street'], shipment['sender']['houseNumber'], xstr(shipment['sender']['houseNumberSuffix']))
		cust_postalcode = shipment['sender']['postalCode']
		cust_town = shipment['sender']['town']
		line = f'{barcode}, {delivery_status}, {cust_name}, {cust_address}, {cust_postalcode}, {cust_town}'
		print(line)