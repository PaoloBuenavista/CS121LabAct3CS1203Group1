from abc import ABC, abstractmethod

class instruments(ABC):
    def __init__(instrument,type,brand,range):
        instrument.type = type
        instrument.brand = brand
        instrument.range = range
        instrument.is_playing = False
        instrument.tune = False
       
    #to play the sound
    def play_sound(instrument):
        if not instrument.is_playing:
            instrument.is_playing = True
            print("The {instruments.type} is now playing. ")
        else: 
            print("The {instrument.type} is already playing.")

    #check if the instrument is out of tune
    def tune_instrument(instrument):
        if not instrument.tune:
            tune_instrument = True
            print("The {instrument.type} is on tune. ")
        else:
            print("The {instrument.type} is out of tune. ")  


class guitar(instrument):
    def __init__(instrument, type, brand, sound_range=0):