# ! -*- coding: utf-8 -*-
#
# author: forcemain@163.com


from marshmallow import Schema, fields


class ResultListSchema(Schema):
    ip = fields.String(required=True)
    alive = fields.Boolean(required=True)
    created = fields.DateTime(required=True)
