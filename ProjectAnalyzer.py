from seldon_core.user_model import SeldonResponse
import project_utils

import logging 
logging.basicConfig(level=logging.DEBUG,format='%(asctime)s - %(levelname)s : %(message)s',filename='./logging/mylog_analyzer.txt')

class ProjectAnalyzer:
    def __init__(self):
        self._transformer = project_utils.Transformer()
        
    
    def predict(self, x=None, names=None,meta=None):
        print("ProjectAnalyzer")
        logging.debug("ProjectAnalyzer predict")
        output = self._transformer.predict(x)
        print(output)
        logging.debug("ProjectAnalyzer predict completed")
        
        logging.debug("ProjectAnalyzer SeldonResponse")
        out = SeldonResponse(data=output)
        logging.debug("ProjectAnalyzer SeldonResponse completed")
        return out
