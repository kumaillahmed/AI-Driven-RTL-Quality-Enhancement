import pandas as pd
from rtl_ai.ml.features.feature_engineering import build_features

def test_features():
    df=pd.DataFrame({"a":[1]})
    assert build_features(df).shape[0]==1
