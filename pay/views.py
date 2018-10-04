from __future__ import unicode_literals
from django.shortcuts import render, get_object_or_404
from django_filters.views import FilterView
from django_tables2.views import SingleTableMixin
from .tables import PersonTable
from . models import *
from . forms import *
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.db.models import Count, Q
from graphos.sources.model import ModelDataSource
from graphos.renderers.gchart import LineChart
from graphos.renderers.gchart import ColumnChart
from graphos.renderers.gchart import BarChart
from graphos.renderers import flot
from graphos.sources.simple import SimpleDataSource
from django.db.models import Sum
from django.shortcuts import render
from django.http import HttpResponse
from collections import OrderedDict

# Include the `fusioncharts.py` file that contains functions to embed the charts.
from fusioncharts import FusionCharts








def test(request):
     dataSource = OrderedDict()

    # The `chartConfig` dict contains key-value pairs of data for chart attribute
     chartConfig = OrderedDict()
     chartConfig["caption"] = "No.of Users/Day"
     chartConfig["subCaption"] = ""
     chartConfig["xAxisName"] = "Date"
     chartConfig["yAxisName"] = "No.of Users"
     chartConfig["numberSuffix"] = ""
     chartConfig["theme"] = "fusion"

    # The `chartData` dict contains key-value pairs of data
     chartData = OrderedDict()
     chartData["2018-09-22"] = 2
     chartData["2018-09-23"] = 0
     chartData["2018-09-24"] = 0
     chartData["2018-09-25"] = 0
     chartData["2018-09-26"] = 0
     chartData["2018-09-27"] = 0
     chartData["2018-09-28"] = 0
     chartData["2018-09-29"] = 1
     chartData["2018-09-30"] = 0
     chartData["2018-10-01"] = 0
     chartData["2018-10-02"] = 0
     chartData["2018-10-03"] = 0

     dataSource["chart"] = chartConfig
     dataSource["data"] = []

    # Convert the data in the `chartData`array into a format that can be consumed by FusionCharts.
    #The data for the chart should be in an array wherein each element of the array 
    #is a JSON object# having the `label` and `value` as keys.

    #Iterate through the data in `chartData` and insert into the `dataSource['data']` list.
     for key, value in chartData.items():
         data = {}
         data["label"] = key
         data["value"] = value
         dataSource["data"].append(data)

     column2D = FusionCharts("column2d", "myFirstChart", "600", "400", "myFirstchart-container", "json", dataSource)



