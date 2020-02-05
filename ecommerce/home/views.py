from django.shortcuts import render,redirect,HttpResponse
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, generics
from rest_framework.filters import SearchFilter,OrderingFilter
from .serializers import UserSerializer,ItemSerializer
from .models import homeslider,productcollectioninfo,blogpost,contact,webabout,Orders,productreview,orderupdate
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
import json
# from django.views.generic import  View
# //classmethod
# class BaseView(View):
#     dictonary={'items':homeslider.objects.all()
#
#                }
#
#        write in urls=home.as_view()
# class home(BaseView):
#     def get(self,request):
#         self.dictonary ['tablename']=table.objects.all
#
#         return render(request,'fghjk')



def index(request):
    sliderdata = homeslider.objects.all().order_by('-id')[:3]

    productdata = productcollectioninfo.objects.all().order_by('?')[:]
    return render(request,'index.html',{'slider':sliderdata,'productdata':productdata})


def productshow(request):

    productdata = productcollectioninfo.objects.all().order_by('?')[:]
    return render(request,'product.html',{'productdata':productdata})


def shoppingcart(request):
    productdata = productcollectioninfo.objects.all().order_by()
    return render(request,'shoping-cart.html',{'productdata':productdata})

def blog(request):
    productdata = productcollectioninfo.objects.all().order_by('?')[:]
    blogdata = blogpost.objects.all().order_by('-id')[:10]

    return render(request,'blog.html',{'productdata':productdata,'blogdata':blogdata})



def blogdetail(request):
    productdata = productcollectioninfo.objects.all().order_by('?')
    blogid = request.GET.get('name')
    target = blogpost.objects.get(id=blogid)
    return render(request,'blog-detail.html',{'productdata':productdata,'target':target})



def productdetail(request):
    ids=request.GET.get('name')
    productdata = productcollectioninfo.objects.all().order_by('?')
    data1 = productcollectioninfo.objects.get(id=ids)
    review = productreview.objects.all()
    count=0
    for item in review:
        if item.productid == int(ids):
            count=count+1
    productlike = data1.item_type
    productdata1 = productcollectioninfo.objects.filter(item_type=productlike).order_by('?')[:8]
    return render(request,'product-detail.html',{'data': data1,'productdata1':productdata1,'productdata':productdata,'review':review,'ids':int(ids),'count':count})

def about(request):
    productdata = productcollectioninfo.objects.all().order_by('?')
    aboutdata = webabout.objects.all().order_by()[:2]

    return render(request,'about.html',{'productdata':productdata,'aboutdata':aboutdata})


def contactshop(request):
    productdata = productcollectioninfo.objects.all().order_by('?')
    contactdata = contact.objects.all().order_by('-id')[:1]
    return render(request,'contact.html',{'productdata':productdata,'contactdata':contactdata})



def messageshop(request):
    from django.core.mail import send_mail
    email = request.POST.get('email')
    message = request.POST.get('msg')

    send_mail('New Message arrive', 'Hey there,'
                                      '\n We have received a Feedback about our service.'
                                      '\n'+message+
                                      '\n Greetings,\n Our Ecommerce Website\n user mail address:'+email,'onlineshoppingstore026@gmail.com',
               ['pradippandit026@gmail.com'],
              fail_silently=False)
    return redirect('home')



def loginform(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username,password=password)

        if user is not None:
            login(request,user)
            messages.success(request,"Successfully Logged In")
            return redirect('home')
        else:
            messages.error(request,"Invalid Credentials,Try again")
            return redirect('home')

    else:
        return HttpResponse('404-Not Found')


