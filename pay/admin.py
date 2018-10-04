# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from . models import *


admin.site.register(User)
admin.site.register(Transaction)
admin.site.register(Form)
admin.site.register(Coupons)
admin.site.register(Services)
# Register your models here.
