from src.CNNClassifier import logger
from src.CNNClassifier.pipeline.stage_02_prepare_base_model import PrepareBaseModelTrainingPipeline
    

STAGE_NAME = 'Prepare Base Model'

if __name__ == '__main__':

    try:
        logger.info("***********************")
        logger.info(f">>>>> stage {STAGE_NAME} started <<<<<<")
        prepare_base_model = PrepareBaseModelTrainingPipeline()
        prepare_base_model.main()
        logger.info(f">>>>> stage {STAGE_NAME} completed <<<<<<\n\nx=========x")
    except Exception as e:
        logger.exception(e)
        raise(e)
    

