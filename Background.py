# Class to represent a given background image that detection images will be
# pasted onto

class Background:
    def __init__(self, name, background_image):
        self.name = name
        self.background_image = background_image
