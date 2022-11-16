from seldon_core.user_model import SeldonResponse
import project_utils

class ProjectAnalyzer:
    def __init__(self):
        self._transformer = project_utils.Transformer()
        
    
    def predict(self, x=None, names=None,meta=None):
        print("ProjectAnalyzer")
        output = self._transformer.predict(x)
        print(output)
        return SeldonResponse(data=output).data
    
    
    
if __name__ =="__main__":
    import numpy as np
    x = np.random.random((3,5))
    m = ProjectAnalyzer()
    m.predict() 
