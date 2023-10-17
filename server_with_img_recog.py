import grpc
import image_search_pb2
import image_search_pb2_grpc
import random
import os
import logging
from concurrent import futures
from multiprocessing import Pool
import tensorflow as tf
from tensorflow import keras

class ImageSearchServicer(image_search_pb2_grpc.ImageSearchServiceServicer):
    def __init__(self):
        self.model = keras.models.load_model('model.h5')

    def SearchImage(self, request, context):
        keyword = request.keyword

        try:
            # Replace this logic with your image search logic
            image_path = self.search_image(keyword)

            if image_path:
                with open(image_path, 'rb') as image_file:
                    image_data = image_file.read()
                return image_search_pb2.ImageResponse(image_data=image_data)
            else:
                context.set_code(grpc.StatusCode.NOT_FOUND)
                context.set_details('Image not found')
                return image_search_pb2.ImageResponse()
        except Exception as e:
            logging.error(f'Error searching for image: {e}')
            context.set_code(grpc.StatusCode.INTERNAL)
            context.set_details('Internal server error')
            return image_search_pb2.ImageResponse()

    def search_image(self, keyword):
        # Replace this with your image search logic
        # You can organize images in directories based on keywords
        keyword_dir = os.path.join('Images', keyword)
        if os.path.exists(keyword_dir):
            images = os.listdir(keyword_dir)
            if images:
                # Use multiprocessing to search for images in parallel
                with Pool() as pool:
                    image_paths = pool.map(lambda image: os.path.join(keyword_dir, image), images)
                    # image_path = pool.apply(random.choice, [images])
                # Use the model to predict the keywords for each image
                keywords = self.predict_keywords(image_paths)
                # Select an image with a matching keyword
                for image_path, image_keywords in zip(images, keywords):
                    if keyword in image_keywords:
                        return os.path.join(keyword_dir, image_path)
        return None

    def predict_keywords(self, image_paths):
        # Load the images and preprocess them
        images = [tf.keras.preprocessing.image.load_img(image_path, target_size=(224, 224)) for image_path in image_paths]
        images = [tf.keras.preprocessing.image.img_to_array(image) for image in images]
        images = [tf.keras.applications.resnet50.preprocess_input(image) for image in images]
        images = tf.stack(images)

        # Use the model to predict the keywords for each image
        predictions = self.model.predict(images)
        keywords = [self.get_keywords(prediction) for prediction in predictions]
        return keywords

    def get_keywords(self, prediction):
        # Replace this with your keyword extraction logic    
        # You can use a threshold to select the top keywords
        top_indices = prediction.argsort()[-5:][::-1]
        top_keywords = [self.get_keyword(index) for index in top_indices]
        return top_keywords

    def get_keyword(self, index):
        # Replace this with your keyword mapping logic
        # You can use a dictionary to map the index to a keyword
        return 'keyword' + str(index)

def serve():
    logging.basicConfig(level=logging.INFO)
    server = grpc.server(futures.ThreadPoolExecutor())
    image_search_pb2_grpc.add_ImageSearchServiceServicer_to_server(
        ImageSearchServicer(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    logging.info('Server started')
    server.wait_for_termination()

if __name__ == '__main__':
    serve()