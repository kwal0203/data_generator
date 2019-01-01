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
    parser.set_defaults(image_dir="None", background_dir="None")
    opts, args = parser.parse_args()

    print("----- ARG TESTING -----")
    print("Detect dir:     ", opts.image_dir)
    print("Background dir: ", opts.background_dir)
    print("----- END ARG TESTING -----")
    print("\n")

    # 2. Read detection images
    image_set = ImageSet(opts.image_dir)
    image_set.make_image_set()
    image_set.iterate_detect_images()

    # 3. Read background images
    background_set = BackgroundSet(opts.background_dir)
    background_set.make_background_set()
    background_set.iterate_backgrounds()

    # 4. Pass detection and background images to DataGenerator
    # data_generator = DataGenerator(image_set, background_set)
    # data_generator.process_images()

    # 5. Finish
    print("Program successfully finished")
