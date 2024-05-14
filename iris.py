# 基本ライブラリ
import streamlit as st
import numpy as np
import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.datasets import load_iris


# データセットの読み込み
iris = load_iris()
df = pd.DataFrame(iris.data, columns=iris.feature_names)

# 目標値
df['target'] = iris.target

# 目標値を数字から花の名前に変更
df.loc[df['target'] == 0, 'target'] = 'setona'
df.loc[df['target'] == 1, 'target'] = 'versicolor'
df.loc[df['target'] == 2, 'target'] = 'virginica'

# 予測モデル構築
x = iris.data[:, [0,2]]
y = iris.target

# ロジスティック回帰
clf = LogisticRegression()
clf.fit(x, y)


# サイドバー(入力画面)
st.sidebar.header('Input Features')
sv = st.sidebar.slider('sepal length (cm)', min_value=0.0, max_value=10.0, step=0.1)
pv = st.sidebar.slider('petal length (cm)', min_value=0.0, max_value=10.0, step=0.1)

# メインパネル
st.title('Iris Classifier')
st.write('## Input Value')

# インプットデータ（１行のデータフレーム）
v_df = pd.DataFrame({'data':'data', 'sepal length (cm)':sv, 'petal length(cm)':pv}, index=[0])
v_df.set_index('data', inplace=True)

# 入力値の値
st.write(v_df)

# 予測値のデータフレーム
pred_probs = clf.predict_proba(v_df)
pred_df = pd.DataFrame(pred_probs,columns=['setosa','versicolor','virginica'],index=['probability'])

st.write('## Prediction')
st.write(pred_df)

# 予測結果の出力
name = pred_df.idxmax(axis=1).tolist()
st.write('## Result')
st.write('このアイリスはきっと',str(name[0]),'です!')