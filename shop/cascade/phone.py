from __future__ import unicode_literals

from cms.plugin_pool import plugin_pool
from cmsplugin_cascade.fields import GlossaryField
from cmsplugin_cascade.plugin_base import CascadeFormMixin
from django.forms import widgets
from django.utils.translation import ugettext_lazy as _

from shop.cascade.plugin_base import ShopPluginBase


class ChangePhoneNumberPlugin(ShopPluginBase):
    name = _("Change Phone Number")
    form = CascadeFormMixin
    require_parent = True
    allow_children = False
    parent_classes = ['BootstrapColumnPlugin']
    render_template = 'shop/phone/default.html'

    def render(self, context, instance, placeholder):
        context['form_name'] = 'change_phone_number_form'
        return self.super(ChangePhoneNumberPlugin, self).render(context, instance, placeholder)


plugin_pool.register_plugin(ChangePhoneNumberPlugin)
