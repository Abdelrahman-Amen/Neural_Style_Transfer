# Neural Style Transfer: Bringing Art to Life 🖼️ 🎨 🖌
# What is Neural Style Transfer (NST)? 🧠

Neural Style Transfer is a fascinating application of deep learning that blends two images:

## 1. Content Image: This provides the structure, layout, and general appearance of the result.
  
## 2. Style Image: This provides the artistic texture and patterns that you want to overlay onto the content image.

By combining these two, NST creates a stylized image that retains the structural elements of the content while incorporating the artistic style.

![Image](https://github.com/user-attachments/assets/1c08419d-e68e-4ba2-a54d-9e1431410523)


# How Does NST Work? 🎨
The process of Neural Style Transfer involves:

1. Extracting Features: Deep learning models, often Convolutional Neural Networks (CNNs), extract features from both the style and content images.
   
2. Defining Objectives:
• The Content Objective ensures the output resembles the structure of the content image.

• The Style Objective ensures the textures, colors, and patterns from the style image are reflected in the result.

3. Merging Style and Content: A pre-trained model adjusts the content image’s features to align with the desired style while retaining the original structure.
   
NST is typically performed using models like VGG19 or TensorFlow Hub's pre-trained Arbitrary Image Stylization model.



# Features of the Project 🚀
1. Dynamic Image Selection:
Upload your content image and style image directly through the app.

2. Real-Time Stylization:
Leveraging TensorFlow Hub’s Arbitrary Image Stylization model, the app generates the stylized image in real-time.

3. User-Friendly Interface:
Built using Streamlit, the app is simple, interactive, and easy to use.




# How the App Works 🛠️

1. Preprocessing Images:

• Converts images into tensors and normalizes them for model compatibility.

• Adds batch dimensions to facilitate computation.

2. Style Transfer Model:

• The pre-trained model processes the images and outputs a stylized tensor.

• Converts the output tensor back into an image for display.

3. Streamlit Integration:

• Provides a clean interface for users to upload images and generate results effortlessly.



# Example Workflow 📸 
1. Upload a content image (e.g., a photo of a cityscape).

2. Upload a style image (e.g., a painting by Van Gogh).
   
3. Click Generate Stylized Image.
 
4 .View and save the newly created masterpiece! 🎉

# Demo 🎥
Here’s how it works:
![Streamlit App Demo](https://github.com/Abdelrahman-Amen/Neural_Style_Transfer/blob/main/Streamlit%20App.gif)


# Why Neural Style Transfer? 💡

NST bridges the gap between artificial intelligence and art, enabling creators to craft unique visuals effortlessly. It’s perfect for:

•  Artistic endeavors

• Image processing

• Creative projects
