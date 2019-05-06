import pandas as pd
from fastai.text import *
from pathlib import Path
from tqdm import tqdm
from fastai.callbacks import CSVLogger 
import argparse

base_path = Path('.')
path = base_path/'judgements.csv'
BATCH_SIZE = 128
data_lang_model = load_data(base_path, 'data_lm.pkl')

def train():
      data_lm = load_data(base_path, 'data_lm.pkl', bs=BATCH_SIZE)
      learn = language_model_learner(data_lm, AWD_LSTM, drop_mult=0.3, callback_fns=[CSVLogger])
      learn.fit_one_cycle(1, 5e-2, moms=(0.8,0.7))
      learn.save('fit_head')
      learn.load('fit_head')
      learn.unfreeze()
      learn.fit_one_cycle(5, 1e-3, moms=(0.8,0.7))
      learn.save('fine_tuned')
      learn.load('fine_tuned')


def predict(sentence, n_words):
      data_lm = load_data(base_path, 'data_lm.pkl', bs=BATCH_SIZE)
      learn = language_model_learner(data_lm, AWD_LSTM, drop_mult=0.3)
      learn.load('fine_tuned')
      print(f"Sentence: {sentence}\nNumber of Words: {n_words}")
      print(" ".join(learn.predict(sentence, n_words, temperature=0.75)
                      for _ in range(1)))


def get_stmt(orig_sentence):
      learn = language_model_learner(data_lang_model, AWD_LSTM, drop_mult=0.3)
      learn.load('fine_tuned')
      pred_sentence = " ".join(learn.predict(orig_sentence, 10, temperature=0.75)
                      for _ in range(1))
      return orig_sentence, pred_sentence


if __name__ == "__main__":
      parser = argparse.ArgumentParser()
      parser.add_argument("--type", help="train or predict", required=True)
      parser.add_argument("--sent", help="Sentence for prediction")
      parser.add_argument("--n_words", help="Number of words to predict in the sentence")
      args = parser.parse_args()
      if args.type == 'predict':
            predict(args.sent, int(args.n_words))
      else: 
            train()
