# CS 121 CS 1203 Group 1

## submitted by:
|Name|Username|
|----|--------|
|Buenavista, Christian Paolo|[Github Link](https://github.com/PaoloBuenavista)|
|Fanoga, Haidie|[Github Link](https://github.com/Haidonuts)|
|Hepuller, Kate Nicole|[Github Link](https://github.com/Hepuller01)|
|Mortel, Cindy Pauleen|[Github Link](https://github.com/cindymortel)|

A lab activity in ***Python***.
```python
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
```
Input options 1 to 4 to do the see the ```sound_range```, to ```tune``` the instrument, to ```play``` the instrument, and to go back to the ```Main Menu```.

```python
    def get_sound_range(self):
            print("The sound range of the Guitar is approximately 82 Hz to 400 Hz. ")
            time.sleep(2)
            
```
The program will print out the ```sound_range``` of the instrument

```python
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
```       
 the program will show if the instrument is tuned or untuned, it will ask you if you want to tune it.
```python
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
```

To play an instrument, use the ```play_sound``` method. If the instrument is out of tune, it will produce an unpleasant sound. If it is properly tuned, it will play a pleasant, harmonious sound.
