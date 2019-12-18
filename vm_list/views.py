from django.shortcuts import render
from .models import vm

# Create your views here.
def vm_list(request):
    vms = posts = vm.objects.all()
    return render(request, 'vm_list/vm_list.html', {{'vms': vms}})
