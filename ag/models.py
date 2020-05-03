from django.db import models

# 1 Tables.
class AgMonthlyAccounts(models.Model):
    class Meta:
        unique_together = (('fin_year', 'treasury_code','mm_yyyy'),)
    fin_year = models.CharField(max_length=9)
    treasury_code = models.CharField(max_length=2)
    mm_yyyy = models.CharField(max_length=7)
    status = models.CharField(max_length=1)