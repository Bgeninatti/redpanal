from __future__ import unicode_literals
from django.apps import AppConfig

class SocialConfig(AppConfig):

    name = 'social'

    def ready(self):
        from actstream import registry
        registry.register(self.get_model('Message'))
