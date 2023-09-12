# End to End Chicken Disease Classification

## Table of Contents
- [Overview](#overview)
- [Requirements](#requirements)
- [Installation](#installation)
- [Usage](#usage)
- [Model Training](#model-training)
- [Results](#results)
- [Contributing](#contributing)
- [License](#license)

## Overview
This project aims to develop an end-to-end solution for classifying diseases in chickens based on images. It includes data preprocessing, model training, and inference. The trained model can classify chicken images into various disease categories, helping farmers identify and treat sick chickens more effectively.
```
Data: python Data.py
```

## Requirements
- tensorflow
-  pandas 
-  dvc
-  notebook
-  numpy
-  matplotlib
-  seaborn
-  python-box==6.0.2
-  pyYAML
-  tqdm
-  ensure==1.0.2
-  joblib
-  types-PyYAML
-  scipy
-  Flask
-  Flask-Cors

## Installation
1. Clone the repository:
   ```
   git clone https://github.com/kushalBanda/END-TO-END-Chicken-Disease-Classification-.git
   cd END-TO-END-Chicken-Disease-Classification-
   ```

2. Create a virtual environment (recommended):
   ```
   python -m venv venv
   source venv/bin/activate
   ```

3. Install the required packages:
   ```
   pip install -r requirements.txt
   ```

## Usage
1. Data Ingestion: Loading the dataset. `Data.py`
2. Base Model: Prepare a base model for classification `base_model.py`.
3. Train: Train the base model using `train.py`.
4. Model Evaluation: Use the trained model for evaluation using `Evaluation.py`.


## Worflows
1. update config.yaml
2. update secrets.yaml [optional]
3. update params.yaml
4. update the entity
5. update the configuration manager in src config
6. update the components
7. update the pipeline
8. update the main.py
9. update the dvc.yaml
   

### Model Training
To train the model, use the following command:
```
python train.py --dataset_path /path/to/dataset --epochs 50 --batch_size 32
```

### Evaluation
To make predictions on validation dataset, use the following command:
```
python evluation.py
```

## Results
Model performace is given after running evaluation.py where it give the loss and accuracy.

## Contributing
1. Fork the repository.
2. Create a new branch for your feature: `git checkout -b feature-name`
3. Commit your changes: `git commit -m 'Add feature-name'`
4. Push to the branch: `git push origin feature-name`
5. Submit a pull request.

## License
This project is licensed under the [MIT License](LICENSE).

---
