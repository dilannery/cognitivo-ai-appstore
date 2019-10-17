# coding: utf-8
import sqlite3
import logging as log
import pandas as pd
from decouple import config

from twitter import TwitterClient

class Top10Dataset:
  """
  Represents the 10 mosted rated Apps for a Dataset by genre
  """
  
  def __init__(self, df, genre):
    genre_df = df[df['prime_genre'] == genre]
    genre_df = genre_df.sort_values(by='rating_count_tot', ascending=False)
    self.df = genre_df.iloc[:10]
    
  def count_quotes(self):
    twc = TwitterClient()
    
    n_citacoes = []
    for _, row in self.df.iterrows():
      log.info("Fetching quotes for: {}".format(row['track_name']))
      n_citacoes.append(twc.count(row['track_name']))
      
    self.df['n_citacoes'] = n_citacoes
    columns = ['id', 'track_name', 'n_citacoes', 'size_bytes', 'price', 'prime_genre']
    self.df = self.df[columns]
    
  def save(self, path, name):
    con = sqlite3.connect(path.joinpath(name + '.sqlite3'))
  
    self.df.to_csv(path.joinpath(name + '.csv')) # CSV export
    self.df.to_json(path.joinpath(name + '.json')) # JSON export
    self.df.to_sql(name=name, con=con, if_exists="replace") # Local Database Export