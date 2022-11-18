import numpy as np
import joblib
from model.torch_model import TorchModel

import logging 
logging.basicConfig(level=logging.DEBUG,format='%(asctime)s - %(levelname)s : %(message)s',filename='./logging/mylog_utils.txt') 

class Transformer:
    def __init__(self):
        pass
    
    def load_model(self):
        print("transfom_load_model")
        logging.debug("load mode") 
        self.model = joblib.load("./model/torch_model.joblib")
        logging.debug("load model completed") 
        return None
    
    def transform_input(self, x=None, names=None, meta=None):
        print("transformer_input")
        logging.debug("transform_input") 
        y = self.model.predict(x)
        logging.debug("transform_input completed")
        print(y)
        return y
        
    def predict(self, x=None, names=None, meta=None):
        print("transformer_predict")
        logging.debug("transformer_predict")
        self.load_model()
        y = self.transform_input(x)
        logging.debug("transformer_predict completed")
        print(y)
        return y
        
    def transform_output(self, x=None, names=None, meta=None):
        print("transformer_output")
        logging.debug("transformer_output")
        self.load_model()
        y = self.transform_input(x)
        logging.debug("transformer_output completed")
        print(y)
        return y
    
    
if __name__ =="__main__":
    trans = Transformer()
    np.random.seed(0)
    y = trans.predict(np.random.random((1,3)))
    print(y)
    