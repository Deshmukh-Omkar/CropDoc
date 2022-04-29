# CropDoc
CropDoc is a Web Application which predicts crop diseases from user sourced input, across 18 crops and 55 diseases using a Keras Sequential Deep Learning model.
## Problem Statement
Since the birth of farming, a major challenge has always been to safekeep the crops from diseases and pests. However, nature always plays the upper hand and farmers have learnt from trial and error, passing down their learnings to future generations. Evolution of science allowed us to study these diseases in depth and provide fertilizers, pesticides, herbicides etc. to help get the maximum yield.

However, a challenge prevails at the farmer's end. In developing country, such as India, farmers lack the preliminary knowledge of diseases their crops suffer with. That's where CropDoc steps in to empower them. CropDoc allows them to gain insight on an unknown disease by just clicking an image and uploading it to the website. The AI detects the disease and provides back with relevant details along with links for further information.
## Tech Stack
- Python
- Keras
- HTML
- CSS
- Bootstrap
- Flask
- MongoDB Atlas
## Features
- Detects crop disease.
- Provides information about the detected disease.
- If any crop or disease isn't present on the website, provides user a form to submit the details along with pictures.
- Hindi UI for Indian farmers
- Responsive website for all devices.
- Supports low-end hardware (smartphones & PC) on the user's device.
## Module 0: Deep Learning Model
### Why CNN?
![Simple-VS-DeepLearning](https://user-images.githubusercontent.com/42082976/164188704-10dba20e-b1b0-42e4-bf06-5a3d43e55c4a.jpeg)
- Simple Neural Nets are good at learning the weights with one hidden layer which is in between the input and output layer. But, it’s not good at complex feature learning.
- On another hand in  Deep Learning Neural Nets, the series of layers between input and output layer are called hidden layers that can perform identification of features and creating new series of features from data, just as our brain. The more layers we push into the more features it will learn and perform complex operations. The output layer combines all features and makes predictions.
- Therefore, Simple Neural Nets are used for simple tasks and bulk data isn’t required to train itself. whereas in Deep learning Neural Network can be expensive and require massive data sets to train itself on. 
- Convolutional Neural Network(CNN or Conv Nets) is well known for its use in applications of image and video recognition. It is more efficient because it reduces the number of parameters which makes different from other deep learning models.
- **For this model, we used DenseNet201.**
### Dataset
- Derived from Kaggle
- Contains 229108 images across 55 classes.
- Sources include
  - PlantVillage
  - USDA
  - Kaggle Competitions
### Development of the model (video)
[![Screenshot 2022-04-20 at 2 53 13 PM](https://user-images.githubusercontent.com/42082976/164196344-e4f1f115-c428-4600-88b0-a876c984e1a3.png)](https://youtu.be/Kz2f_YFx5js)
### Performance of the model (screenshots of the accuracy and charts)
*Due to Dark Mode, the plots might miss certain metrics and title. To view properly, click the plot to open in a new tab.

![Training and Validation Accuracy](https://user-images.githubusercontent.com/42082976/164190971-f6268e9e-57e4-4d68-9c1a-4917428a1c60.png)
![Training and Validation Loss](https://user-images.githubusercontent.com/42082976/164190997-ffbac7c1-85fc-4a9f-af44-2a6e59eb593a.png)
## Module 1: Front-end
- Developed using:
  - HTML
  - CSS
  - Bootstrap
- Hindi text for Indian target end-users.
- Responsive UI for all devices
- Optimised for quick loading even in low speed internet connections.
## Module 2: Backend
### Flask
- Connected and routed all the HTML webpages.
- Uploaded the user input file.
- Secured the file and saved into a folder.
- Preprocessed the image file and sent for prediction.
- Connected the MongoDB Database
- Based on prediction, fetched the respective data from MongoDB.
### MongoDB
- Two tables
  - Disease Data
  - New Data (for user entry form)
- Cloud based
- Quick response
### Development of the Front-end (video)
[![Capture1](https://user-images.githubusercontent.com/42082976/164280334-6dc5eee4-3989-4eb6-8f79-83c57b9750c6.JPG)](https://youtu.be/m4adcrkkdeY)
## Implementation (video)
[![Capture](https://user-images.githubusercontent.com/42082976/164277837-88be32e8-1277-4b2e-ae00-a82cfd57840d.JPG)](https://www.youtube.com/watch?v=NIJWenfImOo)

