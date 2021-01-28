from PIL import Image

hot = Image.open('sources/Hot.jpg')
medium = Image.open('sources/caution.jpg')
okay = Image.open('sources/safe.jpg')
temp = 37.00
setup = True


def tempcheck():
    if temp <= 37.40:
        okay.show()
    if 37.50 <= temp <= 37.99:
        medium.show()
    if temp >= 38.0:
        hot.show()
