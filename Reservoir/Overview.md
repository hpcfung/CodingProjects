Here we have a simple neural network (NN) with 6 layers (4 hidden layers), trained to classify a simplified version of MNIST.
Conceptually, the NN can be decomposed into 3 parts: the features (the first hidden layer), the "reservoir" 
(the 2-4th hidden layers), and "regression" (the final neuron).

### Features

### Reservoir

### Regression

## Results

(Unless specified, uses Adam)

### 1
First epoch first batch, since random initialization, not good algorithm for the problem at hand, lots of learning in all layers


### 2
(200 epoch run) By around epoch 2, regression has the least change

Most learning in reservoir 2 and 3? But similar (though less) for features

Reservoir 1 has the least change?

Sometimes we see clear pattern: the deeper it goes, the less learning

eg 700 epoch run, around epoch 4, test accuracy ~90%, test accuracy still going up

Very clear pattern in that regime

### 2.5
eg 700 epoch run, test accuracy plateaued at 0.98 by epoch 18 (though the training loss is getting stochastic)

The pattern is still clear (deeper layer less learning)

After that, you start to see more exceptions

eg reservoir 2 learns more than reservoir 1

After that reservoir 2 starts to approach features 

By 700 epoch run, epoch 27, reservoir 2 often exceeds features

By 700 epoch run, epoch 30, we get an inverted V graph: most learning happens at the center, reservoir 2

Learning goes down as you move to either side


### 3
Late: eg 700 epoch run, test accuracy routinely reaches 0.986 by epoch 60, maxed out

Also the training loss is experiencing a lot of stochasticity

Most of the learning happens in the upper layers

Peak at reservoir 3

Reservoir 1,2,3 and regression have roughly the same learning

Features: much less learning


When overfitting, most of the learning occurs in the reservoir?

Changing the algorithm structure, towards "rote memorization"?

### SGD
SGD converges much more slowly. However the qualitative behavior seems to be the same (at the given test accuracy)

Except regression tends to have the most learning? Even when test accuracy = 0.9

Quite consistent from beginning to the end

For both SGD 200 and 700 epoch runs

## Counterarguments to overfitting = learning only happens in the higher layers

### 1
this is just fine-tuning?

### 2
Exception: 1000 epoch run, epoch 626, features change and regression change roughly the same?

Just a rare exception?

The final batch is smaller, induces stochasticity?

### 3
a small change in the features layer, induces a larger change in the later layers

need a relatively large change in weights in the final layers to compensate


