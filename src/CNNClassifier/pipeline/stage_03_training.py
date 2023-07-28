from src.CNNClassifier.config.configuration import ConfigurationManager
from src.CNNClassifier.components.training import Training
from src.CNNClassifier import logger


STAGE_NAME = "Training"

class ModelTrainingPipeline:
    def __init__(self) -> None:
        pass

    def main(self):
        config = ConfigurationManager()
        training_config = config.get_training_config()
        training = Training(config=training_config)
        training.get_base_model()
        training.train_valid_generator()
        training.train()
        
    