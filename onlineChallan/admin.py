from django.contrib import admin

# Register your 2 models here.
from .models import (
    OnlineReceiptMaster,
    OnlineReceiptSeq,
)
admin.site.register(OnlineReceiptMaster)
admin.site.register(OnlineReceiptSeq)