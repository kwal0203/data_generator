# Class to represent a given image that will be used to train the detector

class DetectImage:
    def __init__(self, name, detection_image):
        self.name = name
        self.detection_image = detection_image
        self.width = detection_image.size[0]
        self.height = detection_image.size[1]