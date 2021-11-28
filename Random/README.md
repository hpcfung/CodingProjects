## Similar projects

### 1
https://arxiv.org/abs/1905.02342

uses CNN + LSTM

https://research.nccgroup.com/2021/10/15/cracking-random-number-generators-using-machine-learning-part-1-xorshift128/

### 2
https://research.nccgroup.com/2021/10/15/cracking-random-number-generators-using-machine-learning-part-1-xorshift128/

similar project

## Results
### 1
- train loss goes down, but test loss goes up: overfitting? does not generalize
- interestingly, at the beginning, the train loss = test loss
- ie it just memorizes the correct labels without developing an algorithm that can generalize?

### 2
- try autoencoder next? maybe it can pick up some good features?


### 3
- by reducing the input length to 10, the NN can't just memorize the seq
- but that means the training loss never goes down
- at least training loss = test loss

### 4
- if we generate the input data on the fly
- then interestingly, sometimes the training loss goes down (probably just bcuz optimizer doing what it can in one iteration)
- but overall it doesn't move
- most importantly, the test loss stays the same throughout (never drops)
