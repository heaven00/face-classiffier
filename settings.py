"""
The configuration used by the program
"""
import os

def get_labels(dirpath):
    label_map = {index:value for index, value in enumerate(os.listdir(dirpath))}
    label_map[-1] = 'Dont Know'
    return label_map

#path to the validation set
VALIDATION_SET = os.path.join('data', 'validation_images')

TRAINING_DATA = os.path.join('data', 'train_images')

# This allows us to choose between cv2.eigenFaceRecoganizer() and
# cv2.fisherFaceRecoganizer. The value can be either "eigen" or
# "fisher"
MODEL = "eigen"

#Number of components / k
COMPONENTS = 20

#Model threshold
THRESHOLD = 5000.0

#Color of the text to be displayed on the cam
TEXT_COLOR = (150, 255, 0)

#Color of the rectangle to be displayed
RECT_COLOR = (255, 255, 0)

#Set the value to True to enable learning mode
LEARNING_MODE = True

#map of labels to replace integer predicted by the model to labels
#always keep -1 as dont know or NA
LABEL_MAP = get_labels(TRAINING_DATA)

REVERSE_LABEL_MAP = {LABEL_MAP[key]:key for key in LABEL_MAP.keys()}
print "labels generated"
print LABEL_MAP