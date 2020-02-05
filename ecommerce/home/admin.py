from django.contrib import admin
from .models import homeslider,productcollectioninfo,blogpost,contact,webabout,Orders,productreview,orderupdate

class orders(admin.ModelAdmin):
    read_only = ["items_json","name","email","address"," city","state","zip_code","phone"]
    def has_change_permission(self, request, obj=None):
        return False

admin.site.register(Orders,orders)


class Productreview(admin.ModelAdmin):
    read_only = ["useremail","reviewsms","productid","productstar","name"]
    def has_change_permission(self, request, obj=None):
        return False
admin.site.register(productreview,Productreview)

admin.site.register(homeslider)
admin.site.register(productcollectioninfo)
admin.site.register(blogpost)
admin.site.register(contact)
admin.site.register(webabout)
admin.site.register(orderupdate)
