from abc import ABC, abstractmethod
import pygame, sys, time
import time
import random
from pathlib import Path
pygame.mixer.init()
sound_folder = Path("sounds")

List_of_drum_sounds = [
    sound_folder / "drum_1.mp3",
    sound_folder / "drum_2.mp3",
    sound_folder / "drum_3.mp3",
    sound_folder / "drum_4.mp3" 
]
List_of_guitar_solo = [
    sound_folder / "guitar_1.mp3",
    sound_folder / "guitar_2.mp3",
    sound_folder / "guitar_3.mp3",
    sound_folder / "guitar_4.mp3"
    
]    
List_of_piano_solo = [
    sound_folder / "piano_1.mp3",
    sound_folder / "piano_2.mp3",
    sound_folder / "piano_3.mp3",
    sound_folder / "piano_4.mp3"
    
]

List_of_xylophone_solo = [
    sound_folder / "xylophone_1.mp3",
    sound_folder / "xylophone_2.mp3",
    sound_folder / "xylophone_3.mp3",
    sound_folder / "xylophone_4.mp3"
]

class Musical_Instrument(ABC):
    def __init__(self,type,brand):
        self.type = type
        self.brand = brand
    
        
    def get_type(self):
        return self.type
    
    def get_brand(self):
        return self.brand
    
    @abstractmethod
    def play_sound(self):
        pass
    
    @abstractmethod
    def get_sound_range(self):
        pass
    
    @abstractmethod
    def tune_instrument(self):
        pass

class Guitar(Musical_Instrument):
    def __init__ (self,type,brand,first_string,second_string,third_string,fourth_string,fifth_string,sixth_string):
        super().__init__(type,brand)
        self.first_string = first_string
        self.second_string = second_string
        self.third_string = third_string
        self.fourth_string = fourth_string
        self.fifth_string = fifth_string
        self.sixth_string = sixth_string

        
    def get_sound_range(self):
            print("The sound range of the Guitar is approximately 82 Hz to 400 Hz. ")
            time.sleep(2)
            

    def tune_instrument(self):
        for string_name in ['first_string', 'second_string', 'third_string', 'fourth_string', 'fifth_string', 'sixth_string']:
            part = getattr(self, string_name)
            if not part:
                answer = input(f"The {string_name} is not tuned. Would you like to tune it? yes/no: ").strip().lower()
                if answer == "yes":
                    setattr(self, string_name, True)
                    print(f"Tuning {string_name} please wait a moment.", end = '', flush = True)
                    for i in range (5):
                        print('.', end = '', flush = True)
                        time.sleep(0.3)
                    time.sleep(1)
                    print(f" The {string_name} is now tuned.")
                    time.sleep(0.5)
                else:
                    time.sleep(0.5)
                    print(f"The {string_name} is still untuned.")
            else:
                print(f"The {string_name} is already in tune.")
                time.sleep(0.5)
        print("The Guitar is now tuned. You can now play the Guitar! ")
        time.sleep(0.5)
    
    def play_sound(self):
        play = input("Do you want to play the Guitar? yes/no: ").strip().lower()
        if play == "yes":
            parts = [self.first_string, self.second_string, self.third_string,
                    self.fourth_string, self.fifth_string, self.sixth_string]

            if all(parts):
                print("🎶 🎶 🎶  Playing Guitar  🎶 🎶 🎶")
                random_guitar = random.choice(List_of_guitar_solo)
                sound = pygame.mixer.Sound(random_guitar)
            else:
                print("Playing Guitar 🎶 (Some parts are untuned 😵‍💫)")
                sound = pygame.mixer.Sound(sound_folder / "ugly_guitar.mp3")

            channel = pygame.mixer.Channel(0)
            channel.play(sound)

            print("Press Enter to stop the sound manually...")
            time.sleep(0.5)
            input()
            channel.stop()

            if all(parts):
                print("Your guitar skills are good, keep it up!")
                time.sleep(0.5)
            else:
                print("Oof... That sounded unpleasant. Try tuning your Guitar!")
                time.sleep(0.5)

                    
            