# Create an object for the column 2D chart using the FusionCharts class constructor
# The chart data is passed to the `dataSource` parameter.


     tes = User.objects.count()
     tes99 = User.objects.all()
     tes1 = Transaction.objects.count()
     tes12 = Transaction.objects.all()
     tes123 = Transaction.objects.annotate(Sum('Amount'))
     tes2 = Transaction.objects.filter(Description__contains='Cashing').count()
     tes44 = Transaction.objects.filter(Description__contains='Cashing')
     tes3 = Transaction.objects.filter(Description__contains='Bill').count()
     tes32 = Transaction.objects.filter(Description__contains='Bill')
     tes4 = Transaction.objects.filter(Description__contains='Friend').count()
     tes45 = Transaction.objects.filter(Description__contains='Friend')
     tes5 = Transaction.objects.filter(Description__contains='Purchase').count()
     tes56 = Transaction.objects.filter(Description__contains='Purchase')

     dataSource2 = OrderedDict()

    # The `chartConfig` dict contains key-value pairs of data for chart attribute
     chartConfig1 = OrderedDict()
     chartConfig1["caption"] = "No.of Active Users/Day"
     chartConfig1["subCaption"] = ""
     chartConfig1["xAxisName"] = "Date"
     chartConfig1["yAxisName"] = "No.of Active User"
     chartConfig1["numberSuffix"] = ""
     chartConfig1["theme"] = "fusion"

    # The `chartData` dict contains key-value pairs of data
     chartData1 = OrderedDict()
     chartData1["2018-09-22"] = 2
     chartData1["2018-09-23"] = 0
     chartData1["2018-09-24"] = 0
     chartData1["2018-09-25"] = 1
     chartData1["2018-09-26"] = 0
     chartData1["2018-09-27"] = 0
     chartData1["2018-09-28"] = 0
     chartData1["2018-09-29"] = 0 
     chartData1["2018-09-30"] = 0
     chartData1["2018-10-01"] = 0
     chartData1["2018-10-02"] = 0
     chartData1["2018-10-03"] = 0

     dataSource2["chart"] = chartConfig1
     dataSource2["data"] = []

    # Convert the data in the `chartData`array into a format that can be consumed by FusionCharts.
    #The data for the chart should be in an array wherein each element of the array 
    #is a JSON object# having the `label` and `value` as keys.

    #Iterate through the data in `chartData` and insert into the `dataSource['data']` list.
     for key, value in chartData1.items():
         data1 = {}
         data1["label"] = key
         data1["value"] = value
         dataSource2["data"].append(data1)



     colum2D = FusionCharts("column2d", "myFirstChart1", "600", "400", "myFirstchart-container2", "json", dataSource2)
 
     dataSource3 = OrderedDict()

    # The `chartConfig` dict contains key-value pairs of data for chart attribute
     chartConfig3 = OrderedDict()
     chartConfig3["caption"] = "No.of Transactions/Day"
     chartConfig3["subCaption"] = ""
     chartConfig3["xAxisName"] = "Date"
     chartConfig3["yAxisName"] = "No.of Transactions"
     chartConfig3["numberSuffix"] = ""
     chartConfig3["theme"] = "fusion"

    # The `chartData` dict contains key-value pairs of data
     chartData3 = OrderedDict()
     chartData3["2018-09-22"] = 6
     chartData3["2018-09-23"] = 0
     chartData3["2018-09-24"] = 0
     chartData3["2018-09-25"] = 1
     chartData3["2018-09-26"] = 0
     chartData3["2018-09-27"] = 0
     chartData3["2018-09-28"] = 0
     chartData3["2018-09-29"] = 0 
     chartData3["2018-09-30"] = 0
     chartData3["2018-10-01"] = 0
     chartData3["2018-10-02"] = 0
     chartData3["2018-10-03"] = 0

     dataSource3["chart"] = chartConfig3
     dataSource3["data"] = []

    # Convert the data in the `chartData`array into a format that can be consumed by FusionCharts.
    #The data for the chart should be in an array wherein each element of the array 
    #is a JSON object# having the `label` and `value` as keys.

    #Iterate through the data in `chartData` and insert into the `dataSource['data']` list.
     for key, value in chartData3.items():
         data3 = {}
         data3["label"] = key
         data3["value"] = value
         dataSource3["data"].append(data3)

     colun2D = FusionCharts("column2d", "myFirstChart3", "600", "400", "myFirstchart-container3", "json", dataSource3)
 
 
     context = {
                'tes' : tes,
               'tes123' : tes123,
               'tes99' : tes99,
               'tes1' : tes1,
               'tes2' : tes2,
               'tes3' : tes3,
               'tes4' : tes4,
               'tes5' : tes5,
               'tes32' : tes32,
               'tes44' : tes44,
               'tes45' : tes45,
               'tes56' : tes56,
               'tes12' : tes12,
               'output' : column2D.render(),
               'output1' : colum2D.render(),
               'output2' : colun2D.render(),
               }
    
     return render(request, 'pay/index2.html', context)





def complaint(request):
    sd = Services.objects.all().filter(complaint__isnull=False)
    return render(request, 'pay/complaint.html', {'sd' : sd})


def Serviced1(request):
    tes1 = Services.objects.filter(Service_type__contains='Internet')
    context = {
            'tes1' : tes1,
            }
    return render(request, 'pay/serve1.html', context)

