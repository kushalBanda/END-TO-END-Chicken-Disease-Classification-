from src.CNNClassifier import logger
from src.CNNClassifier.pipeline.stage_03_training import ModelTrainingPipeline


STAGE_NAME = 'Training'

if __name__ == '__main__':

    try:
        logger.info("***********************")
        logger.info(f">>>>> stage {STAGE_NAME} started <<<<<<")
        model_trainer = ModelTrainingPipeline()
        model_trainer.main()
        logger.info(f">>>>> stage {STAGE_NAME} completed <<<<<<\n\nx=========x")
    except Exception as e:
        logger.exception(e)
        raise(e)
    

