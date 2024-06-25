# Kobol RSF VCO

## Brief Description
A brief description of the project goes here. Explain the main objective and features of the project.

## Installation

Clone the repository:

```bash
git clone https://github.com/ObiWxnKenxbi/KobolRSF
```

Install the package and its dependencies or create a virtual environment:

### Using the requirements.txt:

```bash
pip install -r requirements.txt
```

### To create a conda environment using the .yml file:

Create the conda environment:
``` bash
conda env create -f conda_env_cpu.yml
```

Activate the conda environment:
```bash
conda activate KobolRSF
```

To remove the environment:

``` bash
conda env remove -n KobolRSF
```

## Usage

The main file is main.py. In there you can run the integrator and get the phases by providing a value for cv (from 0 to 1).

## Folder Structure
``` lua
|-- models
|   |-- PU.h5               # trained periodic unit model
|-- src                     # source code for this project
|   |-- main.py             # main script to access any functionality
|   |-- phaseintegrator.py  # uses the H5 model to generate the angular frequency using the cv, then integrates it with the time steps and returns the folded phases
|-- LICENSE
|-- README.md               # this file
|-- requirements.txt        # requirements to use the code
|-- conda_environment.yml   # conda environment configuration
```

## Contributing
Contributions to this project are welcome! If you find any issues, have suggestions for improvements, or would like to add new features, please submit a pull request.

## Citation
This repository is part of my thesis project for the Masters in Sound and Music Computing at Universitat Pompeu Fabra, Barcelona, Spain. If you use this code, please consider citing the following:

``` bibtex

@masterthesis{sofia_vallejo_2024_pending,
  author       = {Sofia Vallejo Budziszewski},
  title        = {{Title Pending}},
  school       = {Universitat Pompeu Fabra},
  year         = 2024,
  month        = jul,
  doi          = {pending},
  url          = {pending}
}

```

## TODO
Finish the FFNN to predict the waveform data.
Implement the real-time functionality.
