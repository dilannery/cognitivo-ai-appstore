# coding: utf-8
import pandas as pd
from pathlib import Path

from top10 import Top10Dataset

BASE_DIR = Path(__file__).resolve().parent.parent
DATASET_PATH = BASE_DIR.joinpath('data')

def main():
  print('Opening dataset...')
  appstore_df = pd.read_csv(DATASET_PATH.joinpath('AppleStore.csv'))
  
  # Extract Top 10 apps for Music and Book
  print('Extracting top 10 apps for Music and Book...')  
  top10_music_apps = Top10Dataset(appstore_df, 'Music')
  top10_book_apps = Top10Dataset(appstore_df, 'Book')
  
  # Find quotes on Twitter (most rated News app)
  print('Adding quotes couting for Music Apps...')  
  top10_music_apps.count_quotes()
  print('Adding quotes couting for Book Apps...')    
  top10_book_apps.count_quotes()
  
  # Save new dataset as CSV, JSON and Local Database (SQLite3)
  print('Saving datasets...')
  top10_music_apps.save(DATASET_PATH, 'music/top10')
  top10_book_apps.save(DATASET_PATH, 'book/top10')
  

if __name__ == '__main__':
  main()