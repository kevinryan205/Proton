#First of all you have to make an instance of the Myjdapi class and set your APPKey:
import myjdapi
from proton import restart_progs
from datetime import datetime


def check_jdownloader():
    jd=myjdapi.Myjdapi()
    jd.set_app_key("EXAMPLE")

    """
    After that you can connect.
    Now you can only connect using username and password.
    This is a problem because you can't remember the session between executions
    for this reason i will add a way to "connect" which is actually not connecting,
    but adding the old tokens you saved. This way you can use this between executions
    as long as your tokens are still valid without saving the username and password.
    """

    jd.connect("kevinryan205@gmail.com","annabelle0")

    # When connecting it gets the devices also, so you can use them but if you want to
    # gather the devices available in my.jdownloader later you can do it like this

    jd.update_devices()

    # Now you are ready to do actions with devices. To use a device you get it like this:
    device=jd.get_device("JDownloader@Kevin")
    # The parameter by default is the device name, but you can also use the device_id.
    # device=jd.get_device(device_id="43434")

    # After that you can use the different API functions.
    # For example i want to get the packages of the downloads list, the API has a function under downloads called queryPackages,
    # you can use it with this library like this:
    qps = device.downloads.query_packages([{
                    # "bytesLoaded" : True,
                    # "bytesTotal" : True,
                    # "comment" : False,
                    # "enabled" : True,
                    # "eta" : True,
                    # "priority" : False,
                    # "finished" : True,
                    "running" : True,
                    # "speed" : True,
                    "status" : True,
                    # "childCount" : True,
                    # "hosts" : True,
                    # "saveTo" : True,
                    # "maxResults" : -1,
                    # "startAt" : 0,
                }])
    print(qps)
    restarted = False
    for d in qps:
        for key,val in d.items():
            if key == 'status':  
                if '509 Bandwidth Limit Exceeded' in val:
                    print('restart_progs')
                    restart_progs()
                    restarted = True
                    break
        if restarted:
            break

    if restarted:
        print(f'Programs Restarted at {datetime.now()}')