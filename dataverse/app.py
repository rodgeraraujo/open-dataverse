import dataread.download as data

url = "https://raw.githubusercontent.com/codeforamerica/ohana-api/master/data/sample-csv/addresses.csv";

def main():
  data.downloadData(url, "aluno")

__main__ = main()