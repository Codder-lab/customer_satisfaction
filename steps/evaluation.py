import logging
import pandas as pd
from zenml import step

@step
def evaluate_model(df: pd.DataFrame) -> None:
    """
    Evaluates the model on the ingested data.
    Args:
        df: The ingested data.
    """
    pass