class Solution:
    def get_minimizer(self, iterations: int, learning_rate: float, init: int) -> float:
        # Objective function: f(x) = x^2
        x = init
        # Derivative:         f'(x) = 2x
        for _ in range(iterations):
        # Update rule:       x = x - learning_rate * f'(x)
         d = 2*x
         x = x-learning_rate*d
        # Round final answer to 5 decimal places
        x = round(x,5)
        return x
