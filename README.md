# South Park Diction

My project surrounding South Park character diction learning.

<a href="https://www.dictionary.com/browse/diction">Dictionary.com</a> defines diction as: noun - *style of speaking or writing as dependent upon choice of words*

Given a collection of 70k+ utterances from the series <a href="https://en.wikipedia.org/wiki/South_Park">South Park</a>, can an AI model learn the diction of different main characters? Is it able to out perform humans who are familiar with the show?

## Data

The utterances are recorded from Season 1 - 18 of South Park and stored in `characterUtterances.csv`  under the `/data` folder.

## Files

  1. SPdiction_clean.ipynb

#### SPdiction_clean.ipynb

The data was cleaned in the following manner: ellipses indicating stutters were stripped and replaced with blank space. Regular punctuation was then removed and the lines were lowercased. A lower bound was placed on the number of words in a line, a value of 4 has been decided for the time being. 6 main characters were selected for the time being, and all others dropped.

The results of this is saved in `/data/procCharLines.csv`

## To-Do

<<<<<<< HEAD
-[x] Clean & preprocess data, determine appropriate minimum length.
-[ ] Data exploration, semantic modelling, toxicity modelling.
-[ ] Diction modelling with ML, investigate BERT layers.
-[ ] Flask web application to obtain human scores on test set.
-[ ] Contrast AI accuracy against human accuracy.
-[ ] Flask web application to determine which SP character your diction resembles: if possible let them load emails - not sure on feasability of this yet.
=======
- [ ] Clean & preprocess data, determine appropriate minimum length, train and test splits etc.
- [ ] Data exploration, semantic modelling, toxicity modelling.
- [ ] Diction modelling with ML, investigate BERT layers.
- [ ] Flask web application to obtain human scores on test set.
- [ ] Contrast AI accuracy against human accuracy.
- [ ] Flask web application to determine which SP character your diction resembles: if possible let them load emails - not sure on feasability of this yet.
- [ ] Build models which mimic each characters diction?
>>>>>>> 874c93510beb49f6e79e90e9ec68f08f1e9761a6
