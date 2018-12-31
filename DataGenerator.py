# Class responsible for: calculating where to paste detection images on
# background, pasting images on backgrounds, formatting and outputting CSV
# files

class DataGenerator:
    def __init__(self, image_set, background_set):
        self.image_set = image_set
        self.background_set = background_set

    def process_images(self):
        print("----- PROCESSING IMAGES -----")