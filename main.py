"""
OBS LOGGING SCRIPT - TheGenieA1

This script will automatically log every session of the stream being started to
a local database table.

Add to OBS as a script to run in the OBS Python enviroment

"""

import math
import time
import sqlite3
import os

from datetime import datetime

import obspython as obs


class StreamLogger:
    """
    This class allows the creation of a logger that records session data to a database table.
    Log_session() opens and creates the entry and Close() closes the database
    """

    def __init__(self, db_name: str) -> None:
        self.connection: sqlite3.Connection = sqlite3.connect(db_name)
        self.create_table()

    def create_table(self) -> None:
        with self.connection:

            self.connection.execute("""CREATE TABLE IF NOT EXISTS "Broadcasts" (
                id INTEGER PRIMARY KEY,
                session_id TEXT NOT NULL,
                timestamp TEXT NOT NULL,
                test_flag INTEGER NOT NULL DEFAULT 0,
                website TEXT NOT NULL,
            )
            """)

    def log_session(self,
                    session_id: str,
                    website: str,
                    test_flag: bool = False):
        timestamp = datetime.now().isoformat()
        with self.connection:
            self.connection.execute("""INSERT INTO "Broadcasts" (
                session_id
                timestamp
                test_flag
                website
            )
            VALUES (?, ?, ?, ?, ?)
            """, (session_id, timestamp, test_flag, website))
    def close(self):
        self.connection.close()

def script_description():
    return """<center><h2>Stream Length Logging</h2></center>
            <p>A simple script that will log a start and end timestamp anytime
            streaming is started, along with the website/profile used for the
            stream.</p>"""


def script_properties():
    props = obs.obs_properties_create()


def on_event(event: obs.FrontendEvent):
    if event == obs.OBS_FRONTEND_EVENT_STREAMING_STARTING:
        raise Exception("Triggered when stream starts")
    if event == obs.OBS_FRONTEND_EVENT_STREAMING_STOPPING:  # or STOPPED
        raise Exception("Triggered when stream is stopping")


def script_load(settings: obs.Settings):
    obs.obs_frontend_add_event_callback(on_event)


def script_unload():
    return


def script_save():
    return

def script_tick(seconds: int):
    return

def script_unload():
    pass
