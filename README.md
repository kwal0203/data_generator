# DataGenerator

This is a tool to that generates training and test data-sets for use in the
TensorFlow [Object Detection API](https://github.com/tensorflow/models/tree/master/research/object_detection).
Using this tool will allow you to skip the time-consuming manual labelling step
of the object detection pipeline.

## Getting Started

These instructions will get you a copy of the project up and running on your
local machine for development and testing purposes.

### Prerequisites

The following Python libraries will need to be installed for the application to
work

```
os
optparse
PIL
pandas
random
```

### Usage

On the command-line navigate to a directory where you would like to place the
application.

Type the following command:

```
git clone https://github.com/kwal0203/data_generator.git.
```

Create the following two directories inside the data_generator folder:

```
images
backgrounds
```

Fill the images directory with examples of the object you would like to train
the model to detect.

Fill the backgrounds folder with random images to be used
as backgrounds while training the model.

Decide how many times you would like to re-use each background (see number
below) and type the following command:

```
python3 main.py -s number
```

A new directory called output will be created containing training and test
data-sets in separate folders along with separate CSV files corresponding to
the data-sets. These CSV files can be converted into TFRecords for use in the
TensorFlow Object Detection API. 

## Authors

* **Kane Walter** - [LinkedIn](https://www.linkedin.com/in/kanewalter/)

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md)
file for details