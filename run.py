#!/usr/bin/env python
import cv2
import time
import numpy as np
import settings
import cPickle
from os import path
from face_classifier import make_model, validate_model

def main():
    classifier = cv2.CascadeClassifier('data/classifier/haarcascade_frontalface_alt.xml')
    print "Generating Model ..."
    model = make_model()
    print "Model ready"

    cam = cv2.VideoCapture(0)
    while True:
        val, img = cam.read()
        if settings.LEARNING_MODE:
            # keep the copy of the original image incase it needs to be added to the training set
            learn_img = img.copy()
        img = cv2.flip(img,1,0)
        faces = classifier.detectMultiScale(img, scaleFactor=1.2, minNeighbors=5, minSize=(110,110))
        label = None
        for params in faces:
            x, y, w, h = params
            cv2.rectangle(img, (x, y), (x + w, y + h), settings.RECT_COLOR, thickness=2)
            cropped_img = img.copy()
            roi = cropped_img[y:y+h, x:x+w]
            roi = cv2.resize(roi, (112, 112))
            gray_roi = cv2.cvtColor(roi, cv2.COLOR_BGR2GRAY)
            [p_label, p_confidence] = model.predict(np.asarray(gray_roi))
            label = settings.LABEL_MAP[p_label]
            if p_label != -1:
                string = "%s (confidence=%.2f)" % (label, p_confidence)
            else:
                string = label
            cv2.putText(img, string, (x-10, y-10), cv2.FONT_HERSHEY_COMPLEX,0.5, settings.TEXT_COLOR)
        cv2.imshow("capture", img)
        key = cv2.waitKey(10)
        if key == 27:
            break
        if settings.LEARNING_MODE:
            filepath = None
            for mapid in settings.LABEL_MAP.keys():
                if mapid != -1:
                    if key == ord(str(mapid)[0]):
                        filepath = path.join(settings.TRAINING_DATA, settings.LABEL_MAP[mapid])
            if key in [77, 109]:
                filepath = path.join(settings.TRAINING_DATA, 'male')
            elif key in [70, 112]:
                filepath = path.join(settings.TRAINING_DATA, 'female')
            if filepath:
                fn = "learned_img_{0:.0f}.png".format(time.time())
                fn = path.join(filepath, fn)
                cv2.imwrite(fn, learn_img)
                print fn, "saved"

if __name__ == "__main__":
    main()