import joblib

class fake_news_model:
    def __init__(self, title, text) -> None:
        self.title = title
        self.text = text

    def isFake(self) -> bool:
        model = joblib.load("model/fake_news_classification.pkl")
        prediction = model.predict([self.title + self.text])
        print(prediction)
        pred_bool = True if prediction[0] == "FAKE" else False
        return pred_bool