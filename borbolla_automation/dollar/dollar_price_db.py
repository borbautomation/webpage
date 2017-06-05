#!/usr/bin/env python3

import os
from webscrap import Dolar
os.environ.setdefault('DJANGO_SETTINGS_MODULE',
'borbolla_automation.settings')
import django
django.setup()
from dollar.models import Banco , Precio

def populate():
	dollar = Dolar()
	for banco in dollar.divisas:
		bank,created = Banco.objects.get_or_create(nombre = banco['banco'])
		bank.save()
		print(created)
		precio_hoy = Precio.objects.create(banco = banco , compra = banco['compra'] , venta = banco['venta'])
        precio_hoy.save()

if __name__ == '__main__':
	print('starting populating script...')
	populate()        
	print('done...')