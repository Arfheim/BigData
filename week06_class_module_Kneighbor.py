#import matplotlib.pyplot as plt
#import numpy as np
import pandas as pd
#from sklearn.linear_model import LinearRegression
import tkinter as tk
from sklearn.neighbors import KNeighborsRegressor

def predict_life_satisfaction(*ev) :
    x = int(en_GDP_per_capita.get())
    X_new = [[x]]

    life_satisfaction = pd.read_csv("https://github.com/ageron/data/raw/main/lifesat/lifesat.csv")
    X = life_satisfaction[["GDP per capita (USD)"]].values
    y = life_satisfaction[["Life satisfaction"]].values
    print(life_satisfaction)
    # life_satisfaction.plot(kind='scatter', grid=True,
    #              x="GDP per capita (USD)", y="Life satisfaction")
    # plt.axis([23_500, 62_500, 4, 9])
    # plt.show()

    model = KNeighborsRegressor(n_neighbors=3)

    model.fit(X, y)

    lbl_life_satisfaction.config(text=f"해당 국가의 삶의 만족도는 {model.predict(X_new)}로 예측됩니다.")

if __name__ == "__main__":


    window = tk.Tk()
    window.title("삶의 만족도 예측 프로그램 v0.1")
    window.geometry("400x150")

    lbl_life_satisfaction = tk.Label(text="아래 입력상자에 삶의 만족도를 알고 싶은\n국가의 1인당 GDP값을 입력하세요")
    en_GDP_per_capita = tk.Entry(window)
    btn_predict = tk.Button(window, text="예측", command=predict_life_satisfaction)

    lbl_life_satisfaction.pack()
    en_GDP_per_capita.pack(fill='x')
    btn_predict.pack(fill='x')

    en_GDP_per_capita.bind("<Return>",predict_life_satisfaction)
    en_GDP_per_capita.focus()

    window.mainloop()
