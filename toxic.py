import pandas as pd
import numpy as np

def load_data():
    """Loads the toxic classification problem data, decimating the training data"""
    # Load data CSVs
    train = pd.read_csv("data/toxic_train.csv.zip", index_col="id")
    test = pd.read_csv("data/toxic_test.csv.zip", index_col="id")

    # Decimate training data
    np.random.seed(123456789)
    train = train.sample(int(len(train)/100))

    # Extract labels
    y_train = train.drop("comment_text", axis=1).values
    y_test = test.drop("comment_text", axis=1).values

    return train, y_train, test, y_test
