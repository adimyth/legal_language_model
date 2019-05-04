# Language Model on Legal Data

Language Modeling is the development of probabilistic models that are able to predict the next word in the sequence given the words that precede it.
A language model learns the probability of word occurrence based on examples of text. Simpler models may look at a context of a short sequence of words, whereas larger models may work at the level of sentences or paragraphs. Most commonly, language models operate at the level of words.

Here, I'm training a word level language model.

## Data
I used Supreme Court reports as data. You can create your own dataset. Any dataset with large corpus of text files, is good enough. For example, Wikipedia, News channel articles etc.

## Modelling
I used transfer learning to train the language model. The inspiration here, is mostly taken from Jeremy Howard's course "Practical Deep Learning for Coders".
AWD_LSTM is a variant of LSTM and has been trained on the Wiki-103 dataset. Wiki-103 is a  collection of over 100 million tokens extracted from the set of verified Good and Featured articles on Wikipedia.

AWD_LSTM was created by Stephen Merity. It has the following two key concepts
    * DropConnect
    * Non-monotonically triggered averaged sgd
For more details, check this excellent [article](https://yashuseth.blog/2018/09/12/awd-lstm-explanation-understanding-language-model/)

## Training
#### Clone the repo
```bash
git clone https://github.com/adimyth/legal_language_model.git
```

#### Create python environment
```bash
cd legal_language_model
conda env create -f conda.yml
conda activate lang_model
```

#### Training the model
Change the file from `judgements.csv` to your filename in LanguageModelling.py script
```
export PYTHONPATH=.
python scripts/LangaugeModelling.py --type train
```

#### Inference
```
python scripts/LanguageModelling.py --type predict --sent "It is therefore the duty" --n_words 10
```

## Result
After training for 10 epochs, I got an accuracy of **0.49**, which implies that the model is able to predict every second word correctly, which is cool.
The highlighted/bold section represents the predicted sentences.

<pre>
Example 1
Sentence: The jurisdiction  of the High Court
Num of words: 5
The jurisdiction  of the High Court <b>in the case of</b>


Example 2
Sentence: The  fixed monthly allowance
Num of words: 5
The  fixed monthly allowance <b>payable to the assessee</b>


Example 3
Sentence: It is therefore the duty
Num of words: 5
It is therefore the duty <b>of the Court</b>


Example 4
Sentence: The jurisdiction  of the High Court
Num of words: 10
The jurisdiction  of the High Court <b>to interfere with the findings of fact arrived at</b>


Example 5
Sentence: It is therefore the duty
Num of words: 10
It is therefore the duty <b>of the High Court to set aside</b>


Example 6
Sentence: The  fixed monthly allowance
Num of words: 10
The  fixed monthly allowance <b>of Rs . 85 / - per month</b>
</pre>
