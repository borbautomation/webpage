#!/usr/bin/env python3

import bs4 , requests

class Dolar(object):
    """docstring for Dolar"""
    def __init__(self):       
        
        self.divisas = []
        self.get_current_price()

    def get_current_price(self): 
        request = requests.get('http://www.eldolar.info/es-MX/mexico/dia/hoy')
        request.raise_for_status()
        dolar = bs4.BeautifulSoup(request.text,'lxml')
        bancos = dolar.findAll('span',{'class':'small-hide'})   
        for banco in bancos:
            diccionario = {}
            diccionario['banco'] = banco.get_text()
            if len(banco.parent.parent.parent.findAll('td',{'class':'xTimes'})) == 1:
                compra = banco.parent.parent.parent.findAll('td',{'class':'xTimes'})
                venta  = banco.parent.parent.parent.findAll('td',{'class':'xTimes'})
                diccionario['compra'] = compra[0].get_text()
                diccionario['venta']  = venta[0].get_text()
                self.divisas.append(diccionario)
            else:    
                try:          
                    compra,venta = banco.parent.parent.parent.findAll('td',{'class':'xTimes'})
                    diccionario['compra'] = compra.get_text()
                    diccionario['venta']  = venta.get_text()
                    self.divisas.append(diccionario)
                except ValueError as e:
                    pass

    def get_best_sell(self):
        best = 10000
        for banco in self.divisas:
            if float(banco['venta'])<best:
                if float(banco['venta']) == float(banco['compra']):
                    pass
                else:    
                    mejor_venta = banco
                    best = float(banco['venta'])
        return mejor_venta        

   
    def get_best_buy(self):
        best = 0
        for banco in self.divisas:
            if float(banco['compra'])>best:
                if float(banco['venta']) == float(banco['compra']):
                    pass
                else:    
                    mejor_venta = banco
                    best = float(banco['compra'])
        return mejor_venta           

if __name__ == '__main__':
    a = Dolar()
    print(a.divisas)
    print(a.get_best_sell())
    print(a.get_best_buy())