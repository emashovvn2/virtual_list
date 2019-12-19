from django.shortcuts import render
from .models import Vm

# Create your views here.
def vm_list(request):
    vms = posts = Vm.objects.all()
    return render(request, 'vm_list/vm_list.html', {'vms': vms})
