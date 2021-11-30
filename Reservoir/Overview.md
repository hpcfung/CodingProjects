Here we have a simple neural network (NN) with 6 layers (4 hidden layers), trained to classify a simplified version of MNIST.
Conceptually, the NN can be decomposed into 3 parts: the features (the first hidden layer), the "reservoir" 
(the 2-4th hidden layers), and "regression" (the final neuron).

### Features

### Reservoir

### Regression

## Results


First epoch first batch, 

(200 epoch run)

By around epoch 2, regression has the least change

Most learning in reservoir 2 and 3? But similar (though less) for features

Reservoir 1 has the least change?

Late: 


When overfitting, most of the learning occurs in the reservoir?

Changing the algorithm structure, towards "rote memorization"?

Counterarguments 

### 1
this is just fine-tuning?

### 2
Exception: 1000 epoch run, epoch 626, features change and regression change roughly the same?

Just a rare exception?

The final batch is smaller, induces stochasticity?

### 3
a small change in the features layer, induces a larger change in the later layers

need a relatively large change in weights in the final layers to compensate


