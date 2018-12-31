# Class to represent a given image that will be used to train the detector

class Image:
    def __init__(self, name, detection_image):
        self.name = name
        self.detection_image = detection_image
