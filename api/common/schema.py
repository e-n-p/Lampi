##
# endpoints.py 22/2/2021
##

from marshmallow import Schema, fields, validates, ValidationError


def validate_colour(value):
    if len(value) > 3:
        raise ValidationError("Too many values, only RGB supported")
    if len(value) < 3:
        raise ValidationError("Not enough values, only RGB supported")
    if (value[0] < 0) or (value[1] < 0) or (value[2] < 0):
        raise ValidationError("Colour value too low, valid range is: 0-255")
    if (value[0] > 255) or (value[1] > 255) or (value[2] > 255):
        raise ValidationError("Colour value too high, valid range is: 0-255")

def validate_intensity(value):
    if value < 0.1:
        raise ValidationError("intensity value too low")
    if value > 1.0:
        raise ValidationError("intensity value too high")

class doubleColourSchema(Schema):
    firstColour = fields.List(fields.Int(), validate=validate_colour)
    secondColour = fields.List(fields.Int(), validate=validate_colour)

class onBannerSchema(Schema):
    colours = fields.Nested(doubleColourSchema, required=True)
    intensity = fields.Float(validate=validate_intensity)

class onBasicSchema(Schema):
    colour = fields.List(fields.Int(), required=True, validate=validate_colour)
    intensity = fields.Float(validate=validate_intensity)

