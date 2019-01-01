import optparse
from src.ImageSet import ImageSet
from src.BackgroundSet import BackgroundSet
from src.DataGenerator import DataGenerator

if __name__ == '__main__':
    # 1. Read command line arguments
    parser = optparse.OptionParser()
    parser.add_option("-i", "--images", dest="image_dir", type="string",
                      help=("the maximum number of characters that can be "
                            "output to string fields [default: %default]"))
    parser.add_option("-b", "--backgrounds", dest="background_dir",
                      help=("the format used for outputting numbers "
                            "[default: %default]"))
    parser.add_option("-s", "--samples", dest="samples", type="int",
                      help="Total number of samples to be created")
    parser.add_option("-p", "--cutoff", dest="cutoff", type="float",
                      help="percentage of images in training set")
    parser.set_defaults(image_dir="images/", background_dir="backgrounds/", samples=2,
                        cutoff=0.8)
    opts, args = parser.parse_args()

    # 2. Read detection images
    image_set = ImageSet(opts.image_dir)
    image_set.make_image_set()

    # 3. Read background images
    background_set = BackgroundSet(opts.background_dir)
    background_set.make_background_set()

    # 4. Pass detection and background images to DataGenerator
    data_generator = DataGenerator(image_set, background_set, opts.samples,
                                   opts.cutoff)
    data_generator.process_images()
    data_generator.generate_csv()

    # 5. Finish
    print("Program successfully finished")
