from django.utils.translation import gettext_lazy as _

from cms.app_base import CMSApp


class CatalogListCMSApp(CMSApp):
    name = _("Catalog List")

    def get_urls(self, page=None, language=None, **kwargs):
        raise NotImplementedError("{} must implement method `.get_urls()`.".format(self.__class__))


class OrderApp(CMSApp):
    name = _("View Orders")
    cache_placeholders = False

    def get_urls(self, page=None, language=None, **kwargs):
        from django.conf.urls import url
        from shop.views.order import OrderView

        return [
            url(r'^(?P<slug>[\w-]+)/(?P<secret>[\w-]+)', OrderView.as_view(many=False)),  # publicly accessible
            url(r'^(?P<slug>[\w-]+)', OrderView.as_view(many=False)),  # requires authentication
            url(r'^', OrderView.as_view()),  # requires authentication
        ]


class PasswordResetApp(CMSApp):
    name = _("Password Reset Confirm")

    def get_urls(self, page=None, language=None, **kwargs):
        from django.conf.urls import url
        from shop.views.auth import PasswordResetConfirmView

        return [
            url(r'^(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})',
                PasswordResetConfirmView.as_view(),
            )
        ]
