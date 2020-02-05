from django.db import models
import  datetime
uploaddate  = datetime.datetime.now()
lis=('men','Men'),('women','Women'),('bag','Bag'),('shoes','Shoes'),('watches','Watches')
class homeslider(models.Model):
    id = models.AutoField
    text1 = models.CharField(max_length=100, default='Collection')
    text2 = models.CharField(max_length=100, default='New arrivals')
    slideimage = models.ImageField(upload_to='sliderimage', blank=False)
    thumbcaption = models.CharField(max_length=30, default='Visit Shop')

    def __str__(self):
        return self.text1

class productcollectioninfo(models.Model):
    id=models.AutoField
    item_name = models.CharField(max_length=200, default='product name')
    item_price = models.IntegerField(default='Rs.00')
    item_type = models.CharField(choices=lis,max_length=100, default='*')
    item_feature = models.TextField(max_length=100,default='No Feature Mention')
    item_description = models.TextField(max_length=1000, default='No Description')
    additional_info_weight = models.CharField(max_length=10,default='..kg')
    additional_info_dimensions = models.CharField(max_length=20,default='.x.x.x cm')
    additional_info_material = models.CharField(max_length=50, default='..% cotton')
    additional_info_available_color = models.CharField(max_length=100,default='black,red,grey....')
    additional_info_size = models.CharField(max_length=50, default='S,M,L,XL,XXL')
    item_image = models.ImageField(upload_to='productImages',blank=False)
    item_Back_view = models.ImageField(upload_to='productImages',blank=False)
    item_alone_view = models.ImageField(upload_to='productImages',blank=False)


    def __str__(self):
        return self.item_name


class blogpost(models.Model):
    blogheading = models.TextField(max_length=100,blank=False,default="Today's Heading")
    blogtheme =  models.TextField(max_length=200,blank=False,default="Today's Heading theme")
    blogdescription_para1 = models.TextField(max_length=10000,blank=False,default="Description")
    blogdescription_para2 = models.TextField(max_length=10000,blank=True)
    blogdescription_para3 = models.TextField(max_length=10000,blank=True)
    blogtags = models.CharField(max_length=100,blank=False,default='Story')
    blogimage = models.ImageField(upload_to='blogimage',blank=False)
    date = models.DateTimeField(blank=True,default=uploaddate)

    def __str__(self):
        return self.blogheading



class contact(models.Model):
    shopaddress = models.CharField(max_length=200,blank=False,default='address')
    shopphone = models.IntegerField(blank=False)
    shopgmail = models.EmailField(blank=False)


    def __str__(self):
        return  self.shopaddress

class webabout(models.Model):
    about_heading = models.CharField(max_length=100, blank=False)
    about_para1 = models.TextField(max_length=1000, blank=False)
    about_para2 = models.TextField(max_length=1000, blank=True)
    about_image = models.ImageField(upload_to='about_images')
    about_theme = models.TextField(max_length=300, blank=False)
    thought_by = models.CharField(max_length=20,blank=True)

    def __str__(self):
        return self.about_heading


class Orders(models.Model):
    order_id = models.AutoField(primary_key=True)
    items_json = models.TextField(max_length=5000)
    name = models.CharField(max_length=90)
    email = models.CharField(max_length=111)
    address = models.CharField(max_length=111)
    city = models.CharField(max_length=111)
    state = models.CharField(max_length=111)
    zip_code = models.CharField(max_length=111)
    phone = models.CharField(max_length=111, default="")

    def __str__(self):
        return  self.city



class productreview(models.Model):
    reviewid = models.AutoField
    useremail = models.EmailField(blank=False)
    reviewsms = models.TextField(blank=False,max_length=1000)
    productid = models.IntegerField()
    productstar = models.IntegerField()
    name = models.CharField(blank=False,max_length=50)
    def __str__(self):
        return  self.name

class orderupdate(models.Model):
    update_id  = models.AutoField(primary_key=True)
    order_id = models.IntegerField(default="")
    update_desc = models.TextField(max_length=5000)
    timestamp = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.update_desc[0:10] + "..."