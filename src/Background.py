
# Class to represent a given background image that detection images will be
# pasted onto

class Background:
    def __init__(self, name, background_image):
        self.name = name
        self.background_image = background_image
        self.width = background_image.size[0]
        self.height = background_image.size[1]
