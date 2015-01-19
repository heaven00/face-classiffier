#!/usr/bin/env python
import os
import cv2
import numpy as np
import settings

CLASSIFIER = cv2.CascadeClassifier('data/classifier/haarcascade_frontalface_alt.xml')

def read_images(path=r'data/train_images/'):
    """
    Walk through the data/train_images/ folder and pick up subdirectories
    and images in it.
    The name of the subdirectory will act as the label for the training data.

    example:
        |train_images
        ----|male
            -----|male_1.pgm
            -----|male_2.pgm
            -----|male_3.pgm
        ----|female
            -----|female_1.pgm
            -----|female_2.pgm
            -----|female_3.pgm

    args
    ====
    path = path to a folder/dir containg the training set

    Return
    ======
    A list of numpy arrays containing images and labels
    """
    label = 0
    images, labels = [], []
    for dirpath, dirnames, filenames in os.walk(path):
        for subdir in dirnames:
            subdirpath = os.path.join(dirpath, subdir)
            for filename in os.listdir(subdirpath):
                img = cv2.imread(os.path.join(subdirpath, filename))
                #do basic image conversion to grayscale and resize images
                faces = CLASSIFIER.detectMultiScale(img, minSize=(30,30))
                for params in faces:
                    x, y, w, h = params
                    cropped_img = img.copy()
                    roi = cropped_img[y:y+h, x:x+w]
                    roi = cv2.resize(roi, (112, 112))
                    gray_roi = cv2.cvtColor(roi, cv2.COLOR_BGR2GRAY)
                    images.append(np.asarray(gray_roi, dtype=np.uint8))
                    labels.append(label)
            label = label + 1
    return [images, labels]

def get_model(images, labels, model_name='eigen', k=settings.COMPONENTS):
    """
    Gives the user an option to choose between eigenfaces and fisherfaces

    args
    ====
    images = list of images in numpy array format
    labels = respectve labels for the images
    model_name = string reference to choosing fihser or eigen model
                {'eigen' : cv2.createEigenFaceRecognizer,
                'fisher' : cv2.createFisherFaceRecognizer}

    Returns
    =======
    A trained model class.
    """
    models = {'eigen' : cv2.createEigenFaceRecognizer(num_components=k, threshold=settings.THRESHOLD),
            'fisher' : cv2.createFisherFaceRecognizer(threshold=settings.THRESHOLD)}

    model = models[settings.MODEL]
    model.train(np.asarray(images), np.asarray(labels))
    return model

def validate_model(model):
    [images, labels] = read_images(settings.VALIDATION_SET)
    total_number = float(len(images))
    correct = 0.0
    wrong = 0.0
    for index in range(0, len(images)):
        img = images[index]
        actual_label = labels[index]
        [p_label, p_confidence] = model.predict(img)
        if p_label == actual_label:
            #add up the true neg and true pos
            correct += 1.0
        elif p_label != actual_label:
            #add up the false neg and false pos
            wrong += 1.0
    accuracy = (correct/(correct + wrong))*100
    return accuracy

def make_model():
    [images, labels] = read_images()
    components = settings.COMPONENTS
    model = None
    model_accuracy = 0.0
    print "Finding optimal number of components... this might take a while."
    for index in range(10,200,10):
        temp_model = get_model(images, labels, model_name='eigen', k=index)
        temp_model_accuracy = validate_model(temp_model)
        if model_accuracy < temp_model_accuracy:
            components = index
            model = temp_model
            model_accuracy = temp_model_accuracy
    print "number of components= {0}, acc= {1:.2f}%".format(components, model_accuracy)
    return model

if __name__ == "__main__":
    model = make_model()
    print model.getMat("eigenvectors")
