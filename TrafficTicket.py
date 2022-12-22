# A simple project to check if you have fines or not
import emoji

speed = int(input('Enter your speed: '))
speed_full = 80
if speed <= speed_full:
    print(emoji.emojize('You do not have fines :thumbs_up:'))
elif speed > speed_full and speed <= speed_full + 10:
    print(emoji.emojize('Your fine is cheap :neutral_face:'))
elif speed >= speed_full + 11 and speed <= speed_full + 20:
    print(emoji.emojize('Your fine is expensive :cold_face:'))
elif speed > speed_full + 20:
    print(emoji.emojize(
        "Bro you lost your driver license :face_with_raised_eyebrow:, please pay more attention when you drive "))