def Serviced2(request):
    tes1 = Services.objects.filter(Service_type__contains='Servicos')
    context = {
            'tes1' : tes1,
            }
    return render(request, 'pay/serve2.html', context)



def Serviced3(request):
    tes1 = Services.objects.filter(Service_type__contains='Taxas')
    context = {
            'tes1' : tes1,
            }
    return render(request, 'pay/serve3.html', context)

def Serviced4(request):
    tes1 = Services.objects.filter(Service_type__contains='Companhias')
    context = {
            'tes1' : tes1,
            }
    return render(request, 'pay/serve4.html', context)

def Serviced5(request):
    tes1 = Services.objects.filter(Service_type__contains='Seguros')
    context = {
            'tes1' : tes1,
            }
    return render(request, 'pay/serve5.html', context)

def Serviced6(request):
    tes1 = Services.objects.filter(Service_type__contains='Universidades')
    context = {
            'tes1' : tes1,
            }
    return render(request, 'pay/serve6.html', context)



def delete(request, id = None):
    instance = get_object_or_404(Coupons, id = id)
    instance.delete()
    return HttpResponseRedirect(reverse('pay:Coupon'))

def update(request, id = None): 
    instance = get_object_or_404(Coupons, id = id)
    form = CouponForm(request.POST or None, instance = instance)
    if form.is_valid():
	instance = form.save(commit=False)
	instance.save()
        return HttpResponseRedirect(reverse('pay:Coupon'))
    context = {"instance" : instance, "form" : form}
    return render(request, 'pay/Cop2.html', context)



def index(request):
    user1 = User.objects.all()
    Trans = Transaction.objects.all()
    context = {
            'user1' : user1,
            'Trans' : Trans,
            }
    return render(request, 'pay/index.html',context)

def feedback(request):
    sd = User.objects.all()
    return render(request, 'pay/feed.html', {'sd' : sd})


def Coupon(request):
    sd = Coupons.objects.all()
    if request.method == 'POST':
        form = CouponForm(request.POST)
        if form.is_valid():
	    chargeT = form.save(commit=False)
	    chargeT.user = request.user
            chargeT.save()
            return HttpResponseRedirect(reverse('pay:Coupon'))
    else:
        form = CouponForm()
    return render(request, 'pay/Cop.html', {'sd' : sd, 'form' : form})


def Transactioning(request):
    tes2 = Transaction.objects.all()
    tes1 = Transaction.objects.count()
    context = {
               'tes2' : tes2,
               'tes1' : tes1,
               }
    return render(request, 'pay/zero.html',context)


def Transaction1(request):
    tes2 = Transaction.objects.filter(Description__contains='Cashing').count()
    tes44 = Transaction.objects.filter(Description__contains='Cashing')
    context = {
               'tes2' : tes2,
               'tes44' : tes44,
               }
    return render(request, 'pay/first.html', context)

def Transaction2(request):
    tes3 = Transaction.objects.filter(Description__contains='Bill').count()
    tes32 = Transaction.objects.filter(Description__contains='Bill')
    context = {
               'tes3' : tes3,
               'tes32' : tes32,
               }
    return render(request, 'pay/second.html', context)

def Transaction3(request):
    tes4 = Transaction.objects.filter(Description__contains='Friend').count()
    tes45 = Transaction.objects.filter(Description__contains='Friend')
    context = {
               'tes4' : tes4,
               'tes45' : tes45,
               }
    return render(request, 'pay/third.html', context)


def Transaction4(request):
    tes5 = Transaction.objects.filter(Description__contains='Purchase').count()
    tes56 = Transaction.objects.filter(Description__contains='Purchase')
    context = { 
               'tes5' : tes5,
               'tes56' : tes56,
               }
    return render(request, 'pay/forth.html', context)


