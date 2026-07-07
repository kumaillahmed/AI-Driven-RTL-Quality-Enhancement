from rtl_ai.ml.features import extract_features

def test_features():
    f = extract_features({"message":"abc","severity":"WARNING"})
    assert f["message_length"] == 3
