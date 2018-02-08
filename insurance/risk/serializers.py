# Third Party Stuff
from rest_framework import serializers

from .models import Risk, RiskField


class RiskFieldSerializer(serializers.ModelSerializer):
    class Meta:
        model = RiskField
        fields = ('name', 'ftype')


class RiskSerializer(serializers.ModelSerializer):
    riskfields = RiskFieldSerializer(many=True)

    class Meta:
        model = Risk
        fields = ('name', 'insurer', 'riskfields')

    def create(self, validated_data):
        rfields_data = validated_data.pop('riskfields')
        risk = Risk.objects.create(**validated_data)
        for rfield_data in rfields_data:
            RiskField.objects.create(risk=risk, **rfield_data)
        return risk
