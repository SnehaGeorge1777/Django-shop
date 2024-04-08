import phonenumber_field
from django.db.models import CharField
from rest_framework import serializers

from shop.models.customer import CustomerModel


class ChangePhoneNumberSerializer(serializers.ModelSerializer):
    phone_number = phonenumber_field.modelfields.PhoneNumberField

    class Meta:
        model = CustomerModel
        fields = ['phone_number']
