import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Load the data
def readcsv(file):
    return pd.read_csv(file)