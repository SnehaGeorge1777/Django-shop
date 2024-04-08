from django.db import connection
from django.utils.translation import gettext_lazy as _

from rest_framework.generics import GenericAPIView
from rest_framework.response import Response

from shop.models.customer import CustomerModel
from shop.serializers.phone import ChangePhoneNumberSerializer
from softsecshop import settings


class ChangePhoneNumberView(GenericAPIView):
    form_name = 'change_phone_number_form'
    serializer_class = ChangePhoneNumberSerializer

    def get(self, request, *args, **kwargs):
        customer = CustomerModel.objects.get_from_request(self.request)
        return Response({self.form_name: {
            'phone_number': _(str(customer.phone_number))
        }})

    def post(self, request, *args, **kwargs):
        form_data = request.data.get('form_data', {})
        phone_number = form_data.get("phone_number")
        customer = CustomerModel.objects.get_from_request(self.request)
        user_id = customer.user_id
        with connection.cursor() as cursor:
            cursor.execute("UPDATE " + settings.SHOP_APP_LABEL + "_customer SET phone_number = "
                           + phone_number
                           + " WHERE user_id = " + str(user_id))
        return Response({self.form_name: {'success_message': _("Phone number has been changed successfully.") }})
