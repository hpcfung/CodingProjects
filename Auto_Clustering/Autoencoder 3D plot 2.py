import torch as T
import numpy as np
import matplotlib.lines
import matplotlib.pyplot as plt
from torch import nn
import time, sys

import plotly.express as px
import plotly.io as pi

device = T.device("cpu") # cuda

hidden_layer_width1 = 150
hidden_layer_width2 = 100
hidden_layer_width3 = 3
hidden_layer_width4 = 100
hidden_layer_width5 = 150

learning_rate = 1e-4
batch_size = 32 #100
epochs = 100 # 50

reg_const = 0 # 250
wavelength = 300 # 300
offset = 0
prod_coeff = 0
drift_coeff = 0

show_every = 800
cols, rows = 32, 16

_3d_plot_in_matlab = False

class DigitsDataset(T.utils.data.Dataset):

  def __init__(self, src_file, TEST):
    if TEST == True:            #use random split?
      x_tmp = np.loadtxt(src_file, max_rows=3000, usecols=range(0, 196))
      y_tmp = np.loadtxt(src_file, max_rows=3000, usecols=196)
    else:
      x_tmp = np.loadtxt(src_file, skiprows=3000, usecols=range(0, 196))
      y_tmp = np.loadtxt(src_file, skiprows=3000, usecols=196)

    self.x_data = T.tensor(x_tmp, dtype=T.float32).to(device)
    self.y_data = T.tensor(y_tmp).to(device)

  def __len__(self):
    return len(self.x_data)  # required

  def __getitem__(self, idx):
    img = self.x_data[idx, 0:196]
    dgt = T.div(self.y_data[idx], 2, rounding_mode='floor')
    return img, dgt.long()

train_dataset = DigitsDataset("even_mnist.csv", TEST=False)
test_dataset = DigitsDataset("even_mnist.csv", TEST=True)

train_dataloader = T.utils.data.DataLoader(train_dataset, batch_size=batch_size, shuffle=True)
#test_dataloader = T.utils.data.DataLoader(test_dataset, batch_size=100, shuffle=True)

class NeuralNetwork(nn.Module):
  def __init__(self):
    super(NeuralNetwork, self).__init__()
    self.beta = 0.01
    self.linear_relu_stack1 = nn.Sequential(
      nn.Linear(14 * 14, hidden_layer_width1),
      nn.LeakyReLU(self.beta),
      nn.Linear(hidden_layer_width1, hidden_layer_width2),
      nn.LeakyReLU(self.beta),
      nn.Linear(hidden_layer_width2, hidden_layer_width3),
    )
    self.linear_relu_stack2 = nn.Sequential(
        nn.LeakyReLU(self.beta),
        nn.Linear(hidden_layer_width3, hidden_layer_width4),
        nn.LeakyReLU(self.beta),
        nn.Linear(hidden_layer_width4, hidden_layer_width5),
        nn.LeakyReLU(self.beta),
        nn.Linear(hidden_layer_width5, 14 * 14),
    )

  def forward(self, x):
        code = self.linear_relu_stack1(x)
        return self.linear_relu_stack2(code), code

model = NeuralNetwork().to(device)


def regularizer(input_tensor):
    sinusoid = T.sin(2*np.pi*input_tensor/wavelength)
    before_taking_prod = (sinusoid+offset) ** 3

    # before_taking_prod = T.sin(2*np.pi*input_tensor/wavelength)

    prod = T.prod(before_taking_prod,1)
    radius_term = 1/(T.sum(input_tensor**2,1))**0.2
    return T.mean(prod_coeff*prod+drift_coeff*radius_term)


def train_loop(dataloader, model, loss_fn, optimizer):
  size = len(dataloader.dataset)
  for batch, (X, y) in enumerate(dataloader):
    # Compute prediction and loss
    pred, CODE = model(X)
    loss = loss_fn(pred, X)+reg_const*regularizer(CODE) # -drift_coeff*T.mean(CODE)

    # Backpropagation
    optimizer.zero_grad()
    loss.backward()
    optimizer.step()

    if batch % show_every == 0:
      loss, current = loss.item(), batch * len(X)
      print(f"loss: {loss:>7f}  [{current:>5d}/{size:>5d}]")



