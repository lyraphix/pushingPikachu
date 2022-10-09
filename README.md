# Pushing Pikachu

## Introduction

Pushing Pikachu is a project that uses a fine-tuned GloVe embedding to find conceptual synonyms for words outside of GloVe's corpus. Specifically, this project used 40,000 tweets from 5 large Twitch streamers to train the model on gaming and pop culture vocab. This project was done in 8 weeks through Out in Tech University and under the mentorship of Dr. Lara Martin at the University of Pennsylvania. It was one of two projects selected for presentation to the larger Out in Tech community upon graduation.

Find the .pdf [here,]( https://drive.google.com/file/d/1QxC9f94-CBFVojxkosHuGS2S53V1-LPX/view?usp=sharing) and feel free to try out the code yourself following the instructions below!

## Code Acknowledgement
Credits to the following sources for code and/or assistance:

* Roam Analytics – [Fast Mittens](https://github.com/roamanalytics/mittens)

* Rainy Shen – [Co-occurrence matrix visualization](https://rainynotes.net/co-occurrence-matrix-visualization/)

* Sivasurya Santhanam – [Fine tuning Glove Embeddings with Mittens](https://gist.github.com/chmodsss/867e01cc3eeeaa42226ac931709077dc#file-fine_tune_glove-py)

* Stanford NLP – [GloVe](https://nlp.stanford.edu/projects/glove/)

* Khuyen Tran – [Tokenizing Tweets]( https://github.com/khuyentran1401/Data-science/blob/master/nlp/tweets_tokenize.ipynb)

* Parthvi Shah – [Tweet Pre-Processing](https://towardsdatascience.com/basic-tweet-preprocessing-in-python-efd8360d529e)



## Installation

Start by downloading the folder. Then navigate to the directory in your CLI. The model is included in a .pkl file for convenient access.

## Usage

First, run the program interactively in python using the following command:

```bash
$ !python3 -i pushingPikachu.py
```

The program will automatically unwrap the .pkl (this may take up to 10 minutes). Once complete, you can now run the program!

```python
# returns a synonym for 'pikachu'
findSynonyms('pikachu')
snorlax

# you can also set parameters such as depth
# the example below will compare 'pikachu' to 100000 other terms
findSynonyms('pikachu', tries=100000)
eevee


# and verbosity (print nearest term after each attempt)
findSynonyms('pikachu', tries=100000, p=True)
picachu
picachu
picachu
...
...
...
charmander

```

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License
[MIT](https://choosealicense.com/licenses/mit/)