class Drums(Musical_Instrument):
    def __init__ (self,type,brand,snare,bass,hihat,crash,toms,ride):
        super().__init__(type,brand)
        self.snare = snare
        self.bass = bass 
        self.hihat = hihat 
        self.crash = crash
        self.toms = toms
        self.ride = ride 
        
    def get_sound_range(self):
        print(f"The sound range of the Drums is approximately 50 Hz to 250 Hz. ")
        time.sleep(2)
            
    def tune_instrument(self):
        for part_name in ['snare', 'bass', 'toms', 'hihat', 'crash', 'ride']:
            part = getattr(self, part_name)
            if not part:
                answer = input(f"The {part_name} is not tuned. Would you like to tune it? yes/no: ").strip().lower()
                if answer == "yes":
                    setattr(self, part_name, True)
                    print(f"Tuning {part_name} please wait a moment.", end = '', flush = True)
                    for i in range (5):
                        print('.', end = '', flush = True)
                        time.sleep(0.5)
                    time.sleep(1)
                    print(f" The {part_name} is now tuned.")
                    time.sleep(0.2)
                
                else:
                    time.sleep(0.5)
                    print(f"The {part_name} is still untuned.")
            else:
                print(f"The {part_name} is already in tune.")
                time.sleep(0.5)
        print("The drums is now tuned. You can now play the drums! ")
        time.sleep(0.5)
        
    
    def play_sound(self):
        play = input("Do you want to play the drums? yes/no: ").strip().lower()
        if play == "yes":
            parts = [self.snare, self.bass, self.toms, self.hihat, self.crash, self.ride]
            if all(parts):
                print("🎶 🎶 🎶  Playing Drums  🎶 🎶 🎶")
                random_drum = random.choice(List_of_drum_sounds)
                sound = pygame.mixer.Sound(random_drum)
            else:
                print("Playing Drums 🎶 (Some parts are untuned 😵‍💫)")
                sound = pygame.mixer.Sound(sound_folder / "ugly_drum.mp3")

            channel = pygame.mixer.Channel(1)
            channel.play(sound)

            input("Press Enter to stop the sound manually... ")
            time.sleep(0.5)
            channel.stop()

            if all(parts):
                print("Your drumming skills are good, keep it up!")
                time.sleep(0.5)
            else:
                print("Oof... That sounded rough. Try tuning your drums!")
                time.sleep(0.5)
        else:
            print("Okay, maybe next time.")

class Piano(Musical_Instrument):
    def __init__(self, type, brand, keys_tuned=88):
        super().__init__(type, brand)
        self.keys_tuned = False

    def get_sound_range(self):
        print(f"The sound range of the Piano is approximately 27.5 Hz to 4186 Hz.")
        time.sleep(2)

    def tune_instrument(self):
        answer = input("Would you like to tune the piano? (This might take a while!) yes/no: ").strip().lower()
        if answer == "yes":
            print("Tuning the piano, please wait patiently.", end = '', flush = True)
            for i in range(5):
                print('.', end = '', flush = True)
                time.sleep(0.5) 
            time.sleep(1)
            self.keys_tuned = 88
            print(" The piano is now perfectly tuned!")
        else:
            print("Okay, the piano remains as it is.")

    def play_sound(self):
        answer = input("Ready to play the piano? yes/no: ").strip().lower()
        if answer == "yes":
            notes = (self.keys_tuned)
            if self.keys_tuned == 88:
                print("Playing a beautiful melody 🎼...")
                random_piano = random.choice(List_of_piano_solo)
                sound = pygame.mixer.Sound(random_piano)
            else:
                print("Playing Piano 🎶 (Some parts are untuned 😵‍💫)")
                sound = pygame.mixer.Sound(sound_folder / "ugly_piano.mp3")

            channel = pygame.mixer.Channel(2) 
            channel.play(sound)

            input("Press Enter to stop the piano manually... ")
            channel.stop()

            if self.keys_tuned == 88:
                print("The performance ends with a flourish! ✨")
            else:
                print("Oof... That sounded horrible. Try tuning your Piano!")
        else:
            print("Alright, perhaps another time.")

