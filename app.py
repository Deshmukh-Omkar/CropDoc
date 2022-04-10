# From YouTube video
# https://www.youtube.com/watch?v=XgzxH6G-ufA

# ML Imports
import os
import numpy as np

# Flask imports
from flask import Flask, flash, render_template, request, send_from_directory
from werkzeug.utils import secure_filename

# Define app
app = Flask(__name__)

# Import MongoDB Atlas client
import mongo_db

# ------------------------------------------------------
# Importing prediction functions
import pred

# Loading model once during a session
print("Loading crop disease model...")
loaded_model = pred.get_model()

# Loading model labels
with open("models/disease_labels.txt", 'r') as f:
    class_names = f.read().split('\n')

# -------------------------------------------------------
@app.route("/")
def index():
    return render_template("index.html")

@app.route("/form")
def form():
    return render_template("new_data.html")

@app.route("/new_data", methods=["POST"])
def new_data():
    if request.method == "POST":
        # TO-DO
        # Storing data into variables
        crop_name = request.form.get("crop_name")
        disease_name = request.form.get("disease_name")
        caused_by = request.form.get("caused_by")
        about = request.form.get("about")
        link = request.form.get("link")
        cure = request.form.get("cure")

        # Merging the names for MongoDB entry
        if disease_name != '':
            entry_name = crop_name.capitalize() + "___" + disease_name
        else:
            entry_name = crop_name.capitalize() + "___" + "healthy"

        # Getting the image from the HTML page
        img_files = request.files.getlist('photos[]')
        print(img_files)

        for image in img_files:
            print(image.filename)

            new_filename = entry_name + "__" + image.filename

            # Storing the base path of the directory
            base_path = os.path.dirname(os.path.abspath(__file__))

            # Creating the path for the image and secure check on the image filename.
            img_path = os.path.join(
                base_path, 'new_data_files', secure_filename(new_filename))

            # Saving the image into the root.
            image.save(img_path)

        # Adding the data in MongoDB
        alert = mongo_db.new_data(entry_name, caused_by, about, link, cure)

        return render_template("index.html", Alert=alert)
    else:
        return render_template("index.html", Alert="unsuccessful, no POST")

@app.route("/predict", methods=["POST"])
def predict():
    if request.method == 'POST':
        print("Photo uploaded") # Debug

        # Getting the image from the HTML page
        img_file = request.files['image']

        # Storing the base path of the directory
        base_path = os.path.dirname(os.path.abspath(__file__))

        # Creating the path for the image and secure check on the image filename.
        img_path = os.path.join(
            base_path, 'upload_files', secure_filename(img_file.filename))

        # Saving the image into the root.
        img_file.save(img_path)
        
        # ---------
        # Prediction

        # Pre-processing image
        processed_image = pred.preprocess_image(img_path)

        # TM Getting the prediction class
        preds = loaded_model.predict(processed_image)

        # From the numpy array of probabilities, we filter out the class with maximum probability
        index = np.argmax(preds)

        # Retrieving disease name from label list
        class_name = class_names[index]

        # Deriving the confidence score of the prediction by the model.
        confidence_score = preds[0][index]

        # CLI: Printing the disease name and confidence score 
        print("Class: ", class_name)
        print("Confidence score: ", confidence_score)

        # ---------
        # Retrieving data from MongoDB Atlas
        disease_data = mongo_db.open_mongo_diseases(index)
        # ---------

        # Returning the predicted class
        return render_template("prediction.html",
            Name=disease_data['Name'],
            Caused_by=disease_data['Caused_by'],
            About=disease_data['About'],
            More_info_link=disease_data['More_info_link'],
            Cure=disease_data['Cure'],
            Image_Path=pred.pred_img(disease_data['Name']))
    
    return render_template("index.html")

if __name__ == '__main__':
    app.run(debug=True)