# Read version from installed package
from importlib.metadata import version
__version__ = version("ddatools")

# Populate package namespace
from ddatools.load_data import load_bank, load_credit, load_default, load_hotel, load_ticdata