def home(request):
    data = [
       ['Date','Users'],
       ['2018-09-22', 2],
       ['2018-09-23', 0],
       ['2018-09-24', 0],
       ['2018-09-25', 0],
       ['2018-09-26', 0],
       ['2018-09-27', 0],
       ['2018-09-28', 0],
       ['2018-09-29', 1],
       ]
    data2 = [
            ['Date', 'No.of Transactions'],
            ['22-09-22', 6 ],
            ['22-09-23', 0 ],
            ['22-09-24', 0 ],
            ['22-09-25', 1],
            ]
    data3 = [
            ['Date', 'Active Users'],
            ['22-09-22', 2 ],
            ['22-09-23', 0 ],
            ['22-09-24', 0 ],
            ['22-09-25', 1],
            ]
    tes = User.objects.count()
    tes99 = User.objects.all()
    tes1 = Transaction.objects.count()
    tes12 = Transaction.objects.all()
    tes123 = Transaction.objects.annotate(Sum('Amount'))
    tes2 = Transaction.objects.filter(Description__contains='Cashing').count()
    tes44 = Transaction.objects.filter(Description__contains='Cashing')
    tes3 = Transaction.objects.filter(Description__contains='Bill').count()
    tes32 = Transaction.objects.filter(Description__contains='Bill')
    tes4 = Transaction.objects.filter(Description__contains='Friend').count()
    tes45 = Transaction.objects.filter(Description__contains='Friend')
    tes5 = Transaction.objects.filter(Description__contains='Purchase').count()
    tes56 = Transaction.objects.filter(Description__contains='Purchase')
    data_source = SimpleDataSource(data=data)
    data_source2 = SimpleDataSource(data=data2)
    data_source3 = SimpleDataSource(data=data3)
    chart = ColumnChart(data_source)
    chart2 = ColumnChart(data_source2)
    chart3 = ColumnChart(data_source3)
    context = {
               'tes' : tes,
               'tes123' : tes123,
               'tes99' : tes99,
               'chart2' : chart2,
               'chart' : chart,
               'chart3' : chart3,
               'tes1' : tes1,
               'tes2' : tes2,
               'tes3' : tes3,
               'tes4' : tes4,
               'tes5' : tes5,
               'tes32' : tes32,
               'tes44' : tes44,
               'tes45' : tes45,
               'tes56' : tes56,
               'tes12' : tes12,
               }
    return render(request, 'pay/home.html',context)


def Block(request ,id = None):
    sd = User.objects.filter(id = id).update(status = True)
    return HttpResponseRedirect(reverse('pay:index'))

def UnBlock(request, id = None):
    sd = User.objects.filter(id = id).update(status = False)
    return HttpResponseRedirect(reverse('pay:index'))



def detail(request, id = None):
    users = User.objects.all().filter(id = id)
    trans = Transaction.objects.all().filter(user_id = id)
    trans1 = Transaction.objects.all().filter(user_id = id, Description__contains = 'Bill')
    trans2 = Transaction.objects.all().filter(user_id = id, Description__contains = 'Purchase')
    trans3 = Transaction.objects.all().filter(user_id = id, Description__contains = 'Cashin')
    trans4 = Transaction.objects.all().filter(user_id = id, Description__contains = 'Friend')
    context = {
            'users' : users,
            'trans' : trans,
            'trans1' : trans1,
            'trans4' : trans4,
            'trans3' : trans3,
            'trans2' : trans2
            } 
    return render(request, 'pay/detail.html', context)




"""
def submit(request, year, month, day, year2, month2, day2):
    s = year + "-" +  month + "-" +day
    d = year2 + "-" + month2 + "-" + day2
    find = User.objects.filter(SignUp_Date__gte=s, SignUp_Date__lte=d)
    return render(request, 'pay/submit.html', {'find' : find})



def submit2(request):
    if request.method == 'POST':
        form = AuthorForm(request.POST)
        if form.is_valid():
	    chargeT = form.save(commit=False)
	    chargeT.user = request.user
            chargeT.save()
            return HttpResponseRedirect(reverse('pay:index'))
    else:
        form = AuthorForm()
    return render(request, 'pay/Company.html', {'form': form})

"""


