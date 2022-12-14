# GeoCAT Tutorials

[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/NCAR/geocat-tutorials/main) [![Documentation Status](https://readthedocs.org/projects/geocat-tutorials/badge/?version=latest)](https://geocat-tutorials.readthedocs.io/en/latest/?badge=latest)

Tutorial content for GeoCAT software

## Running the Tutorials

| **Method** | **Set Up** | **Description** |
|---|---|---|
| Binder | [![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/NCAR/geocat-tutorials/main) | Run the tutorial on binder without needing any local set up |
| Local install |  [Instructions](#Local-installation-instructions)|Download the tutorial notebooks and install the necessary packages (via `conda`) locally. Setting things up locally can take a few minutes, so we recommend going through the installation steps prior to the tutorial.  |

## See pre-run notebooks

You can view fully rendered notebooks at the GeoCAT Tutorials [documentation pages](https://geocat-tutorials.readthedocs.io/en/latest/).

## Local installation instructions

1. Clone the repository

    First clone this repository to your local machine via:

    ```bash
    git clone https://github.com/NCAR/geocat-tutorials
    ```

2. Create a conda environment

    Navigate to the `geocat-tutorials/` directory and create a new conda environment with:

    ```bash
    cd geocat-tutorials
    conda env create -f environment.yml
    ```

    This will create a new conda environment named `geocat-tutorials`.

3. Activate the environment

    Next, activate your new environment with:

    ```bash
    conda activate geocat-tutorials
    ```

4. Launch

    Finally, launch jupyter locally with:

    ```bash
    jupyter lab
    ```

    and navigate to the `notebooks/` directory to view the tutorial notebooks.
