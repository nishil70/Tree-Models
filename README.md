# Hidden Mark.. M.. (Project #2)

## Requirements
   Probabilistic states and transitions
1. Set up a new git repository in your GitHub account
2. Pick a text corpus dataset such as
https://www.kaggle.com/kingburrito666/shakespeare-plays
or from https://github.com/niderhoff/nlp-datasets
3. Choose a programming language (Python, C/C++, Java)
4. Formulate ideas on how machine learning can be used to learn word correlations and distributions within the dataset
5. Build a Hidden Markov Model to be able to programmatically
1. Generate new text from the text corpus
2. Perform text prediction given a sequence of words
6. Document your process and results
7. Commit your source code, documentation and other supporting files to the git repository in GitHub 

## Contributors
- Nishil Parmar

## Datasets
- [Amazon Fine Food Reviews (240 MB)](https://www.kaggle.com/snap/amazon-fine-food-reviews)

## Implementions
- Text Generation and Prediction
  - Uses 2nd Order Markov Chain Property
  - Uses a Transition Probability Matrix to predict next word and eventually generates a sentence

## Project Files
- [sqllite3 database preprocessing](https://github.com/nishil70/HiddenMarkovModel/blob/master/notebooks/1_preprocessing.ipynb)
- [Text prediction using Review Summary](https://github.com/nishil70/HiddenMarkovModel/blob/master/notebooks/2_building-dictionary.ipynb)
- [Text prediction using Reviews](https://github.com/nishil70/HiddenMarkovModel/blob/master/notebooks/3_generate-sentences.ipynb)
- [Markov Model](https://github.com/nishil70/HiddenMarkovModel/blob/master/models/MarkovModel.py)

## References
- http://www.cs.cmu.edu/~./awm/tutorials/hmm.html
- http://www.blackarbs.com/blog/introduction-hidden-markov-models-python-networkx-sklearn/2/9/2017
- http://ieeexplore.ieee.org/iel5/5/698/00018626.pdf?arnumber=18626
- https://towardsdatascience.com/using-a-markov-chain-sentence-generator-in-python-to-generate-real-fake-news-e9c904e967e
- https://hackernoon.com/automated-text-generator-using-markov-chain-de999a41e047
- https://medium.com/ymedialabs-innovation/next-word-prediction-using-markov-model-570fc0475f96
