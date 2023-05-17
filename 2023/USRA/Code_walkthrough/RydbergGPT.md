most info in `config/.yaml` file  
`dataset`: so many `null`?  
how does graph embedding work?



training data format  
eg `data/delta_-1_545`
```
config.json
dataset.h5
graph.json
```

weight source target? where do the weights come from?

figure out what dataloader does?

key = pytorch lightning
```
class LitMLP(pl.LightningModule):
    def __init__(self, model):
        super().__init__()
        self.model = model

    def training_step(self, batch, batch_idx):
        X, y = batch
        pred = self.model(X)
        loss = nn.functional.mse_loss(pred, y)

        self.log("train_loss", loss)
        return loss

    def configure_optimizers(self):
        optimizer = T.optim.Adam(self.parameters(), lr=learning_rate)
        return optimizer
```
instead of manual training loop with eg `optimizer.zero_grad()`, `loss.backward()`, `optimizer.step()`, we have `def training_step():`. Note that is extension of `pl.LightningModule`.

Also, instead of defining the model as a class with `def __init__():` and `def forward():`, usually define model as an instance
```
model = nn.Sequential(
        nn.Linear(1, hidden_layer_width1),
        nn.ReLU(),
        nn.Linear(hidden_layer_width1, hidden_layer_width2),
        nn.ReLU(),
        nn.Linear(hidden_layer_width2, 1),
    )
    
MLP = LitMLP(model)
```

### Architecture
See docstring for `class RydbergEncoderDecoder(EncoderDecoder):` in `rydberggpt/models/rydberg_encoder_decoder.py`

## L4
```
yaml_path = f"config/"
main(config_path=yaml_path, config_name=config_name)
def main(config_path: str, config_name: str):
```

### model
```
model = get_rydberg_graph_encoder_decoder(config) # train.py
from rydberggpt.models.rydberg_encoder_decoder import get_rydberg_graph_encoder_decoder
def get_rydberg_graph_encoder_decoder(config): # rydberggpt/models/rydberg_encoder_decoder.py
model = RydbergEncoderDecoder(
        encoder=Encoder(),
        decoder=Decoder(),
        src_embed=GraphEmbedding(),
        tgt_embed=nn.Sequential(),
        generator=Generator(),
        config=config,
) # afterwards: Xavier uniform initialization
class RydbergEncoderDecoder(EncoderDecoder):
```
