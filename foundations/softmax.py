import numpy as np
from numpy.typing import NDArray


class Solution:

    def softmax(self, z: NDArray[np.float64]) -> NDArray[np.float64]:
        # z is a 1D NumPy array of logits
        # Hint: subtract max(z) for numerical stability before computing exp
        # return np.round(your_answer, 4)
        m = max(z)
        res = [math.exp(x-m) for x in z]
        s = sum(res)
        res = [round(x/s,4) for x in res]
        return res
    
