from .model import FalsePositiveClassifier

def train_demo():
    texts = [
        "Unused signal",
        "Width mismatch",
        "False positive rule"
    ]
    labels = [0,1,0]
    clf = FalsePositiveClassifier()
    clf.fit(texts, labels)
    return clf
