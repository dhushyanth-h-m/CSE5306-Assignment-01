import keras

# Download the VGG16 model
model = keras.applications.vgg16.VGG16(weights='imagenet')

# Save the model to a file
model.save('model.h5')