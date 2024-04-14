import os
from flask import Flask, render_template, request, send_from_directory
import numpy as np
import tensorflow as tf
from PIL import Image
import uuid  # for generating unique filenames

# Initialize Flask application
app = Flask(__name__)

# Define paths for the model and image uploads
MODEL_ARCHITECTURE_PATH = 'digits_recognition_cnn_architecture.json'
MODEL_WEIGHTS_PATH = 'digits_recognition_cnn_weights.weights.h5'
UPLOAD_FOLDER = 'uploads'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}

# Set the upload folder in Flask app configuration
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Load the model architecture from JSON
with open(MODEL_ARCHITECTURE_PATH, 'r') as f:
    loaded_model_architecture = f.read()

# Reconstruct the model from the architecture
loaded_model = tf.keras.models.model_from_json(loaded_model_architecture)

# Load the model weights
loaded_model.load_weights(MODEL_WEIGHTS_PATH)

# Function to check if the file extension is allowed
def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

# Define a route for the home page
@app.route('/')
def home():
    return render_template('index.html')

# Define a route for model prediction
@app.route('/predict', methods=['POST'])
def predict():
    if 'file' not in request.files:
        return render_template('index.html', prediction='No file uploaded!')
    
    file = request.files['file']
    
    if file.filename == '':
        return render_template('index.html', prediction='No file selected!')
    
    if file and allowed_file(file.filename):
        img = Image.open(file)
        img = img.resize((28, 28))
        img = img.convert('L')  # Convert to grayscale
        img_array = np.array(img)
        img_array = img_array.reshape((1, 28, 28, 1))
        img_array = img_array / 255.0  # Normalize
        
        prediction = loaded_model.predict(img_array)
        predicted_digit = np.argmax(prediction)
        
        # Generate a unique filename for the uploaded image
        filename = str(uuid.uuid4()) + '.png'
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        img.save(file_path)
        
        return render_template('index.html', prediction='Predicted digit: {}'.format(predicted_digit), uploaded_image=filename)
    else:
        return render_template('index.html', prediction='Invalid file format!')

# Define a route to serve uploaded images
@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)

if __name__ == '__main__':
    app.run(debug=True)









