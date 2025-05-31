from __future__ import annotations
import numpy as np
import statsmodels.api as sm
from typing import Tuple

def val_prob(probs: np.ndarray, y: np.ndarray, frac: float = 0.3) -> Tuple[np.ndarray, np.ndarray]:
    """
    Perform lowess calibration on predicted probabilities.

    Lowess calibration smooths predicted probabilities using locally weighted scatterplot smoothing,
    which helps in refining predictions to match observed outcomes more closely.

    Parameters
    ----------
    probs : np.ndarray
        Predicted probabilities from a model (1D array).
    y : np.ndarray
        Binary response variables (0s and 1s), must have the same length as `probs`.
    frac : float
        The fraction of data used for lowess. Default is 0.3. Must be between 0 and 1.

    Returns
    -------
    Tuple[np.ndarray, np.ndarray]
        Original probabilities and smoothed probabilities using lowess.
    
    Example
    -------
    from ddatools import val_prob
    probs = np.array([0.1, 0.4, 0.8])
    y = np.array([0, 1, 1])
    original, smoothed = val_prob(probs, y, frac=0.3)

    Note: The smoothed probabilities might not be in the same order as the input probabilities 
    depending on the sorted output from lowess.
    """
    
    # Convert inputs to numpy arrays
    probs = np.asarray(probs)
    y = np.asarray(y)
    
    # Validate `frac` value
    if not (0 < frac < 1):
        raise ValueError("`frac` must be between 0 and 1.")

    # Check for empty arrays
    if probs.size == 0 or y.size == 0:
        raise ValueError("`probs` and `y` must not be empty.")

    # Validate input shapes
    if probs.shape != y.shape:
        raise ValueError("`probs` and `y` must have the same shape.")

    # Ensure `y` contains only binary values
    if not np.all(np.isin(y, [0, 1])):
        raise ValueError("`y` must contain only binary values (0s and 1s).")

    # Perform lowess smoothing
    lowess_results = sm.nonparametric.lowess(endog=y, exog=probs, frac=frac, return_sorted=True)

    # Extract sorted smoothed probabilities
    sorted_probs, smoothed_probs = lowess_results[:, 0], lowess_results[:, 1]

    return sorted_probs, smoothed_probs
