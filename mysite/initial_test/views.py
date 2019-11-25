from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from . import util

# Create your views here.
def initial_test(request):
    bluetooth_devices = util.getBluetoothDevices()
    maps = util.getMaps()
    mist_devices = util.getMistDevices()
    virtual_beacons = util.getVirtualBeacons()
    return render(request, 'initial_test.html', {'bluetooth_devices': bluetooth_devices, 'maps': maps, 'mist_devices': mist_devices, 'virtual_beacons': virtual_beacons})
