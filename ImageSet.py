import os

from DetectImage import DetectImage
from PIL import Image

# Class that represents the whole set of detection images in the application

class ImageSet:
    def __init__(self, directory):
        self.directory = directory
        self.number_of_images = 0
        self.detection_images = []

    def make_image_set(self):
        for filename in os.listdir(self.directory):
            image_path = self.directory + filename
            open_image = DetectImage(filename, Image.open(image_path, 'r'))
            self.detection_images.append(open_image)
            self.number_of_images += 1

    def iterate_detect_images(self):
        for detect_image in self.detection_images:
            print("Name on object: ", detect_image.name)
            print("Image width:    ", detect_image.width)
            print("Image height:   ", detect_image.height)