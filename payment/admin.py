from django.contrib import admin
from payment.models import Payment, Payment_detail


@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    pass

@admin.register(Payment_detail)
class PaymentdetailAdmin(admin.ModelAdmin):
    pass


