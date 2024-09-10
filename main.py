
from matplotlib import pyplot as plt
import seaborn as sns
from analysis_code import import_data


def main():
  print("This is a demonstration of using git to manage workflows")
  print(import_data.import_data("https://api.worldbank.org/v2/country/all/indicator/SP.POP.TOTL?format=json").columns)

if __name__ == "__main__":
  main()
