import grpc
import image_search_pb2
import image_search_pb2_grpc
import random
import os
import logging
from concurrent import futures
from multiprocessing import Pool
import yake
import keras

class ImageSearchServicer(image_search_pb2_grpc.ImageSearchServiceServicer):
    import keras
    
    def SearchImage(self, request, context):
        keyword = request.keyword

        try:
            
            # Use the model to predict the keywords for the query
            # keywords = self.predict_keywords(keyword)
            keywords = self.extract_keywords(keyword)

            # Search for images with matching keywords
            for keyword in keywords:
                image_path = self.search_image(keyword)
                if image_path:
                    with open(image_path, 'rb') as image_file:
                        image_data = image_file.read()
                    return image_search_pb2.ImageResponse(image_data=image_data)
                
        except Exception as e:
            logging.error(f'Error searching for image: {e}')
            context.set_code(grpc.StatusCode.INTERNAL)
            context.set_details('Internal server error')
            return image_search_pb2.ImageResponse()
        
    def predict_keywords(self, query):
        # Replace this with your keyword extraction logic
        # You can use a pre-trained model to predict the keywords
        # For example, you can use a language model like BERT or GPT-2
        # Or you can use a keyword extraction library like RAKE or YAKE
        # For simplicity, we're just splitting the query into words
        keywords = query.split()
        return keywords
    
    def extract_keywords(self, query):
        # Use the keyword extractor to extract keywords from the query
        keywords = self.keyword_extractor.extract_keywords(query)
        keywords = [keyword[0] for keyword in keywords]
        return keywords

    def search_image(self, keyword):
        # Replace this with your image search logic
        # You can organize images in directories based on keywords
        keyword_dir = os.path.join('Images', keyword)
        if os.path.exists(keyword_dir):
            images = os.listdir(keyword_dir)
            if images:
                # Use multiprocessing to search for images in parallel
                with Pool() as pool:
                    image_path = pool.apply(random.choice, [images])
                return os.path.join(keyword_dir, image_path)
        return None

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