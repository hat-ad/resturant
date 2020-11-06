from django.shortcuts import render, redirect, reverse, HttpResponse
from django.contrib.auth.views import login_required
from django.contrib.auth import login, logout
from django.contrib.auth.models import User
from django.core.mail import send_mail
from rest_framework.generics import ListAPIView, RetrieveAPIView
from . import models
from . import serializers
import json


def handler404(request, *args, **argv):
    return render(request, '404.html', status=404)


def handler500(request, *args, **argv):
    return render(request, '500.html', status=500)


def register_view(request):
    status = 0
    if 'first_name' in request.POST and 'last_name' in request.POST \
            and 'email' in request.POST and 'password' in request.POST:
        try:
            user = User.objects.get(email=request.POST['email'])
            status = 1
        except User.DoesNotExist:
            user = User(first_name=request.POST['first_name'],
                        last_name=request.POST['last_name'],
                        email=request.POST['email'],
                        username=request.POST['email'])
            user.set_password(request.POST['password'])
            user.save()
            login(request, user)
            return redirect(reverse('index'))
    return render(request, 'register.html', {'status': status})


def login_view(request):
    status = 0
    if 'email' in request.POST and 'password' in request.POST:
        email = request.POST['email']
        password = request.POST['password']
        try:
            user = User.objects.get(email=email)
            if user.check_password(password):
                login(request, user)
                return redirect(reverse('index'))
            else:
                status = 1
        except User.DoesNotExist:
            status = 2
    return render(request, 'login.html', {'status': status})


def logout_view(request):
    logout(request)
    return redirect(reverse('index'))


def forgot_view(request):
    status = 0
    if 'email' in request.POST:
        try:
            user = User.objects.get(email=request.POST['email'])
            send_mail('Reset password',
                      'Reset your password here: http://127.0.0.1:8000/reset/' +
                      str(user.id)+'/',
                      'subhobasak22@gmail.com', [user.email, ])
        except User.DoesNotExist:
            status = 1
    return render(request, 'forgot.html', {'status': status})


def reset_view(request, uid):
    status = 0
    if 'new_pswd' in request.POST and 'cnfrm_pswd' in request.POST:
        if request.POST['new_pswd'] == request.POST['cnfrm_pswd']:
            try:
                user = User.objects.get(id=uid)
                user.set_password(request.POST['new_pswd'])
                user.save()
                login(request, user)
                return redirect(reverse('index'))
            except User.DoesNotExist:
                status = 1
        else:
            status = 2
    return render(request, 'reset.html', {'status': status})


@login_required
def index_view(request):

    # if request.method == 'POST':
    #     print(request.POST)
    return render(request, 'order.html')


class CustomerDetailsPhone(RetrieveAPIView):
    lookup_field = 'phone'
    queryset = models.Customer.objects.all()
    serializer_class = serializers.CustomerSerializer


class CustomerDetailsEmail(RetrieveAPIView):
    lookup_field = 'email'
    queryset = models.Customer.objects.all()
    serializer_class = serializers.CustomerSerializer


class VegBreakfastItems(ListAPIView):
    queryset = models.Product.objects.filter(type='0', category='0')
    serializer_class = serializers.ItemSerializer


class VegMealItems(ListAPIView):
    queryset = models.Product.objects.filter(type='0', category='1')
    serializer_class = serializers.ItemSerializer


class VegSnacksItems(ListAPIView):
    queryset = models.Product.objects.filter(type='0', category='2')
    serializer_class = serializers.ItemSerializer


class VegDinnerItems(ListAPIView):
    queryset = models.Product.objects.filter(type='0', category='3')
    serializer_class = serializers.ItemSerializer


class NonVegBreakfastItems(ListAPIView):
    queryset = models.Product.objects.filter(type='1', category='0')
    serializer_class = serializers.ItemSerializer


class NonVegMealItems(ListAPIView):
    queryset = models.Product.objects.filter(type='1', category='1')
    serializer_class = serializers.ItemSerializer


class NonVegSnacksItems(ListAPIView):
    queryset = models.Product.objects.filter(type='1', category='2')
    serializer_class = serializers.ItemSerializer


class NonVegDinnerItems(ListAPIView):
    queryset = models.Product.objects.filter(type='1', category='3')
    serializer_class = serializers.ItemSerializer


@login_required
def order_view(request, table_id, order_id):
    waiters = models.Waiter.objects.all()
    tables = models.Table.objects.filter(fill=0)
    if order_id > 0:
        try:
            order = models.Order.objects.get(id=order_id)
        except models.Order.DoesNotExist:
            return redirect(reverse('table'))
    else:
        try:
            table = models.Table.objects.get(id=table_id)
            order = models.Order(table_no=table)
            order.save()
        except models.Table.DoesNotExist:
            return reverse(redirect('table'))

    return render(request, 'order.html',
                  {'waiters': waiters, 'tables': tables, 'table_no': table_id})


@login_required
def table_view(request):
    tables = models.Table.objects.all()
    models.Order.objects.filter(customer=None).delete()
    if 'table_id' in request.POST:
        if 'new_order' in request.POST:
            return redirect('/order/'+str(request.POST['table_id'])+'/0/')
        elif 'edit' in request.POST and 'order_id' in request.POST:
            return redirect('/order/'+str(request.POST['table_id'])+'/'+str(request.POST['order_id'])+'/')
        elif 'complete' in request.POST and 'order_id' in request.POST:
            try:
                table = models.Table.objects.get(id=request.POST['table_id'])
                table.fill = 0
                table.save()
            except models.Table.DoesNotExist:
                pass
            return redirect(reverse('table'))
    return render(request, 'table.html', {'tables': tables})


def testView(request):
    print(request.POST)
    return HttpResponse("test")
