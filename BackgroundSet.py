import os

from Background import Background
from PIL import Image

# Class that represents the whole set of background images in the application

class BackgroundSet:
    def __init__(self, directory):
        self.directory = directory
        self.number_of_backgrounds = 0
        self.background_images = []

    def make_background_set(self):
        for filename in os.listdir(self.directory):
            image_path = self.directory + filename
            open_image = Background(filename, Image.open(image_path, 'r'))
            self.background_images.append(open_image)
            self.number_of_backgrounds += 1

    def iterate_backgrounds(self):
        for background in self.background_images:
            print("Name on object: ", background.name)
            print("Image width:    ", background.width)
            print("Image height:   ", background.height)
