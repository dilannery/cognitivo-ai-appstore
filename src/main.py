# coding: utf-8
import logging as log
import pandas as pd
from pathlib import Path

from top10 import Top10Dataset

log.basicConfig(level=log.INFO, format='[%(levelname)s] %(asctime)s - %(message)s')
BASE_DIR = Path(__file__).resolve().parent.parent
DATASET_PATH = BASE_DIR.joinpath('data')

def main():
  log.info('=======================================')
  log.info('Opening dataset...')
  log.info('=======================================')
  appstore_df = pd.read_csv(DATASET_PATH.joinpath('AppleStore.csv'))
  
  # Extract Top 10 apps for Music and Book
  log.info('=============================================')  
  log.info('Extracting top 10 apps for Music and Book...')  
  log.info('=============================================')
  top10_music_apps = Top10Dataset(appstore_df, 'Music')
  top10_book_apps = Top10Dataset(appstore_df, 'Book')
  
  # Find quotes on Twitter (most rated News app)
  log.info('=======================================')
  log.info('Adding quotes couting for Music Apps...') 
  log.info('=======================================')
  top10_music_apps.count_quotes()
  log.info('=======================================')
  log.info('Adding quotes couting for Book Apps...')    
  log.info('=======================================')
  top10_book_apps.count_quotes()
  
  # Save new dataset as CSV, JSON and Local Database (SQLite3)
  try:
    log.info('Saving datasets...')
    top10_music_apps.save(DATASET_PATH, 'music/top10')
    top10_book_apps.save(DATASET_PATH, 'book/top10')
  except ValueError:
    log.error('It was not possible to save the dataset')

if __name__ == '__main__':
  main()
