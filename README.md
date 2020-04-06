# South Park Diction

My project surrounding South Park character diction learning.

<a href="https://www.dictionary.com/browse/diction">Dictionary.com</a> defines diction as: noun - *style of speaking or writing as dependent upon choice of words*

Given a collection of 70k+ utterances from the series <a href="https://en.wikipedia.org/wiki/South_Park">South Park</a>, can an AI model learn the diction of different main characters? Is it able to out perform humans who are familiar with the show?

## Data

The utterances are recorded from Season 1 - 18 of South Park and stored in `characterUtterances.csv`  under the `/data` folder.

## Files

  1. SPdiction_clean.ipynb
  2. SPdiction_EDA.ipynb
  3. SPdiction_detection.ipynb

#### SPdiction_clean.ipynb

The data was cleaned in the following manner: ellipses indicating stutters were stripped and replaced with blank space. Regular punctuation was then removed and the lines were lowercased. A lower bound was placed on the number of words in a line, a value of 4 has been decided for the time being. 6 main characters were selected for the time being, and all others dropped.

The results of this is saved in `/data/procSelectCharLines.csv`.

The results for all characters is saved in `/data/procAllCharLines`

<a href='https://colab.research.google.com/drive/15B5iReXJFI1v7RMoxYwrev6NJl-2cCZT'>Open in Google Colab</a>

#### SPdiction_EDA.ipynb

Exploratory data analysis of the processed character lines. We look at the total lines per character, the distribution of line lengths per character, the most common uni/bi/tri-grams across all lines, as well as the most frequent uni/bi/tri-grams for each of our chosen characters. We end of using the VADER module to detect the sentiment of each line and plot the sentiment of our characters, and the sentiment variation over the 18 seasons.

<a href='https://colab.research.google.com/drive/1NC5aAYyqmRaGSean3o8LLfVIGkxNOKg3'>Open in Google Colab</a>

#### SPdiction_detection.ipynb

Added very basic conv model.

## To-Do

- [x] Clean & preprocess data, determine appropriate minimum length, train and test splits etc.
- [x] Data exploration, semantic modelling.
- [ ] Diction modelling with ML, investigate BERT layers, ELMO.
- [ ] Flask web application to obtain human scores on test set.
- [ ] Contrast AI accuracy against human accuracy.
- [ ] Flask web application to determine which SP character your diction resembles: if possible let them load emails - not sure on feasability of this yet.
- [ ] Build models which mimic each characters diction?
