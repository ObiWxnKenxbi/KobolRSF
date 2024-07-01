# RSF Kobol Synthesizer VCO Dataset

The RSF Kobol Synthesizer VCO dataset focuses on the digital emulation of the analog Voltage-Controlled Oscillator (VCO) to capture and replicate the distinctive qualities of analog sound in a digital format. Analog signals, known for their continuous nature and inherent imperfections, contribute to the warmth and depth of sound, characteristics that are highly prized and challenging to mimic digitally. The dataset aims to model the oscillators of the VCO module accurately.

## Feature Extraction

Features were extracted and saved into a CSV file for use in model training and evaluation. These features include:

- `cv_frequency`: Control voltage value for frequency adjustment.
- `cv_waveform`: Control voltage value for waveform selection.
- `waveform_id`: Identifier for the waveform type.
- `frequency`:  Estimated fundamental frequency of the audio signal using a pitch detection algorithm (`detect_pitch`). This algorithm analyzes the spectral peaks of the waveform to determine the average pitch, providing an estimate of the fundamental frequency.
- `angular_frequency`: Angular frequency calculated from the control voltage.
- `waveform_data`: Raw audio data converted to numerical format.

## Methodology for Feature Extraction

### Control Voltage of Frequency and Waveform Knobs

- The control voltage (CV) is an essential parameter in voltage-controlled oscillators (VCOs).
- For this project, frequency adjustments were made in steps of 0.33 volts and waveform selections in steps of 0.5 volts.

### Waveform Data

- Waveform data was extracted using the wave library.
- This data includes details such as the number of audio channels, sample width, sample rate, and the total number of frames from an audio file.

### Pitch, Loudness, and Angular Frequency

- **Pitch**: Extracted using an algorithm that converts time-domain audio data to its corresponding frequency-domain representation, identifying the fundamental frequency.
- **Loudness**: Computed by analyzing the amplitude of the audio signal, often using a perceptual loudness model that reflects human hearing sensitivity.
- **Angular Frequency**: Derived from the fundamental frequency, it is calculated as \( \omega = 2\pi f \), where \( f \) is the fundamental frequency.

## Dataset Location

The dataset can be found [here](https://www.kaggle.com/datasets/bringmethetxcos/kobolrsf-vco) with more information about the dataset itself and how it was recorded.

## Usage Example

To use the dataset, you can import it from Kaggle and start exploring the features. Heres a simple example in Python:

### Importing the Dataset

First, ensure you have the Kaggle API installed and configured. Then, download the dataset:

```bash
kaggle datasets download -d bringmethetxcos/kobolrsf-vco
unzip kobolrsf-vco.zip -d kobolrsf-vco
```

### Importing the Dataset

```python
import pandas as pd

# Load the CSV file into a DataFrame
df = pd.read_csv('kobolrsf-vco/features.csv')

# Display the first few rows of the dataset
print(df.head())

# Example usage: Plotting the frequency distribution
import matplotlib.pyplot as plt

plt.hist(df['frequency'], bins=50, alpha=0.75)
plt.xlabel('Frequency (Hz)')
plt.ylabel('Count')
plt.title('Frequency Distribution of VCO Outputs')
plt.show()

```

This example demonstrates how to load the dataset and perform a simple analysis by plotting the frequency distribution of VCO outputs.