def plot_a_picture(sample,shift):
    picture_as_array = []
    picture = np.zeros([14, 14], int)
    for i in range(196):
      picture[i // 14, i % 14] = sample[i]
      picture_as_array.append(sample[i])
    figure.add_subplot(rows, cols, 2*n +shift+1)
    # title = str(prediction(picture_as_tensor.float()))+" ["+str(round(sample[196]))+"]"
    # plt.title(title)
    plt.axis("off")
    plt.imshow(np.array(picture), cmap="gray")

def code_plot(encoding):
    colour = 'k' # if == 0
    if encoding[3] == 2:
        colour = 'm'
    if encoding[3] == 4:
        colour = 'y'
    if encoding[3] == 6:
        colour = 'g'
    if encoding[3] == 8:
        colour = 'b'
    ax.scatter3D(encoding[0], encoding[1], encoding[2], color=colour)

if __name__ == '__main__':
    loss_fn = nn.MSELoss()
    optimizer = T.optim.Adam(model.parameters(), lr=learning_rate)

    start = time.time()
    for t in range(epochs):
        train_loop(train_dataloader, model, loss_fn, optimizer)
        end = time.time()
        print(f"Epoch {t + 1}   time = {end-start}")
        start = time.time()
    print("Done!")

# def prediction(input_tensor):
#   logits = model(input_tensor)
#   pred_probab = nn.Softmax()(logits) #dim=1
#   y_pred = pred_probab.argmax()*2 #1
#   return y_pred.tolist()

    Input = np.loadtxt("even_mnist.csv")

    figure = plt.figure(figsize=(8, 8))


    num_plots = rows*int(cols/2)
    code_plot_list = np.zeros((num_plots,4))
    digits = []

    for n in range(num_plots):
        before_processing = Input[n, 0:196]
        picture_as_tensor = T.tensor(np.array(np.float32(before_processing))).to(device)
        to_be_plot,encoded = model(picture_as_tensor)
        #encoded2 = encoded.detach().numpy()
        code_plot_list[n,0]=encoded[0]
        code_plot_list[n, 1] = encoded[1]
        code_plot_list[n, 2] = encoded[2]
        code_plot_list[n, 3] = Input[n, 196]
        digits.append(str(int(Input[n, 196])))

        plot_a_picture(before_processing, 0)
        plot_a_picture(to_be_plot, 1)

    if _3d_plot_in_matlab:
        fig = plt.figure(100)
        ax = plt.axes(projection='3d')
        for n in range(num_plots):
            code_plot(code_plot_list[n,:])

        scatter1_proxy = matplotlib.lines.Line2D([0],[0], linestyle="none", c='k', marker = 'o')
        scatter2_proxy = matplotlib.lines.Line2D([0],[0], linestyle="none", c='m', marker = 'o')
        scatter3_proxy = matplotlib.lines.Line2D([0],[0], linestyle="none", c='y', marker = 'o')
        scatter4_proxy = matplotlib.lines.Line2D([0],[0], linestyle="none", c='g', marker = 'o')
        scatter5_proxy = matplotlib.lines.Line2D([0],[0], linestyle="none", c='b', marker = 'o')
        ax.legend([scatter1_proxy, scatter2_proxy,scatter3_proxy, scatter4_proxy, scatter5_proxy],
                  ['0', '2', '4', '6', '8'], numpoints = 1)


    data_frame = {'x': code_plot_list[:,0], 'y': code_plot_list[:,1],
                  'z': code_plot_list[:,2]}
    fig2 = px.scatter_3d(data_frame, x='x', y='y', z='z', color=digits, opacity=1,
                         title='wavelength' + str(wavelength) + ', regularizer' + str(reg_const)+', drift'+str(drift_coeff)+', offset'+str(offset))
    fig2.update_traces(marker=dict(size=3))
    name = 'wavelength' + str(wavelength) + 'regularizer' + str(reg_const)+'drift'+str(drift_coeff)+'time' + str(int(time.time()))+'offset'+str(offset)
    fig2.write_html(name + '.html')
    plt.savefig(name+ '.pdf')

    plt.show()
