##
# endpoints.py 22/2/2021
##

from marshmallow import Schema, fields, ValidationError

class doubleColourSchema(Schema):
    firstColour = fields.List(fields.Int())
    secondColour = fields.List(fields.Int())

class onBannerSchema(Schema):
    colours = fields.Nested(doubleColourSchema, required=True)
    intensity = fields.Float()


class onPulseSchema(Schema):
    colour = fields.List(fields.Int(), required=True)
    intensity = fields.Float()
