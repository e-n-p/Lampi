##
# endpoints.py 22/2/2021
##

from marshmallow import Schema, fields, ValidationError


class onBannerSchema(Schema):
    #handle colour object with 2 arrays
    colour = fields.List(fields.Int(), required=True)
    intensity = fields.Float()


class onPulseSchema(Schema):
    colour = fields.List(fields.Int(), required=True)
    intensity = fields.Float()
