import numpy as np

class Transformer:
    def __init__(self):
        pass
    
    def load_model(self):
        pass
    
    def transform_input(self, x=None, names=None, meta=None):
        print("transformer_input")
        if x is not None:
            return x
        else:
            return np.array([[111]])
        
    def predict(self, x=None, names=None, meta=None):
        print("transformer_predict")
        if x is not None:
            return x
        else:
            return np.array([[112]])
        
    def transform_output(self, x=None, names=None, meta=None):
        print("transformer_output")
        if x is not None:
            return x
        else:
            return np.array([[113]])