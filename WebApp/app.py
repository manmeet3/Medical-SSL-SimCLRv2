import os
import sys

# Flask
from flask import Flask, redirect, url_for, request, render_template, Response, jsonify, redirect
from werkzeug.utils import secure_filename
from gevent.pywsgi import WSGIServer

# TensorFlow and tf.keras
import tensorflow as tf
from tensorflow import keras

from tensorflow.keras.applications.imagenet_utils import preprocess_input, decode_predictions
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image

# Some utilites
import numpy as np
from util import base64_to_pil
from simclr_data_util import *

# Declare a flask app
app = Flask(__name__)


# You can use pretrained model from Keras
# Check https://keras.io/applications/
# or https://www.tensorflow.org/api_docs/python/tf/keras/applications


resnet_model = keras.models.load_model("./models/simclr.h5")

plant_patho_labels = ["healthy", "multiple_diseases", "rust", "scab"]

print('Models loaded. Check http://127.0.0.1:5000/')


def _preprocess_simclr(x):
  x = preprocess_image(
      x, 224, 224, is_training=False, color_distort=False) # used 224*224 for simclr
  return x


@app.route('/', methods=['GET'])
def index():
    # Main page
    return render_template('index.html')


@app.route('/predict', methods=['GET', 'POST'])
def predict():
    if request.method == 'POST':
        # Get the image from post request
        img = base64_to_pil(request.json)

        # Save the image to ./uploads
        img.save("./uploads/image.png")
#        resnet_preds = models_predict(img, resnet_model)
        
        resnet_img = img.resize((2048, 1365)) 
        # Preprocessing the image
        resnet_img = image.img_to_array(resnet_img)
        resnet_img = np.expand_dims(resnet_img, axis=0)


        print(type(resnet_model))
        resnet_preds = resnet_model.predict(resnet_img)

        print("prediction: ", resnet_preds)


        pred_proba = np.argmax(resnet_preds)   # Max probability
        print("class: ", pred_proba)
        pred_class = plant_patho_labels[pred_proba]
        print("Proba: ", pred_proba, "class: ", pred_class)


        final_result = pred_class #+ '\nRESNET Result: ' + pred_class

        # Serialize the result, you can add additional fields
        return jsonify(result=final_result, probability=str(pred_proba))
        #return jsonify(result=result2, probability=pred_proba2)

    return None


if __name__ == '__main__':
    # app.run(port=5002, threaded=False)

    # Serve the app with gevent
    http_server = WSGIServer(('0.0.0.0', 5000), app)
    http_server.serve_forever()
