import optparse
from ImageSet import ImageSet
from BackgroundSet import BackgroundSet
from DataGenerator import DataGenerator

if __name__ == '__main__':
    # 1. Read command line arguments
    parser = optparse.OptionParser()
    parser.add_option("-i", "--images", dest="image_dir", type="string",
                      help=("the maximum number of characters that can be "
                            "output to string fields [default: %default]"))
    parser.add_option("-b", "--backgrounds", dest="background_dir",
                      help=("the format used for outputting numbers "
                            "[default: %default]"))
    parser.set_defaults(test_dir="None", train_dir="None")
    opts, args = parser.parse_args()

    # 2. Read detection images
    image_set = ImageSet(opts.image_dir)
    print("Image directory: /" + image_set.directory)

    # 3. Read background images
    background_set = BackgroundSet(opts.background_dir)
    print("Background directory: /" + background_set.directory)

    # 4. Pass detection and background images to DataGenerator
    data_generator = DataGenerator(image_set, background_set)
    data_generator.process_images()

    # 5. Finish
    print("Program successfully finished")