<div align="center">
  <img src="img/bigthings.png" height="450"><br>
</div>

# Solving Natural Language problems with scarce data

This repository contains the source code and data used for the talk [Solving Natural Language problems with scarce data](https://www.bigthingsconference.com/2019/schedule/solving-natural-language-problems-with-scarce-data/) presented at the Big Things conference in 2019.

To reproduce the experiments presented in the talk you will need to install an Anaconda Python 3 distribution, clone this repository, then create a Conda environment with

    conda env create -f environment.yml
    
You can then login into the environment with

    source activate bigthings
    
The project is composed as a set of notebooks that approach the problem using different techniques. You can open Jupyter Notebooks to explore them by running

    jupyter notebook

Index of notebooks:

* **sklearn-baselines.ipynb**: baseline models created with scikit-learn.
* **keras.ipynb**: deep learning models created with Keras.
* **simpleBERTusage.ipynb**: simple examples showing the usage of the BERT tokenizer and embeddings.
* **bert.ipynb**: BERT model created with Transformers.
* **plotting.ipynb**: results visualization.

You will also find a **toxic.py** file with auxiliary functions to load and preprocess the data.

Learn and enjoy!
