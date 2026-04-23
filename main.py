import obspython as obs
import math, time

def script_description():
  return """<center><h2>Stream Length Logging</h2></center>
            <p>A simple script that will log a start and end timestamp anytime
            streaming is started, along with the website/profile used for the
            stream.</p>"""

def script_properties():
    props = obs.obs_properties_create()

def on_event(event):
    if event == obs.OBS_FRONTEND_EVENT_STREAMING_STARTING:
        raise Exception("Triggered when stream starts")
    if event == obs.OBS_FRONTEND_EVENT_STREAMING_STOPPING: # or STOPPED
        raise Exception("Triggered when stream is stopping")

def script_load(settings):
    obs.obs_frontend_add_event_callback(on_event)

def script_unload():
    return

def script_save():
    return

def script_tick(seconds: int):
    return

def script_unload():
    pass