class Xylophone(Musical_Instrument):
    def __init__(self, type, brand, C=False, D=False, E=False, F=False, G=False):
        super().__init__(type, brand)
        self.C = C
        self.D = D
        self.E = E
        self.F = F
        self.G = G

    def get_sound_range(self):
        print("The average sound range of the Xylophone is approximately 349 to 4186 Hz.")
        time.sleep(2)

    def tune_instrument(self):
        for key in ['C', 'D', 'E', 'F', 'G']:
            if not getattr(self, key):
                answer = input(f"Key {key} is not tuned. Would you like to tune it? yes/no: ").strip().lower()
                if answer == "yes":
                    setattr(self, key, True)
                    print(f"Tuning key {key}, please wait.", end = '', flush = True)
                    for i in range(5):
                        print('.', end = '', flush = True)
                        time.sleep(0.5)
                    time.sleep(1)
                    print(f" Key {key} is now tuned.")
                    time.sleep(0.2)

                else:
                    print(f"Key {key} remains untuned.")
                time.sleep(0.5)
            else:
                print(f"Key {key} is already tuned.")
                time.sleep(0.3)
        print("Xylophone tuning complete.")

    def play_sound(self):
        answer = input("Do you want to play the xylophone? yes/no: ").strip().lower()
        if answer == "yes":
            notes = {self.C, self.D, self.E, self.F, self.G}
            if all(notes):
                print("Playing xylophone 🎵")
                random_xylo = random.choice(List_of_xylophone_solo)
                sound = pygame.mixer.Sound(random_xylo)
            else:
                print("Playing Xylophone 🎶 (Some parts are untuned 😵‍💫)")
                sound = pygame.mixer.Sound(sound_folder / "ugly_xylophone.mp3")

            channel = pygame.mixer.Channel(3)
            channel.play(sound)

            input("Press Enter to stop the xylophone manually... ")
            time.sleep(0.5)
            channel.stop()

            if all(notes):
                print("Performance complete. Great job!")
                time.sleep(0.5)
            else:
                print("Oof... That sounded ugly. Try tuning your Xylophone!")
                time.sleep(0.5)
        else:
            print("Okay! Maybe later.")
   

