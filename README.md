# Hidden Mark.. M.. (Project #2)

## Contributors
- Nishil Parmar

## Datasets
- [Amazon Fine Food Reviews (240 MB)](https://www.kaggle.com/snap/amazon-fine-food-reviews)

## Implementions
- Text Generation and Prediction
  - Uses 2nd Order Markov Chain Property
  - Uses a Transition Probability Matrix to predict next word and eventually generates a sentence
  
## Approach

In a Markov System, the current state determines the probability distribution for the next state. In my approach to building a Markov System for text prediction, the current state and the previous state will determine the probability distribtion for the next state. This is can be called as 2nd Order Markov System. This arcitecture can prove to be generate more corherent text sentences, the quality of text sentences generated would also depend on the data used to train the model. For this project i chose to go with Amazon Fine Food Review dataset.

Amazon Fine Food Reviews dataset has a rich collection of reviews posted by amazon users on various amazon food products, These are real life day to day text sentences which can be very helpful in text generation and prediction applications.


## Project Files
- [sqllite3 database preprocessing](https://github.com/nishil70/HiddenMarkovModel/blob/master/notebooks/1_preprocessing.ipynb)
- [Text prediction using Review Summary](https://github.com/nishil70/HiddenMarkovModel/blob/master/notebooks/2_building-dictionary.ipynb)
- [Text prediction using Reviews](https://github.com/nishil70/HiddenMarkovModel/blob/master/notebooks/3_generate-sentences.ipynb)
- [Markov Model](https://github.com/nishil70/HiddenMarkovModel/blob/master/models/MarkovModel.py)
- [persistent models](https://github.com/nishil70/HiddenMarkovModel/tree/master/archives)
   - Couldn't include some of the trained persistant models as they were quite large in size

## References
- http://www.cs.cmu.edu/~./awm/tutorials/hmm.html
- http://www.blackarbs.com/blog/introduction-hidden-markov-models-python-networkx-sklearn/2/9/2017
- http://ieeexplore.ieee.org/iel5/5/698/00018626.pdf?arnumber=18626
- https://towardsdatascience.com/using-a-markov-chain-sentence-generator-in-python-to-generate-real-fake-news-e9c904e967e
- https://hackernoon.com/automated-text-generator-using-markov-chain-de999a41e047
- https://medium.com/ymedialabs-innovation/next-word-prediction-using-markov-model-570fc0475f96
