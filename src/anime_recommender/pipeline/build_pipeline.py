from anime_recommender.components.data_loader import AnimeDataLoader
from anime_recommender.components.vector_store import VectorStoreBuilder
from anime_recommender.config import ORIGINAL_CSV_PATH, PROCESSED_CSV_PATH
from anime_recommender.utils import AnimeRecommenderException, get_logger

import sys

logger = get_logger(__name__)

def build_pipeline():
    try:
        logger.info("Starting to build pipeline...")

        loader = AnimeDataLoader(ORIGINAL_CSV_PATH , PROCESSED_CSV_PATH)
        processed_csv = loader.load_and_process()

        logger.info("Data  loaded and processed...")

        vector_builder = VectorStoreBuilder(processed_csv)
        vector_builder.build_and_save_vectorstore()

        logger.info("Vector store Built sucesfully....")

        logger.info("Pipelien built sucesfuly....")
    except Exception as e:
            logger.error(f"Failed to execute pipeline {str(e)}")
            raise AnimeRecommenderException(e, sys)
    
if __name__=="__main__":
     build_pipeline()
