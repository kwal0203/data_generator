# DataGenerator

This is a tool that generates data-sets for use in the TensorFlow
[Object Detection API](https://github.com/tensorflow/models/tree/master/research/object_detection).
Using this tool will allow you to avoid the need to manually label your input
images.

## Getting Started

These instructions will get you a copy of the project up and running on your
local machine for development and testing purposes.

### Prerequisites

The following Python libraries will need to be installed for the application to
work:

```
os
optparse
PIL
pandas
random
```

You will need an image of the object you want the trained model to detect and
a set of random images to serve as backgrounds. The application will paste the
object image in a random location on the backgrounds that you place in the
'backgrounds' directory (explained below). Doing this process repeatedly
(with any number of object and background images) is how the data-sets are
created. 

In terms of the input images, make sure that all of your background images are
of the same dimensions and all your object images are of the same dimensions
(and smaller than the background image dimensions).

### Usage

On the command-line, navigate to a directory where you would like to place the
application.

Type the following command:

```
git clone https://github.com/kwal0203/data_generator.git
```

Create the following two directories inside the 'data_generator' folder:

```
images
backgrounds
```

In the 'images' directory, place an example of the object/s you want to train
the model to detect.

Fill the 'backgrounds' folder with random images to be used as backgrounds while
training the model. The objects in the 'images' directory will be randomly
pasted onto these backgrounds to create the data-sets.

Decide how many times you would like to re-use each background (NUMBER) and
type the following command to run the application:

```
python3 main.py -s NUMBER
```

A new directory called output will be created containing training and test
data-sets in separate folders. CSV files that correspond to these data-sets
will also be created. The CSV files can be converted into TFRecords for use in
the TensorFlow Object Detection API. 

## Authors

* **Kane Walter** - [LinkedIn](https://www.linkedin.com/in/kanewalter/)

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md)
file for details