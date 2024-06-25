import numpy as np
import matplotlib.pyplot as plt
from keras.models import load_model

model = load_model('PU.h5')

class PhaseIntegrator:
    def __init__(self, cv: float, start_time: float = 0, end_time: float = 200, num_steps: int = 1000):
        """
        Initializes the PhaseIntegrator with the given cv value and time range.

        Args:
            cv (float): The cv value to use for the prediction.
            start_time (float, optional): Start time for the integration. Defaults to 0.
            end_time (float, optional): End time for the integration. Defaults to 200.
            num_steps (int, optional): Number of steps for integration. Defaults to 1000.
        """
        self.cv = cv
        self.start_time = start_time
        self.end_time = end_time
        self.num_steps = num_steps
        self.prediction = self.make_prediction([cv])
        self.time_steps = np.linspace(start_time, end_time, self.num_steps)
        self.first_prediction = self.prediction[0]
        self.integrated_phases = np.zeros_like(self.time_steps)
        self.folded_phases = None
        self.dtype = type(cv)
    
    def make_prediction(self, input_value):
        """
        Makes a prediction based on the input value using the model.

        Args:
            input_value (list): The input value for the prediction.

        Returns:
            np.ndarray: The predicted values.
        """
        input_value = np.array(input_value).reshape(1, -1)
        prediction = model.predict(input_value)
        return prediction
    
    def calculate_first_prediction(self) -> float:
        """
        Calculates the first prediction's integration result.

        Returns:
            float: The result of the integration for the first prediction.
        """
        second_time_step = self.time_steps[1]
        predicted_value = self.first_prediction
        result = second_time_step * predicted_value
        print(f'First Predicted Value: {predicted_value}')
        print(f'Result of integration: {result}')
        return result
    
    def integrate_phases(self) -> None:
        """
        Integrates the phases over the time steps using the first prediction.
        """
        for i, time_step in enumerate(self.time_steps):
            self.integrated_phases[i] = time_step * self.first_prediction
    
    def fold_phases(self) -> None:
        """
        Folds the integrated phases to be within the range [0, 1).
        """
        self.folded_phases = self.integrated_phases % 1.0
    
    def plot_phases(self) -> None:
        """
        Plots the folded phases against the time steps.

        Raises:
            ValueError: If folded phases have not been calculated yet.
        """
        if self.folded_phases is None:
            raise ValueError("Folded phases have not been calculated yet. Call fold_phases() first.")
        plt.figure(figsize=(10, 6))
        plt.plot(self.time_steps, self.folded_phases, label='Integrated Phases')
        plt.xlabel('Time Steps')
        plt.ylabel('Integrated Phases')
        plt.title('Integrated Phases vs Time Steps')
        plt.grid(True)
        plt.legend()
        plt.show()
    
    def run(self) -> None:
        """
        Runs the full phase integration process including calculation, integration,
        folding, and plotting of phases.
        """
        self.calculate_first_prediction()
        self.integrate_phases()
        self.fold_phases()
        self.plot_phases()