from rtl_ai.ml.train import train_demo

def test_training():
    model = train_demo()
    assert model is not None
