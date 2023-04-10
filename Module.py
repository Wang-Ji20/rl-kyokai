import torch
from torch import nn

import HyperParameters

class Module(nn.Module, HyperParameters):
    def __init__(self):
        super().__init__()

    def loss(self, y_hat, y):
        raise NotImplementedError

    def forward(self, X):
        assert hasattr(self, 'net'), 'no network!'
        return self.net(X)

    def training_step(self, batch):
        l = self.loss(self(*batch[:-1]), batch[-1])
        return l

    def validation_step(self, batch):
        l = self.loss(self(*batch[:-1]), batch[-1])

    def configure_optimizers(self):
        raise NotImplementedError