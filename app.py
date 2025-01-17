import streamlit as st
import tensorflow_hub as hub
from PIL import Image
import numpy as np
import tensorflow as tf
import os

# Suppress warnings and logs
os.environ['TF_ENABLE_ONEDNN_OPTS'] = '0'
tf.get_logger().setLevel('ERROR')

# Cache the model
@st.cache_resource
def load_model():
    return hub.load('https://tfhub.dev/google/magenta/arbitrary-image-stylization-v1-256/2')

model = load_model()

# Cache the image preprocessing
@st.cache_data
def preprocess_image(image_data, max_dim=256):  # Reduced resolution for faster processing
    img = tf.image.decode_image(image_data, channels=3)
    img = tf.image.convert_image_dtype(img, tf.float32)  # Normalize to [0,1]
    original_shape = tf.cast(tf.shape(img)[:-1], tf.float32)
    scale = max_dim / max(original_shape)  # Scale based on max dimension
    new_shape = tf.cast(original_shape * scale, tf.int32)
    img = tf.image.resize(img, new_shape)
    img = tf.expand_dims(img, axis=0)  # Add batch dimension
    return img

# Streamlit App
st.title("Neural Style Transfer App")

# Step 1: Upload the content image
content_file = st.file_uploader("Upload Content Image", type=["jpg", "jpeg", "png"])
if content_file is not None:
    content_image = content_file.read()  # Read the file as bytes
    content_image_pil = Image.open(content_file)  # Display using PIL
    st.image(content_image_pil, caption="Content Image", use_container_width=True)
    content_image = preprocess_image(content_image)  # Preprocess the image

# Step 2: Upload the style image
style_file = st.file_uploader("Upload Style Image", type=["jpg", "jpeg", "png"])
if style_file is not None:
    style_image = style_file.read()  # Read the file as bytes
    style_image_pil = Image.open(style_file)  # Display using PIL
    st.image(style_image_pil, caption="Style Image", use_container_width=True)
    style_image = preprocess_image(style_image)  # Preprocess the image

# Step 3: Generate the stylized image
if st.button('Generate Stylized Image') and content_file is not None and style_file is not None:
    # Perform style transfer
    stylized_image = model(tf.constant(content_image), tf.constant(style_image))[0]
    
    # Convert tensor to image format for display
    stylized_image_np = np.squeeze(stylized_image.numpy())  # Remove batch dimension
    stylized_image_np = np.clip(stylized_image_np, 0.0, 1.0)  # Ensure values are between 0 and 1
    
    # Display the stylized image
    st.image(stylized_image_np, caption="Stylized Image", use_container_width=True)
