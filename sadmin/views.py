from django.shortcuts import render,redirect

from django.contrib import messages
from django.contrib.auth.models import User, auth
from startpage.models import Muser,Raja,RentVehichle

# Create your views here.
def checkAdmin(id):
    user = User.objects.get(id = id)
    muser = Muser.objects.get(muser = user)
    if muser.status == 1:
        return False
    else:
        return True

def adminpage(request):
    if not request.user.is_authenticated:
        return redirect('/login')
    else:
        if checkAdmin(request.user.id):
            return redirect('/login')
        m = RentVehichle.objects.all().order_by()[::-1] 
        context = {'med':m}
        return render(request,'shome.html',context)

def shopDetails(request, shop_id):
    if not request.user.is_authenticated:
        return redirect('/music/login')
    else:
        if checkAdmin(request.user.id):
            return redirect('/music/login')

        rent = RentVehichle.objects.get(id=shop_id)
        return render(request, 'shopDetails.html',{'shop':rent})

def final(request):
    if request.method == 'POST':
        aid = request.POST.get('aid')
        approve = request.POST.get('approve')
        reject = request.POST.get('reject')
        oname = RentVehichle.objects.get(id=aid)
        if approve==None:
            print(reject)
            oname.status = -1

            oname.save()
            # rejectMail(mail bhej dena yaha se)
            
        elif reject==None:
            print(approve)
            oname.status = 1
            oname.save()
            #acceptMail(mail bhej dena yaha se)
    return redirect('adminhome')
