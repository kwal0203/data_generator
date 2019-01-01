import os
import pandas as pd

from random import randint

# Class responsible for: calculating where to paste detection images on
# background, pasting images on backgrounds, formatting and outputting CSV
# files

class DataGenerator:
    def __init__(self, image_set, background_set, num_samples, cutoff):
        self.image_set = image_set
        self.background_set = background_set
        self.num_samples = num_samples
        self.csv_lines = []
        self.cutoff = cutoff * num_samples

    def process_images(self):
        print("----- PROCESSING IMAGES -----")
        sample_no = 1

        train_dir = "output/train/"
        test_dir = "output/test/"
        if not os.path.exists(train_dir):
            os.makedirs(train_dir)
        if not os.path.exists(test_dir):
            os.makedirs(test_dir)

        for background in self.background_set.background_images:
            for i in range(0, self.num_samples):
                tmp_back = background.background_image.copy()
                new_name = str(sample_no) + ".png"
                for image in self.image_set.detection_images:
                    r_width = tmp_back.width - image.width
                    r_height = tmp_back.height - image.height

                    width_offset = randint(0, r_width)
                    height_offset = randint(0, r_height)
                    offset = (width_offset, height_offset)

                    # Place card in offset position
                    tmp_back.paste(image.detection_image, offset)

                    # x_min, y_min, x_max, y_max
                    x_min = offset[0]
                    y_min = offset[1]
                    x_max = x_min + image.width
                    y_max = y_min + image.height
                    class_name = image.name[0:-4]
                    self.csv_lines.append((new_name, tmp_back.width,
                                             tmp_back.height, class_name,
                                             x_min, y_min, x_max, y_max))

                # Name and save the new image (background image remains
                # unchanged)
                print("Processing Sample ", sample_no)

                if sample_no <= self.cutoff:
                    tmp_back.save("output/train/" + new_name)
                else:
                    tmp_back.save("output/test/" + new_name)
                sample_no += 1

    def generate_csv(self):
        tmp_cutoff = int(self.cutoff)

        train_list = self.csv_lines[0:tmp_cutoff]
        test_list = self.csv_lines[tmp_cutoff:self.num_samples]

        column_name = ['filename', 'width', 'height', 'class', 'xmin', 'ymin', 'xmax', 'ymax']
        train_df = pd.DataFrame(train_list, columns=column_name)
        test_df = pd.DataFrame(test_list, columns=column_name)

        train_df.to_csv('output/train_labels.csv', index=None)
        test_df.to_csv('output/test_labels.csv', index=None)
