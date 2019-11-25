import requests
import datetime

ND_SITE_ID = "a0747c5a-0720-11e6-bad6-02e208b2d34f"
APARTMENT_SITE_ID = '7fe1f1f2-12a5-4daa-9766-cfe2eb76f6c9'
ND_MAP_ID = 'a530474e-f7cd-4267-afa6-0fd5387b34c8'
APARTMENT_MAP_ID = '84f4ff94-6593-408a-91dd-bc5b850a266a'

AUTH_TOKEN = 'Token uJJ834bA1zHelDVpe9xqdHtSEXXv2K4PEZvW1hITweHNyuUa0Z98aGdWfdp0TRVCctgjLBWqD5r8lAvdyQE0a0R7rf0g59ag'

# returns all the blutooth devices being picked up by the mist device given a certain site and map
# the datetime object holds all info down to microseconds
def getBluetoothDevices():
    response = requests.get('https://api.mist.com/api/v1/sites/' + ND_SITE_ID + '/stats/maps/' + ND_MAP_ID + '/discovered_assets', headers={'Authorization': AUTH_TOKEN})
    response = response.json()
    useful = {}
    for device in response:
        curr_mac = device['mac']
        useful[curr_mac] = {}
        useful[curr_mac]['x'] = device['x']
        useful[curr_mac]['y'] = device['y']
        useful[curr_mac]['map_id'] = device['map_id']
        date = datetime.datetime.fromtimestamp(device['last_seen'])
        useful[curr_mac]['last_seen'] = date

    return useful

# returns all maps that are associated with a certain site
# ppm property can be used alongside x and y locations returned from other methods to find a physical location where someone is as opposed to just their pixel location
def getMaps():
    response = requests.get('https://api.mist.com/api/v1/sites/' + ND_SITE_ID + '/maps', headers={'Authorization': AUTH_TOKEN}).json()
    useful = {}
    for map in response:
        curr_map = map['id']
        useful[curr_map] = {}
        useful[curr_map]['ppm'] = map['ppm']
        useful[curr_map]['width_m'] = map['width_m']
        useful[curr_map]['height_m'] = map['height_m']

    return useful

# returns all mist devices that are at a certain site
def getMistDevices():
    response = requests.get('https://api.mist.com/api/v1/sites/' + ND_SITE_ID + '/devices', headers={'Authorization': AUTH_TOKEN})
    response = response.json()
    useful = {}
    for device in response:
        curr_mac = device['mac']
        useful[curr_mac] = {}
        useful[curr_mac]['x'] = device['x']
        useful[curr_mac]['y'] = device['y']
        useful[curr_mac]['map_id'] = device['map_id']
        useful[curr_mac]['name'] = device['name']

    return useful

# returns all virtual beacons associated with a certain site
def getVirtualBeacons():
    response = requests.get('https://api.mist.com/api/v1/sites/' + ND_SITE_ID + '/vbeacons', headers={'Authorization': AUTH_TOKEN})
    response = response.json()
    useful = {}
    for vbeacon in response:
        curr_vbeacon = vbeacon['id']
        useful[curr_vbeacon] = {}
        useful[curr_vbeacon]['x'] = vbeacon['x']
        useful[curr_vbeacon]['y'] = vbeacon['y']
        useful[curr_vbeacon]['name'] = vbeacon['name']
        useful[curr_vbeacon]['map_id'] = vbeacon['map_id']

    return useful
