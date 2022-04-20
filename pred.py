# ML Imports
import numpy as np
# Keras imports
from keras.models import load_model
from keras.preprocessing import image
from keras.preprocessing.image import img_to_array

# Function to load model
def get_model():
    global loaded_model

    # Loading the model
    loaded_model = load_model("models/crop-model-new-day2.h5")

    # Compiling the saved model
    loaded_model.compile(
        optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])

    # CLI success output
    print("Model loaded")
    return loaded_model

# Preprocessing function
def preprocess_image(image_path):
    # Loading image into a variable and Resizing according to model dimensions.
    img = image.load_img(image_path, target_size=(224,224))

    # Converting into nd.array
    img = img_to_array(img)

    # Adding an extra dimension to fit the model shape.
    img = np.expand_dims(img, axis=0)
    return img

def pred_img(dis_name):
    # Dictionary of crop icons
    crop_icons = {
        "टमाटर": "static/assets/offerings/tomato.svg",
        "सेब": "static/assets/offerings/apple.svg",
        "देवदार": "static/assets/offerings/apple.svg",
        "शिमला": "static/assets/offerings/bell_pepper.svg",
        "चेरी": "static/assets/offerings/cherry.svg",
        "कॉफी": "static/assets/offerings/coffee_beans.svg",
        "मकई": "static/assets/offerings/corn.svg",
        "कपास": "static/assets/offerings/cotton_pred.png",
        "अंगूर": "static/assets/offerings/grapes.svg",
        "आड़ू": "static/assets/offerings/peach.svg",
        "आलू": "static/assets/offerings/potato.svg",
        "चावल": "static/assets/offerings/rice.svg",
        "राइस": "static/assets/offerings/rice.svg",
        "गेहूं": "static/assets/offerings/wheat.svg",
        "ब्लूबेरी": "static/assets/offerings/blueberry.svg",
        "संतरा": "static/assets/offerings/orange.svg",
        "रास्पबेरी": "static/assets/offerings/raspberry.svg",
        "सोयाबीन": "static/assets/offerings/soybean.svg",
        "स्क्वैश": "static/assets/offerings/squash.svg",
        "स्ट्राबेरी": "static/assets/offerings/strawberry.svg"
    }

    # Isolating the class name and providing the SVG
    crop_name_words = dis_name.split()
    crop_name = crop_name_words[0]

    pred_img_path = crop_icons[crop_name]
    return pred_img_path