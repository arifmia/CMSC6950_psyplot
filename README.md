# CMSC6950 - Pymagicc: A Python wrapper for the simple climate model MAGICC

# S M Arifuzzaman

Pymagicc is a Python wrapper around the reduced complexity climate model MAGICC6. It wraps the CC-BY-NC-SA licensed MAGICC6 binary. Pymagicc itself is AGPL licensed.

MAGICC (Model for the Assessment of Greenhouse Gas Induced Climate Change) is widely used in the assessment of future emissions pathways in climate policy analyses, e.g. in the Fifth Assessment Report of the Intergovernmental Panel on Climate Change or to model the physical aspects of climate change in Integrated Assessment Models (IAMs).

See www.magicc.org and Meinshausen et al. 2011 for further information.

# Installation
    pip install pymagicc

    On Linux and OS X the original compiled Windows binary available on http://www.magicc.org/ and included in Pymagicc can run using Wine.

    On modern 64-bit systems one needs to use the 32-bit version of Wine

    sudo dpkg --add-architecture i386
    sudo apt-get install wine32
    On 32-bit systems Debian/Ubuntu-based systems wine can be installed with

    sudo apt-get install wine
    On OS X wine is available in the Homebrew package manager:

    brew install wine
    It should also be available in other package managers, as well as directly from the Wine project.

    Note that after the first install the first run of Pymagicc might be slow due to setting up of the wine configuration and be accompanied by pop-ups or debug output.

    To run an example session using Jupyter Notebook and Python 3 you can run the following commands to create a virtual environment venv and install an editable version for local development:

    git clone https://github.com/openscm/pymagicc.git

    cd pymagicc
    make venv
    ./venv/bin/pip install --editable .
    ./venv/bin/jupyter-notebook notebooks/Example.ipynb