def signupform(request):
    if request.method =='POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        repassword = request.POST.get('repassword')
        firstname = request.POST.get('fname')
        lastname = request.POST.get('lname')
        username = request.POST.get('uname')
        if len(username) > 10 or len(username) < 4:
            messages.error(request,"username must between 4-10 character")
            return redirect('home')

        elif password != repassword:
            messages.error(request,"password do Not match")
            return redirect('home')

        elif User.objects.filter(username=username).exists():
            messages.error(request, "Username Already Taken try another")
            return redirect('home')

        elif User.objects.filter(email=email).exists():
            messages.error(request, "Email Already Taken try another")
            return redirect('home')

        elif not username.isalnum():
            messages.error(request,"username must be character and digits")
            return redirect('home')


        else:
            myuser =User.objects.create_user(username,email,password)
            myuser.first_name = firstname
            myuser.last_name = lastname

            myuser.save()

            user = authenticate(username=username, password=password)

            if user is not None:
                login(request, user)
                messages.success(request,"Your Account has been Successfully created and you are Logged In")
                return redirect('home')
            else:
                messages.error(request, "Invalid Credentials,Try again")
                return redirect('home')
    else:
        return HttpResponse('404-Not Found')


def logoutform(request):
        logout(request)
        messages.success(request, "You are Successfully Logout")
        return redirect('home')


def placeorder(request):
    if request.method == "POST":
        items_json = request.POST.get('itemsJson')
        name = request.POST.get('name', '')
        email = request.POST.get('email', '')
        address = request.POST.get('address1', '') + " " + request.POST.get('address2', '')
        city = request.POST.get('city', '')
        state = request.POST.get('state', '')
        zip_code = request.POST.get('zip_code', '')
        phone = request.POST.get('phone', '')
        order = Orders(items_json=items_json, name=name, email=email, address=address, city=city,
                       state=state, zip_code=zip_code, phone=phone)
        order.save()
        update = orderupdate(order_id=order.order_id, update_desc="The order has been placed")
        update.save()
        thank = True
        id = order.order_id
        return render(request, 'shoping-cart.html', {'thank': thank, 'id': id})
    return render(request, 'shoping-cart.html')


def reviewitem(request):
    if request.method == "POST":
        sms = request.POST.get('review')
        name = request.POST.get('name')
        email = request.POST.get('email')
        rating = request.POST.get('rating')
        productid = request.POST.get('ids')
        reviewproduct = productreview(useremail = email,reviewsms = sms, productid = productid, productstar = rating,name= name)
        reviewproduct.save()
        return redirect('shop')
    else:
        return redirect('home')



def searchMatch(query, item):
    if query in item.item_description.lower() or query in item.item_name.lower() or query in item.item_feature.lower() or query in item.item_type.lower():
        return True
    else:
        return False

def search_my_item(request):
    query = request.GET.get('search')


    prodtemp = productcollectioninfo.objects.all()
    prod = [item for item in prodtemp if searchMatch(query, item)]

    para = {'allprods':prod , "msg": ""}
    if len(prod ) == 0 or len(query)<3:
        para = {'msg': "Please make sure to enter relevant search query"}

    return render(request, 'searchshow.html', para)

def track_order(request):
    if request.method=="POST":
        orderId = request.POST.get('orderId', '')
        email = request.POST.get('email', '')
        try:
            order = Orders.objects.filter(order_id=orderId, email=email)
            if len(order)>0:
                update = orderupdate.objects.filter(order_id=orderId)
                updates = []
                for item in update:
                    updates.append({'text': item.update_desc, 'time': item.timestamp})
                    response = json.dumps([updates, order[0].items_json], default=str)
                return HttpResponse(response)
            else:
                return HttpResponse('{}')
        except Exception as e:
            return HttpResponse('{}')

    return render(request, 'tracker.html')


# API part...................................................................
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class ItemViewSet(viewsets.ModelViewSet):
    queryset = productcollectioninfo.objects.all()
    serializer_class = ItemSerializer


class ItemFilterListView(generics.ListAPIView):
    serializer_class = ItemSerializer
    queryset = productcollectioninfo.objects.all()
    filter_backends = (DjangoFilterBackend,OrderingFilter,SearchFilter)
    filter_fields = ['id','item_name','item_description','item_price']
    ordering_fields = ['id','item_price','item_name']
    search_fields = ['item_name','item_description','item_feature']