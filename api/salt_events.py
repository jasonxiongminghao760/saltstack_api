import salt.utils.event

event = salt.utils.event.MasterEvent('/var/run/salt/master')





for item in event.iter_events(full=True):
    print(item)

