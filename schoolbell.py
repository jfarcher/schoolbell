#!/usr/bin/env python

import sys
import time
import socket
from threading import Thread        
from soco import SoCo
import paho.mqtt.client as mqtt

# Add Sonos device IP address here - scanning will be added at a later date
device = '192.168.1.150'
sound = "schoolbell.mp3"





def play(device, queueable_item):
    sonos = SoCo(device)
    track = sonos.get_current_track_info()
    initial_playlist_position = int(track["playlist_position"]) - 1
    
    initial_track_position = (track["position"])
    initial_state = sonos.get_current_transport_info().get("current_transport_state")
    initial_volume = sonos.volume
    sonos.volume=3
    sonos.play_uri(uri=queueable_item, meta='')
    time.sleep( 2 )
    sonos.volume=initial_volume    
    sonos.play_from_queue(initial_playlist_position)
    sonos.seek(initial_track_position)
    if initial_state != 'PLAYING':
                sonos.pause()

play(device,sound)

