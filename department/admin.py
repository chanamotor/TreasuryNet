from django.contrib import admin

# Register your models 6 here.
from .models import (
    OnlineBillMaster,
    OnlineBillDeductions,
    OnlineBillSubDetails,
    OnlineGpfTotal,
    OnlineGpfDetails,
    OnlineBillSeq,
    DepartmentUsers,
    EmployeeBankDetails
)
admin.site.register(OnlineBillMaster)
admin.site.register(OnlineBillDeductions)
admin.site.register(OnlineBillSubDetails)
admin.site.register(OnlineGpfTotal)
admin.site.register(OnlineGpfDetails)
admin.site.register(OnlineBillSeq)
admin.site.register(DepartmentUsers)
admin.site.register(EmployeeBankDetails)