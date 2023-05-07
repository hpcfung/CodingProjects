import numpy as np
import torch
import torch as T
from torch import nn
import sys
import matplotlib.pyplot as plt

def target_function(x):
    return x**2

# the dataloader is necessary for batching/shuffling
class NN_Dataset(T.utils.data.Dataset):
    def __init__(self, TEST): # TEST: additional argument? inheritance?
        if TEST == True:
            x_tmp = np.linspace(start=-5,stop=5,num=50)
            y_tmp = target_function(x_tmp)
        else:
            x_tmp = np.linspace(start=-10, stop=10, num=100)
            y_tmp = target_function(x_tmp)

        self.x_data = T.tensor(x_tmp).to(device).float()
        self.y_data = T.tensor(y_tmp).to(device).float()

    def __len__(self):
        return len(self.x_data)

    def __getitem__(self, idx):
        NN_input = self.x_data[idx]
        NN_output = self.y_data[idx]
        # need an extra dimension with size 1 for batching?
        # otherwise, automatically add dim at the end: wrong
        return torch.unsqueeze(NN_input,0), torch.unsqueeze(NN_output,0)


class NeuralNetwork(nn.Module):
    def __init__(self):
        super(NeuralNetwork, self).__init__()
        hidden_layer_width1 = 100
        hidden_layer_width2 = 100

        # pytorch syntax: each argument is an NN layer
        self.linear_relu_stack = nn.Sequential(
            nn.Linear(1, hidden_layer_width1),
            nn.ReLU(),
            nn.Linear(hidden_layer_width1, hidden_layer_width2),
            nn.ReLU(),
            nn.Linear(hidden_layer_width2, 1),
        )

    def forward(self, x):
        # the NN is a mathematical and code function
        return self.linear_relu_stack(x)

def train_loop(dataloader, model, loss_fn, optimizer):
    size = len(dataloader.dataset)
    for batch, (X, y) in enumerate(dataloader):
        # Compute prediction and loss
        pred = model(X) # the model is a mathematical and code function
        loss = loss_fn(pred, y)

        # Backpropagation: boiler plate code (don't change this)
        optimizer.zero_grad() # this is necessary
        loss.backward() # populate computational graph
        optimizer.step() # update the parameters according to the optimizer

        if batch % 100 == 0:
            current = batch * len(X)
            print(f"[samples processed: {current:>5d}/{size:>5d}]"  # Training loss: {loss:>7f}  
                  f"[mini-batch processed: {batch}]")
            test_loop(train_dataloader, model, loss_fn, "Training")
            test_loop(test_dataloader, model, loss_fn, "Test")
            print()

def test_loop(dataloader, model, loss_fn, train_or_test):
    num_batches = len(dataloader)
    test_loss = 0

    with T.no_grad():
        for X, y in dataloader:
            pred = model(X)
            test_loss += loss_fn(pred, y).item()

    test_loss /= num_batches
    print(f"{train_or_test} loss: {test_loss:>8f}")

if __name__ == '__main__':
    learning_rate = 1e-2
    batch_size = 25
    epochs = 100

    device = T.device("cpu")


    # data
    train_dataset = NN_Dataset(TEST=False)
    test_dataset = NN_Dataset(TEST=True)

    train_dataloader = T.utils.data.DataLoader(train_dataset, batch_size=batch_size, shuffle=True)
    test_dataloader = T.utils.data.DataLoader(test_dataset, batch_size=batch_size, shuffle=True)

    # model
    model = NeuralNetwork().to(device)

    # Easy to swap loss function and optimizer
    loss_fn = nn.MSELoss()
    optimizer = T.optim.Adam(model.parameters(), lr=learning_rate)
    print()

    for t in range(epochs):
        print(f"Epoch {t + 1}\n-------------------------------")
        train_loop(train_dataloader, model, loss_fn, optimizer)
    print("Training complete")
    print(f"-------------------------------------------------------------------------------")

    x_tmp = np.linspace(start=-20, stop=20, num=200)
    test_intput = torch.unsqueeze(torch.tensor(x_tmp).to(device).float(),1)
    model_pred = model(test_intput).detach().numpy()
    plt.plot(x_tmp,model_pred)
    plt.plot(x_tmp,target_function(x_tmp))
    plt.show()
