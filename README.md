How To Run
==========

1. Make sure you have opencv setup on your machine.
2. Unzip the folder
3. cd into ../facerec dir and run "python run.py"

Configuration
=============
All the configuration settings needed are provided in the settings.py file.
(Incase more options are required will be added here.)

1. LABEL_MAP = A dictionary for mapping labels. This should contain -1 key always,
            you may set the value as you desire (The value will be displayed in case
            face is not recoganized).

2. VALIDATION_SET = Path to the validation set used. default is "data/validation_images"

3. MODEL = This helps in choosing between eigen and fisher model. The value should always
        be either "fisher" or "eigen"

4. COMPONENTS = This sets the number of components used in the model.
            NOTE: This only works with "eigen" model

5. THRESHOLD = Sets the threshold value for the chosen model. Ideal configuration with
            eigen is 5000.0 and with fiser is 123.0 (Havent really toyed around with fisher yet.)

6. TEXT_COLOR = Set the color of the text to be displayed on the video feed.

7. RECT_COLOR = Set the color of the rectangle to be displayed.

8. LEARNING_MODE = If this is set to true you will be able to add images to male or female training data by pressing
		'm'/'M' for male and 'f'/'F' for female.

Remarks
=======
The recognition is at optimal configuration known to me so far, but you are free to toy around.
