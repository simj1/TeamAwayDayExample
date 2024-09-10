import pandas as pd
import numpy as np
import requests


def import_data(path: str):
  response = requests.get(path)
  data = response.json()
  df = pd.DataFrame(data[1])
  return df
