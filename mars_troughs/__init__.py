from .accumulation_model import (
    ACCUMULATION_MODEL_MAP,
    AccumulationModel,
    Linear_Insolation,
    Linear_Obliquity,
    Quadratic_Insolation,
)
from .datapaths import DATAPATHS
from .lag_model import LAG_MODEL_MAP, ConstantLag, LagModel, LinearLag
from .model import Model
from .trough import Trough

__author__ = [
    "Tom McClintock <thmsmcclintock@gmail.com>",
    "Kristel Izquierdo <kristell.izquierdo@gmail.com>",
    "Kris Laferriere <klaferri@purdue.edu>",
]
__version__ = "0.0.1"
__docs__ = "Simulating martian ice troughs."
