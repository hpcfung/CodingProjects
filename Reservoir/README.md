Here we have a simple neural network (NN) with 6 layers (4 hidden layers), trained to classify a simplified version of MNIST.
Conceptually, the NN can be decomposed into 3 parts: the features (the first hidden layer), the "reservoir" 
(the 2-4th hidden layers), and "regression" (the final neuron).

Features and regression: interface with input and output?

reservoir = where the computation is actually done?

But actually, there is no real distinction between features and computation?

Features = computation on raw image?

Counter: features = initial data processing?

once the data has been manipulated into the right format, can do the actual computation?

Reference: https://karpathy.medium.com/software-2-0-a64152b37c35

## Results

(Unless specified, uses Adam)

Batch size = 8192 to minimize the effect of stochasticity

Learning rate = 1e-3

All hidden layers has 150 neurons

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

Keeps overshoot, maybe?

### Different architecture
First hidden layer 150 neurons, all subsequent layers: 50 neurons

700 epochs:

reservoir 3 is the peak before epoch 5 (test accuracy ~0.92)

But other than that, deeper = less learning

By epoch 6, reservoir 3 dips below features; strictly deeper = less learning

By epoch 31, reservoir 1 is the peak, test accuracy plateaued at 0.981

### Another architecture

hidden layers: 150, 50, 300, 20

Initially, inverted V-shape (learning to use the right algorithm/computation for this problem?)

peak at reservoir 3: kind of by design (most number of neurons, bulk of the computation?)

By epoch 6, entered the deeper = less learning regime?

By epoch 35, reservoir 1 is now the peak (test accuracy plateaued at 0.985)(inverted V-shape again)

By epoch 76, reservoir 2 is now the peak (although regression can be high sometimes)

This holds until the end?

### Yet another architecture

If I do 20, 400, 20, 400

Then the peak is stuck at reservoir 1? (400) Never goes to reservoir 2? (20)

Other than that all patterns still holds

ie the peaks go to the two 400 layers

we forced them to be the computational layers?

### frozen reservoir
regression larger than features initially

By epoch 6, features larger than regression (test accuracy 0.95)

Epoch 35, start to reverse, (test accuracy 0.981)

### frozen features vs regression
frozen features limit test accuracy to around 0.91, but frozen regression has no effect (still 0.986)

good features: knows what to look?

presumably, the regression weights are diverse enough, we can just assign them?

in fact frozen regression slightly better, 0.987

prevented overfitting? (still some, just not that much?)

although train loss doesn't go as low as otherwise possible

### Reduced training set

Size 8192

At the beginning, deeper = less learning, except peak at reservoir 1

Peak at features by epoch 7

Peak shifts to reservoir 1 by epoch 48 (test accuracy plateaued at 0.975)

Peak shifts to reservoir 2 by epoch 86

Peak shifts to reservoir 3 by epoch 114, continues till the end

Despite more than halving the training set, the test accuracy is still high

Size 2048

Strange enough, there doesn't seem to be any overfitting?

Test accuracy goes up until the end

(reduced batch size means that at the same number of epochs, there have been fewer iterations)

# Random labels

## 150, 150, 150, 150
Has to rely on memorization

So large learning in the computational layers early on?

That said, still need to learn features, to recognize the images

U-shaped? reservoir 2 and 3 are lower than the others

Test accuracy goes to 0.2, ie completely random; no overfit, since the labels are random anyway

But if you go far enough, eg epoch 367, inverted-V? peak at reservoir 2

After that it goes to deeper = less learning, until epoch 400

Train loss cannot go below 0.7, ie this indicates the architecture is not expressive enough to memorize everything?

Hence it doesn't really overfit?

### Frozen reservoir
no rebounce, but much slower convergence

ie needs to walk a lot more steps to reach the minima

this suggests that the global minima are rarer?

## Different architecture: 400, 400, 400, 400

Poor convergence? Train loss drops to 0.26, then bounces, then drops and repeats

Highly rugged loss landscape?

Mostly follows deeper = less learning? eg epoch 227 onwards?

Actually, if you freeze the reservoir, the train loss can go down to 0.09

## 1200, 1200, 1200, 1200
deeper = less learning

then inverted-V, peak at reservoir 3

this time, no rebounce

### frozen reservoir
converged slower

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

counter: deeper layers are actually not that sensitive to the first layers?

ie change filter slightly, still roughly extracts the same feature?


