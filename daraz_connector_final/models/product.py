# -*- coding: utf-8 -*-

from odoo import models, fields, api,_
from odoo.exceptions import Warning
from datetime import datetime ,timezone
import requests
import urllib.parse
from hashlib import sha256
from hmac import HMAC
import json


class ProductProduct(models.Model):
    _inherit = "product.product"

    is_dz_product = fields.Boolean("Is Daraz Product?")
    instance_id = fields.Many2one('daraz.connector', 'Daraz Store')
    sku = fields.Char('Sku')
    export_to_daraz = fields.Boolean("Export To Daraz?")


    def doConnection(self, action=None, req=None, instance_id=False):
        darazStore = instance_id
        url = darazStore.api_url
        key = darazStore.api_key
        action = action if action else "GetProducts"
        format = "json"
        userId = darazStore.userId
        method= req if req  else 'GET'

        now = datetime.now().timestamp()
        test = datetime.fromtimestamp(now, tz=timezone.utc).replace(microsecond=0).isoformat()
        parameters = {
            'UserID': userId,
            'Version': "1.0",
            'Action':action,
            'Format': format,
            'Timestamp': test}
        concatenated = urllib.parse.urlencode(sorted(parameters.items()))
        data = concatenated.encode('utf-8')
        parameters['Signature'] = HMAC(key.encode('utf-8'), data,sha256).hexdigest()
        headers = {
            'Content-Type': "application/json",
            'Accept': "*/*",
            'Connection': "keep-alive",
            'cache-control': "no-cache"
        }
        try:
            response = requests.request(method, url, headers=headers, params=parameters)
        except Exception as e:
            raise Warning(_(response.text))
        return json.loads(response.text)

    def import_product(self, instance):
        res = self.doConnection('GetProducts','GET', instance)
        result = res.get('SuccessResponse', {}).get('Body', {})
        print(result)
        if result:
            product = self.create_product(result, instance)

        return  

    def create_product(self, records, parent=None):
        product_obj = self.env['product.product']
        name = records.get("name")
        product = product_obj.create({
                "name": name, 
                
                })
        return


    def doConnection(self, action=None, req=None, instance_id=False):
        darazStore = instance_id
        url = darazStore.api_url
        key = darazStore.api_key
        action = action if action else "CreateProduct"
        format = "json"
        userId = darazStore.userId
        method= req if req  else 'GET'

        now = datetime.now().timestamp()
        test = datetime.fromtimestamp(now, tz=timezone.utc).replace(microsecond=0).isoformat()
        parameters = {
            'UserID': userId,
            'Version': "1.0",
            'Action':action,
            'Format': format,
            'Timestamp': test}
        concatenated = urllib.parse.urlencode(sorted(parameters.items()))
        data = concatenated.encode('utf-8')
        parameters['Signature'] = HMAC(key.encode('utf-8'), data,sha256).hexdigest()
        headers = {
            'Content-Type': "application/json",
            'Accept': "*/*",
            'Connection': "keep-alive",
            'cache-control': "no-cache"
        }
        try:
            response = requests.request(method, url, headers=headers, params=parameters)
        except Exception as e:
            raise Warning(_(response.text))
        return json.loads(response.text)


    def export_to_daraz(self):


        return 