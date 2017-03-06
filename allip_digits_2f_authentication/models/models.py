# -*- coding: utf-8 -*-
from odoo import models, fields, api
import logging
_logger = logging.getLogger(__name__)
from odoo.http import request
from odoo import http


class digitsConfiguration(models.Model):
    _name = 'digits.configuration'

    digits_consumer_key = fields.Char('CONSUMER KEY (API KEY)', size=256)

    @api.model
    def get_digits_consumer_key(self, values):
        userInfo = http.request.env['res.users'].search([('id', '=', request.session.uid)])

        def convert_ascii(s):
            if s:
                return s.encode('ascii', 'ignore')
            return ''

        url = request.httprequest.host_url+
        url += '&appname=' + convert_ascii(userInfo[0].company_id.name)
        url += '&email=' + convert_ascii(userInfo[0].company_id.email)
        url += '&street=' + convert_ascii(userInfo[0].company_id.street)
        url += '&street2=' + convert_ascii(userInfo[0].company_id.street2)
        url += '&city=' + convert_ascii(userInfo[0].company_id.city)
        url += '&state=' + convert_ascii(userInfo[0].company_id.state_id.name)
        url += '&country=' + convert_ascii(userInfo[0].company_id.country_id.name)
        url += '&phone=' + convert_ascii(userInfo[0].company_id.phone)

        return {
            'type': 'ir.actions.act_url',
            'target': 'new',
            'url': 'https://www.allipcloud.com/consumer/key/form?url=' + url
        }
