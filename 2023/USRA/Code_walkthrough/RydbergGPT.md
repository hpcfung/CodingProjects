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
## Usage

### data
it looks like the names of subfolders in `data` do not have any restrictions?  
`def read_subfolder_data` in `rydberggpt/data/loading/utils.py`  
`for folder in os.listdir(data_path):`  
it just reads into dataframe and append `data` (list)

## L
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

Training is just a one-liner
```
trainer.fit(model=MLP, train_dataloaders=train_dataloader, val_dataloaders=test_dataloader)
```

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
is `forward` method necessary? doesn't show up above, which is from  
https://lightning.ai/docs/pytorch/stable/starter/introduction.html#define-a-lightningmodule  
but shows up here?  
https://lightning.ai/docs/pytorch/stable/common/lightning_module.html#starter-example
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
pass reference to class instance: only runs `def __init__():`  
so `RydbergEncoderDecoder` basically wrapper for `def __init__():` in `EncoderDecoder`  
`EncoderDecoder` subclass of `pl.LightningModule`; makes sense, necessary for pytorch lightning models
```
class EncoderDecoder(pl.LightningModule): # rydberggpt/models/transformer/models.py
```

https://docs.python.org/3/library/functions.html#super
```
class C(B):
    def method(self, arg):
        super().method(arg)
```
does the same thing as `super(C, self).method(arg)`  
https://stackoverflow.com/questions/14743787/python-superclass-self-method-vs-superparent-self-method

note `class EncoderDecoder(pl.LightningModule):` no `training_step()` method, only `forward`, `encode`, `decode`

```
trainer.fit(rydberg_gpt_trainer, train_loader, val_loader)
rydberg_gpt_trainer = RydbergGPTTrainer()
from rydberggpt.training.trainer import RydbergGPTTrainer
class RydbergGPTTrainer(pl.LightningModule): # rydberggpt/training/trainer.py
```
`forward` is basically a wrapper for `class EncoderDecoder(pl.LightningModule):`
```
out = self.model.forward(m_onehot, cond)
cond_log_probs = self.model.generator(out)
return cond_log_probs
```
note that `model.forward` followed by `model.generator`  
so technically `trainer.fit(model=rydberg_gpt_trainer, train_loader, val_loader)`  
So the model is implemented as two different `pl.LightningModule` classes. `EncoderDecoder` is pure model architecture, `RydbergGPTTrainer` is combined model plus training step.

