# coding: utf8
from marshmallow import (Schema, fields)


class LocationSchema(Schema):
    id = fields.String()
    name = fields.String()
    latitude = fields.Decimal()
    longitude = fields.Decimal()

class StationSchema(Schema):
    id = fields.String()
    order = fields.Integer()
    location = fields.Integer()
    is_active = fields.Boolean()    
