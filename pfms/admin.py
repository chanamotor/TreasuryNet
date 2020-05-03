from django.contrib import admin

# Register your 3 models here.
from .models import (
    PfmsFileSeq,
    PfmsSchemeMaster,
    PfmsExpenditure
)
admin.site.register(PfmsFileSeq)
admin.site.register(PfmsSchemeMaster)
admin.site.register(PfmsExpenditure)
