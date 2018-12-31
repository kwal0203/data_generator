from Image import Image

# Class that represents the whole set of detection images in the application

class ImageSet:
    def __init__(self, directory):
        self.directory = directory
        self.number_of_images = 0
