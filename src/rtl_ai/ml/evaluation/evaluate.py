from sklearn.metrics import accuracy_score

def evaluate(y_true,y_pred):
    return {"accuracy":accuracy_score(y_true,y_pred)}
