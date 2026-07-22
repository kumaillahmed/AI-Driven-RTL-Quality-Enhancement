from rtl_ai.ml.models.false_positive_classifier import create_model

def test_model():
    assert create_model() is not None
