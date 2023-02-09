from django.contrib import admin
from .models import Trinket, Uses, Merchant

admin.site.register(Trinket)
admin.site.register(Uses)
admin.site.register(Merchant)