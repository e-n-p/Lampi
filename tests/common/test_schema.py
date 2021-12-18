"""
    test_schema
"""

import unittest
from marshmallow import ValidationError
from server.api.common.schema import OnBasicSchema, OnDoubleSchema

class TestBasicSchema(unittest.TestCase):

    def test_basic_schema(self):
        json_test = '{"colour":[27,222,242], "intensity": "1.0"}'
        schema = OnBasicSchema()
        out = schema.loads(json_test)
        self.assertEqual(
            out,
            {
                'colour': [27, 222, 242],
                'intensity': 1.0
            }
        )

    def test_basic_schema_fails_on_too_many_values(self):
        json_test = '{"colour":[27,222,242,100]}'
        schema = OnBasicSchema()
        with self.assertRaisesRegex(ValidationError, 'Too many values, only RGB supported'):
            schema.loads(json_test)

    def test_basic_schema_fails_on_mispelling(self):
        json_test = '{"color":[27,222,242]}'
        schema = OnBasicSchema()
        with self.assertRaises(ValidationError):
            schema.loads(json_test)

    def test_basic_schema_fails_with_high_colour_out_of_bound_values(self):
        json_test = '{"colour":[300,222,242]}'
        schema = OnBasicSchema()
        with self.assertRaisesRegex(
            ValidationError,
            'Colour value too high, valid range is: 0-255'
        ):
            schema.loads(json_test)

    def test_basic_schema_fails_with_low_colour_out_of_bound_values(self):
        json_test = '{"colour":[-5,222,242]}'
        schema = OnBasicSchema()
        with self.assertRaisesRegex(
            ValidationError,
            'Colour value too low, valid range is: 0-255'
        ):
            schema.loads(json_test)

    def test_basic_schema_fails_with_high_intensity_out_of_bound_values(self):
        json_test = '{"colour":[300,222,242], "intensity": "2.0"}'
        schema = OnBasicSchema()
        with self.assertRaisesRegex(ValidationError, 'intensity value too high'):
            schema.loads(json_test)

    def test_basic_schema_fails_with_low_intensity_out_of_bound_values(self):
        json_test = '{"colour":[300,222,242], "intensity": "0.0"}'
        schema = OnBasicSchema()
        with self.assertRaisesRegex(ValidationError, 'intensity value too low'):
            schema.loads(json_test)



class TestDoubleSchema(unittest.TestCase):

    def test_double_schema(self):
        json_test = '''
            {
                "colours":{
                    "firstColour": [27,220,242],
                    "secondColour": [150,150,150]
                },
                "intensity": "1.0"
            }
        '''
        schema = OnDoubleSchema()
        out = schema.loads(json_test)
        self.assertEqual(
            out,
            {
                'colours':{
                    'firstColour': [27,220,242],
                    'secondColour': [150,150,150]
                },
                'intensity': 1.0
            }
        )

    def test_double_schema_missing_a_colour(self):
        json_test = '{"colours":{"firstColour": [27,220,242]}}'
        schema = OnDoubleSchema()
        with self.assertRaisesRegex(
            ValidationError,
            r"{'colours': {'secondColour': \['Missing data for required field.'\]}}"
        ):
            schema.loads(json_test)

    def test_double_schema_fails_on_a_mispelling(self):
        json_test = '{"colors":{"firstColour": [27,220,242,0], "secondColor": [150,150,150]}}'
        schema = OnDoubleSchema()
        with self.assertRaises(ValidationError):
            schema.loads(json_test)

    def test_double_schema_fails_on_too_many_values(self):
        json_test = '{"colours":{"firstColour": [27,220,242,0], "secondColour": [150,150,150]}}'
        schema = OnDoubleSchema()
        with self.assertRaisesRegex(ValidationError, 'Too many values, only RGB supported'):
            schema.loads(json_test)

    def test_double_schema_fails_with_high_out_of_bound_values(self):
        json_test = '{"colours":{"firstColour": [27,220,1000], "secondColour": [150,150,150]}}'
        schema = OnDoubleSchema()
        with self.assertRaisesRegex(
            ValidationError,
            r"{'colours': {'firstColour': \['Colour value too high, valid range is: 0-255'\]}}"
        ):
            schema.loads(json_test)

    def test_double_schema_fails_with_low_out_of_bound_values(self):
        json_test = '{"colours":{"firstColour": [27,220,-50], "secondColour": [150,-150,150]}}'
        schema = OnDoubleSchema()
        with self.assertRaises(ValidationError):
            schema.loads(json_test)

    def test_double_schema_fails_with_high_intensity_out_of_bound_values(self):
        json_test = '''
            {
                "colours":{
                    "firstColour": [27,220,242],
                    "secondColour": [150,150,150]
                },
                "intensity": "2.0"
            }
        '''
        schema = OnDoubleSchema()
        with self.assertRaisesRegex(ValidationError, 'intensity value too high'):
            schema.loads(json_test)

    def test_double_schema_fails_with_low_intensity_out_of_bound_values(self):
        json_test = '''
            {
                "colours":{
                    "firstColour": [27,220,242],
                    "secondColour": [150,150,150]
                },
                "intensity": "0.0"
            }
        '''
        schema = OnDoubleSchema()
        with self.assertRaisesRegex(ValidationError, 'intensity value too low'):
            schema.loads(json_test)

    def test_double_schema_fails_with_wrong_intensity_type(self):
        json_test = '''
            {
                "colours":{
                    "firstColour": [27,220,242],
                    "secondColour": [150,150,150]
                },
                "intensity": "f"
            }
        '''
        schema = OnDoubleSchema()
        with self.assertRaises(ValidationError):
            schema.loads(json_test)


if __name__ == '__main__':
    unittest.main()
