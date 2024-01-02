from django.http import HttpResponse
from django.shortcuts import render
from django.http import JsonResponse
from .models import CarBrand
import tensorflow as tf
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.image import img_to_array
import cv2
import numpy as np
import os
import time

model_filename = "car_classification_model.h5"
model_path = os.path.join(os.path.dirname(__file__), model_filename)
best_model = load_model(model_path)

class_labels = ['Audi', 'Hyundai Creta', 'Mahindra Scorpio',
                'Rolls Royce', 'Swift', 'Tata Safari', 'Toyota Innova']
print(str(best_model))


def index(request):
    return render(request, 'Predict/index.html')


@tf.function
def predict_image(image_array):
    prediction = best_model(image_array)
    class_index = tf.argmax(prediction, axis=1)
    predicted_class = tf.gather(class_labels, class_index)
    return predicted_class


def predict_car_brand(request):
    if request.method == 'POST' and request.FILES['image']:
        uploaded_image = request.FILES['image'].read()
        image_array = cv2.imdecode(np.frombuffer(uploaded_image, np.uint8), -1)

        # Resize the image to match the model input size
        image_resized = cv2.resize(image_array, (224, 224))

        img_array = img_to_array(image_resized)
        img_array = np.expand_dims(img_array, axis=0)
        img_array /= 255.0

        image_tensor = tf.convert_to_tensor(img_array, dtype=tf.float32)

        # Measure the time taken to make predictions
        start_time = time.time()

        # Make a prediction
        predicted_brand = predict_image(image_tensor)
        label = predicted_brand.numpy()[0].decode()

        end_time = time.time()
        elapsed_time = end_time - start_time
        print(f"Time taken to make predictions: {elapsed_time} seconds")

        # Save the predicted brand to the CarBrand model (optional)
        car_brand = CarBrand.objects.create(name=label)

        # Return the predicted brand as JSON
        return JsonResponse({'predicted_brand': label, 'elapsed_time': elapsed_time})

    return render(request, 'Predict/predict_car_brand.html')


# Load the trained model from the saved file
model_filename = 'CatFaceFeatures_Resnet50_2.h5'
model_path = os.path.join(os.path.dirname(__file__), model_filename)
loaded_model = load_model(model_path)
print(str(loaded_model))


# Function to predict facial landmarks on new images


def predict_landmarks(request):
    if request.method == 'POST' and request.FILES['image']:
        uploaded_image = request.FILES['image'].read()
        image_array = cv2.imdecode(np.frombuffer(uploaded_image, np.uint8), -1)

        # Convert image object to numpy array
        image = image_array.astype('uint8')

        # Define the image size for resizing
        image_size = (224, 224)

        # Convert to RGB before resizing
        image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        resized_image = cv2.resize(image_rgb, image_size)
        input_image = np.expand_dims(resized_image, axis=0)

        # Make predictions using the trained model
        predictions = loaded_model.predict(input_image)

        # Rescale the predictions to the original image size
        scale_y = image.shape[0] / image_size[0]
        scale_x = image.shape[1] / image_size[1]
        resized_predictions = [int(value * scale_x) if i % 2 == 0 else int(
            value * scale_y) for i, value in enumerate(predictions[0])]

        # Calculate the radius of the circles based on image dimensions
        image_height, image_width, _ = image.shape
        max_dim = max(image_height, image_width)
        radius_scale = max_dim / 1500  # Adjust this scale factor as needed

        # Draw circles (dots) on the original image at the predicted landmark locations
        for i in range(0, len(resized_predictions), 2):
            x, y = resized_predictions[i], resized_predictions[i + 1]
            color = (255, 0, 0)
            # Adjust the base radius value as needed
            radius = int(8 * radius_scale)
            thickness = -1
            cv2.circle(image, (x, y), radius, color, thickness)

        # Convert the image array back to bytes
        _, img_encoded = cv2.imencode('.png', image)
        response = img_encoded.tobytes()

        return HttpResponse(response, content_type='image/png')

    # Replace 'your_template.html' with the actual template name
    return render(request, 'Predict/predict_car_brand.html')
