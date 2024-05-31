import grpc
import image_search_pb2
import image_search_pb2_grpc
import random
import os
import logging
from concurrent import futures
import yake
import keras

channel = grpc.insecure_channel('localhost:3080', options=[('grpc.max_receive_message_length', 10 * 1024 * 1024)])

class ImageSearchServicer(image_search_pb2_grpc.ImageSearchServiceServicer):
    
    def __init__(self):
        self.model = keras.models.load_model('model.h5')
        # Compile the model
        self.model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])
        self.keyword_extractor = yake.KeywordExtractor()

    def SearchImage(self, request, context):
        keyword = request.keyword

        try:
            keywords = self.extract_keywords(keyword)
            print(keywords)

            # Search for images with matching keywords
            for keyword in keywords:
                image_path = self.search_image(keyword)
                print(image_path)
                if image_path:
                    with open(image_path, 'rb') as image_file:
                        image_data = image_file.read()
                    return image_search_pb2.ImageResponse(image_data=image_data)
                
        except Exception as e:
            logging.error(f'Error searching for image: {e}')
            context.set_code(grpc.StatusCode.INTERNAL)
            context.set_details('Internal server error')
            return image_search_pb2.ImageResponse()
    
    def extract_keywords(self, query):
        # Use the keyword extractor to extract keywords from the query
        keywords = self.keyword_extractor.extract_keywords(query)
        keywords = [keyword[0] for keyword in keywords]
        return keywords

    def search_image(self, keyword):        
        images_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), 'Images'))
        keywords = self.extract_keywords(keyword)
        print(keywords)
        
        for keyword in keywords:
            keyword_dir = os.path.join(images_dir, keyword)
            print("Keyword dir: ", keyword_dir)
            
            if os.path.exists(keyword_dir):
                print("Keyword dir exists")
                images = os.listdir(keyword_dir)
                print("Images: ",images)
                if images:
                    return os.path.join(keyword_dir, random.choice(images))
        return None

def serve():
    logging.basicConfig(level=logging.INFO)
    server = grpc.server(futures.ThreadPoolExecutor())
    image_search_pb2_grpc.add_ImageSearchServiceServicer_to_server(
        ImageSearchServicer(), server)
    server.add_insecure_port('[::]:3080')
    server.start()
    logging.info('Server started')
    server.wait_for_termination()

if __name__ == '__main__':
    serve() 