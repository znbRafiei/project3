from rest_framework import serializers

class ConversionSerializer(serializers.Serializer):
    value = serializers.FloatField()
    unit_to = serializers.ChoiceField(choices=[
        ('kg', 'کیلوگرم'),
        ('mg', 'میلی‌گرم'),
        ('ton', 'تن'),
        ('lb', 'پوند'),
        ('oz', 'اونس')
    ])