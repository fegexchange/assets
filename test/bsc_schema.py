from marshmallow import INCLUDE, Schema, fields


class BscSchema(Schema):
    id = fields.Str(required=True)
    name = fields.Str(required=True)
    symbol = fields.Str(required=True)
    type = fields.Str(required=True)
    decimals = fields.Int(required=True)

    class Meta:
        unknown = INCLUDE
