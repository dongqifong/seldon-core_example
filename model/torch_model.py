# -*- coding: utf-8 -*-
"""
Created on Fri Nov 18 19:27:59 2022

@author: henry
"""

import joblib
import numpy as np
from sklearn.base import BaseEstimator, RegressorMixin
import torch
import torch.nn as nn
import torch.nn.functional as F

class TorchModel(BaseEstimator, RegressorMixin, nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = nn.Linear(3, 1)
        
    def forward(self, x):
        x = torch.Tensor(x)
        x = self.linear(x)
        x = F.sigmoid(x)
        return x
    
    def fit(self,x,y=None):
        return self
    
    def predict(self,x,y=None):
        y = self.forward(x)
        return y.detach().numpy().reshape(-1)

# if __name__ == "__main__":
#     np.random.seed(0)
#     m = TorchModel()
#     joblib.dump(m,"torch_model.joblib")
#     x = np.random.random((1,3))

#     y = m.predict(x)
#     print(y) # [0.50667244]
    
#     model = joblib.load("torch_model.joblib")
#     y_model = model.predict(x)
#     print(y_model) # [0.50667244]
