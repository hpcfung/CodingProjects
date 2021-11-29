## Similar projects

### 1
https://arxiv.org/abs/1905.02342

uses CNN + LSTM

https://research.nccgroup.com/2021/10/15/cracking-random-number-generators-using-machine-learning-part-1-xorshift128/

### 2
https://research.nccgroup.com/2021/10/15/cracking-random-number-generators-using-machine-learning-part-1-xorshift128/

similar project

## Theory

- Imagine 1,2,3,4,5,...,10,11,12,...,100,101,102,... gluing all of them to form a single sequence
- then given 123, when asked where you are in the sequence
- this question does not have an answer, not even in theory
- loss of predictivity, due to insufficient information among the given information
- need additional information, information not about the sequence itself
- but rather the context...eg the person who asked the question, what their usual thought pattern is like
- eg personality such that
- often choose a small number
- true randomness?

## Results
### 1
- train loss goes down, but test loss goes up: overfitting? does not generalize
- interestingly, at the beginning, the train loss = test loss
- ie it just memorizes the correct labels without developing an algorithm that can generalize?


### 2
- by reducing the input length to 10, the NN can't just memorize the seq
- but that means the training loss never goes down
- at least training loss = test loss

### 3
- if we generate the input data on the fly
- then interestingly, sometimes the training loss goes down (probably just bcuz optimizer doing what it can in one iteration)
- but overall it doesn't move
- most importantly, the test loss stays the same throughout (never drops)

## Autoencoder results
### 1
- both training loss and testing loss drops from around 1.0 to 0.8 in 10 epochs
- drops to 0.7 in 60 epochs, but doesn't drop after that
- maybe it has simply learnt how to do a generic data compression algorithm

## Autoencoder with prediction results
### 1
- if we modify the autoencoder so that the decoder is supposed to return the future values
- surprisingly, both the training and the test loss goes down this time?
- since latent space is reduced and many more predicted values, can't rely on memoriztaion?
- can't go below 0.72 this time
- sometimes the training loss goes down faster than the testing loss, but both still go down at the same time

### 2
- by increasing the latent dim, it can go down to 0.6?
- but actually, when you compute the correlation https://stackoverflow.com/questions/19428029/how-to-get-correlation-of-two-vectors-in-python, it is basically 0?
- which is what we see when we plot the predicted values vs the true values

### 3
- since the loss is distance squared, the actual distance is a bit larger?
- ie the correlation, things go above and below, so cancels out, get overall = 0?

### 4
- actually during training, the correlation does increase? eg 0.003 to 0.015
- although sometimes it becomes more negative for some reasons (ie it goes in the negative direction)
- actually given how large the MSE is, and that the correlation only goes up to 1
- MSE ~ 0.5, correlation ~ 0.08 is reasonable?

### 5
- maximizing the correlation using the optimizer doesn't help
- MSE keeps growing

### 6
- even when testing happens 10000 after the training samples, test loss still goes down at the same rate as before
- this indicates that the algorithm has learnt sth? not just memorization
