How To Use
==========

'cd' into your favourite project directory and clone the project.

    git clone https://github.com/heaven00/face-classiffier.git


well we have the code now we need to setup the data. The training data needs to be in a particular order.

    cd data
    mkdir train_images
    mkdir validation_images

the name of the folders can be changed to anything, but that has to be set in the settings.py accordingly. "*train_images*" will contain your training data and "*validatoin_images*" will contain your validation set.

More information on the structure of the folder can be found in the folders itself.


After setting up the data, 
        
        python run.py

Incase you see an error, please report it. Thanks :)

REQUIREMENT
-----------


You need python 2.7, opencv, numpy & pandas running perfectly on your machine.

For py 2.7, numpy, pandas its easier to just install Anaconda if you are on Windows, if you are on linux well I trust you already know what to do. :) :fingers_crosses:

Now, to setup opencv get a [prebuilt version](http://www.lfd.uci.edu/~gohlke/pythonlibs/#opencv) and install it using wheel.

If you don't have wheel do

    pip install wheel


 and then install the downloaded python version using

    pip install path/to/the/file.whl


