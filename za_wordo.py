import os

f = ('lol.txt')
if os.path.exists(f):
    while True:
        try:
            os.rename(f, f)
            print('yes')
        except:
            print("yeah no")