def main():
    def get_valid_input(prompt, valid_choices):
        while True:
            choice = input(prompt).strip()
            if choice in valid_choices:
                return choice
            else:
                print("    Invalid input. Please try again.")

    while True:
        print(r""" 
      +~~~+~~~+~~~+~~~+~~~+~~~+~~~+~~~+~~~+~~~+~~~+~~~+~~~+~~~+~~~+                        
     ♪              Welcome to the Instrument Gallery             ♪               
    ♫                           Main Menu                          ♫
   ♫ ♪                🤔 What do you want to do?🤔                ♪ ♫         
    ♫                  1 - 🎶 pick an instrument🎶                 ♫       
     ♪                      2 - 🥺 Leave 🥺                       ♪
      +~~~+~~~+~~~+~~~+~~~+~~~+~~~+~~~+~~~+~~~+~~~+~~~+~~~+~~~+~~~+        """)
        choice = input("    Enter your choice (1/2): ").strip()
        time.sleep(0.5)

        if choice == "1":
            print(r""" 
      +~~~+~~~+~~~+~~~+~~~+~~~+~~~+~~~+~~~+~~~+~~~+~~~+~~~+~~~+~~~+                        
     ♪             What instrument do you want to play?           ♪               
    ♫                        1 - 🎸Guitar🎸                        ♫
   ♫ ♪                       2 - 🥁Drums🥁                        ♪ ♫         
    ♫                        3 - 🎹Piano🎹                         ♫       
     ♪                       4 - 🎼Xylophone🎼                    ♪
      +~~~+~~~+~~~+~~~+~~~+~~~+~~~+~~~+~~~+~~~+~~~+~~~+~~~+~~~+~~~+        """)
            instrument_choice = input("    Choose an instrument (1/2/3/4): ")
            time.sleep(0.5)

            if instrument_choice == "1":
                first_string = random.choice([True, False])
                second_string = random.choice([True, False])
                third_string = random.choice([True, False])
                fourth_string = random.choice([True, False])
                fifth_string = random.choice([True, False])
                sixth_string = random.choice([True, False])
                guitar = Guitar("chordophone", "Fender", first_string, second_string, third_string, fourth_string, fifth_string, sixth_string)

                def status(is_tuned):
                    return "Tuned" if is_tuned else "Untuned"

                print("______________________________________________________________________________________________________________________________________________________________")
                print("\n⚠️  Note: your Guitar will sound ugly if not tuned properly! ⚠️ ")
                print(f"Tuning Status: first_string = {status(first_string)}, second_string = {status(second_string)}, third_string = {status(third_string)}, fourth_string = {status(fourth_string)}, fifth_string = {status(fifth_string)}, sixth_string = {status(sixth_string)}")
                print("______________________________________________________________________________________________________________________________________________________________")
                time.sleep(0.5)
                while True:            
                    print(r""" 
      +~~~+~~~+~~~+~~~+~~~+~~~+~~~+~~~+~~~+~~~+~~~+~~~+~~~+~~~+~~~+                        
     ♪           What would you like to do with the Guitar?        ♪               
    ♫                      1 - See Sound Range.                     ♫
   ♫ ♪                     2 - Tune the Guitar.                    ♪ ♫         
    ♫                      3 - Play the Guitar.                     ♫       
     ♪                     4 - Back to Main Menu                   ♪
      +~~~+~~~+~~~+~~~+~~~+~~~+~~~+~~~+~~~+~~~+~~~+~~~+~~~+~~~+~~~+        """)
                    Guitar_action = input("     Choose an action (1-4): ")
                    time.sleep(0.5)
                

                    if Guitar_action == "1":
                        guitar.get_sound_range()
                    elif Guitar_action == "2":
                        guitar.tune_instrument()
                    elif Guitar_action == "3":
                        guitar.play_sound()
                    elif Guitar_action == "4":
                        break
                    else:
                        print("    Invalid Input, Please Try Again.")


            elif instrument_choice == "2":
                snare = random.choice([True, False])
                bass = random.choice([True, False])
                toms = random.choice([True, False])
                hihat = True
                crash = True
                ride = True
                drum = Drums("Percussion", "Zildjian", snare, bass, hihat, crash, toms, ride)

                def status(is_tuned):
                    return "Tuned" if is_tuned else "Untuned"
                
                print("______________________________________________________________________________________________________________________________________________________________")
                print("\n⚠️  Note: your drum sounds will be ugly if not tuned properly! ⚠️ ")
                print(f"Tuning Status: snare = {status(snare)}, bass = {status(bass)}, toms = {status(toms)}, hihat = {status(hihat)}, crash = {status(crash)}, ride = {status(ride)}")
                print("______________________________________________________________________________________________________________________________________________________________")
                time.sleep(0.5)
                while True:
                    print(r""" 
      +~~~+~~~+~~~+~~~+~~~+~~~+~~~+~~~+~~~+~~~+~~~+~~~+~~~+~~~+~~~+                        
     ♪           What would you like to do with the drums?         ♪               
    ♫                     1 - See Sound Range.                      ♫
   ♫ ♪                    2 - Tune the Drums.                      ♪ ♫         
    ♫                     3 - Play the Drums.                       ♫       
     ♪                    4 - Back to Main Menu                    ♪
      +~~~+~~~+~~~+~~~+~~~+~~~+~~~+~~~+~~~+~~~+~~~+~~~+~~~+~~~+~~~+        """)
                    drum_action = input("     Choose an action (1-4): ")
                    time.sleep(0.5)

                    if drum_action == "1":
                        drum.get_sound_range()
                    elif drum_action == "2":
                        drum.tune_instrument()
                    elif drum_action == "3":
                        drum.play_sound()
                    elif drum_action == "4":
                        break
                    else:
                        print("    Invalid Input, Please Try Again.")

            elif instrument_choice == "3":
                piano = Piano("Keyboard", "Steinway")
                print("______________________________________________________________________________________________________________________________________________________________")
                print("\n⚠️  Your Piano is untuned! ⚠️ ")
                time.sleep(0.5)
                print("\n⚠️  Note: Your piano will sound unpleasant if it is not properly tuned.! ⚠️ ")
                print("______________________________________________________________________________________________________________________________________________________________")
                time.sleep(0.5)
                while True:
                    print(r""" 
      +~~~+~~~+~~~+~~~+~~~+~~~+~~~+~~~+~~~+~~~+~~~+~~~+~~~+~~~+~~~+                        
     ♪           What would you like to do with the Piano?         ♪               
    ♫                     1 - See Sound Range.                      ♫
   ♫ ♪                    2 - Tune the Piano.                      ♪ ♫         
    ♫                     3 - Play the Piano.                       ♫       
     ♪                    4 - Back to Main Menu                    ♪
      +~~~+~~~+~~~+~~~+~~~+~~~+~~~+~~~+~~~+~~~+~~~+~~~+~~~+~~~+~~~+        """)
                    piano_action = input("     Choose an action (1-4): ")
                    time.sleep(0.5)

                    if piano_action == "1":
                        piano.get_sound_range()
                    elif piano_action == "2":
                        piano.tune_instrument()
                    elif piano_action == "3":
                        piano.play_sound()
                    elif piano_action == "4":
                        break
                    else:
                        print("    Invalid Input, Please Try Again.")

            elif instrument_choice == "4":
                # Randomize tuning state for keys
                C = random.choice([True, False])
                D = random.choice([True, False])
                E = random.choice([True, False])
                F = random.choice([True, False])
                G = random.choice([True, False])
                xylophone = Xylophone("Percussion", "Yamaha", C, D, E, F, G)

                def key_status(is_tuned):
                    return "Tuned" if is_tuned else "Untuned"
                
                print("______________________________________________________________________________________________________________________________________________________________")
                print("⚠️  Xylophone keys might be out of tune! ⚠️")
                time.sleep(0.5)
                print(f"Tuning Status: C = {key_status(C)}, D = {key_status(D)}, E = {key_status(E)}, F = {key_status(F)}, G = {key_status(G)}")
                print("______________________________________________________________________________________________________________________________________________________________")
                time.sleep(0.5)

                while True:
                    print(r""" 
      +~~~+~~~+~~~+~~~+~~~+~~~+~~~+~~~+~~~+~~~+~~~+~~~+~~~+~~~+~~~+                        
     ♪        What would you like to do with the Xylophone?        ♪               
    ♫                     1 - See Sound Range.                      ♫
   ♫ ♪                    2 - Tune the Xylophone.                  ♪ ♫         
    ♫                     3 - Play the Xylophone.                   ♫       
     ♪                    4 - Back to Main Menu                    ♪
      +~~~+~~~+~~~+~~~+~~~+~~~+~~~+~~~+~~~+~~~+~~~+~~~+~~~+~~~+~~~+        """)
                    xylo_action = input("     Choose an action (1-4): ")
                    time.sleep(0.5)

                    if xylo_action == "1":
                        xylophone.get_sound_range()
                    elif xylo_action == "2":
                        xylophone.tune_instrument()
                    elif xylo_action == "3":
                        xylophone.play_sound()
                    elif xylo_action == "4":
                        break
                    else:
                        print("    Invalid Input, Please Try Again.")
                
            else:
                print("    Invalid Input, Please Try Again.")

        elif choice == "2":
            print("    Thank you for using Instrument Gallery, see you next time!♡")
            break
        
        else:
            print("    Invalid Input. Please Try Again.")

main()