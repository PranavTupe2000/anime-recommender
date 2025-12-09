from anime_recommender.components.vector_store import VectorStoreBuilder
from anime_recommender.components.recommender import AnimeRecommender
from anime_recommender.config import GROQ_API_KEY,MODEL_NAME
from anime_recommender.utils import get_logger, AnimeRecommenderException
from anime_recommender.components.prompt_template import get_anime_prompt

import sys

logger = get_logger(__name__)

class AnimeRecommendationPipeline:
    def __init__(self,persist_dir="chroma_db"):
        try:
            logger.info("Intializing Recommdation Pipeline")
            
            prompt = get_anime_prompt()

            vector_builder = VectorStoreBuilder(csv_path="" , persist_dir=persist_dir)

            retriever = vector_builder.load_vector_store().as_retriever()

            self.recommender = AnimeRecommender(prompt, retriever,GROQ_API_KEY,MODEL_NAME)

            logger.info("Pipleine intialized sucesfully...")

        except Exception as e:
            logger.error(f"Failed to intialize pipeline {str(e)}")
            raise AnimeRecommenderException(e, sys)
        
    def recommend(self,query:str) -> str:
        try:
            logger.info(f"Recived a query {query}")

            recommendation = self.recommender.get_recommendation(query)

            logger.info("Recommendation generated sucesfulyy...")
            return recommendation
        except Exception as e:
            logger.error(f"Failed to get recommendation {str(e)}")
            raise AnimeRecommenderException(e, sys)
        


        