import pandas as pd
df = pd.read_csv("./titanic.csv")


#1. タイタニックデータセットを読み込み、['Age', 'Gender', 'Pclass', 'Fare', 'Survived']列の DataFrame を作成する
# print(df[['Age', 'Gender', 'Pclass', 'Fare', 'Survived']])
# print(df.loc[:,['Age', 'Gender', 'Pclass', 'Fare', 'Survived']])

#データに NaN がある行は DataFrame から除外する。
# df = df.dropna(how='any')
# print(df)

#3. Fare 列の最大値と最小値を Print する。
# print(df['Fare'].max())
# print(df['Fare'].min())

#4. Age が 30 歳以下の人を数える

print(len(df[df['Age'] <= 30]))


#5. DataFrame を Pclass の降順にソートし、結果を Print する。
# print(df.sort_values('Pclass', ascending=False))

#6. 性別ごとに生存者は何人いるか Print する。（Survived == 1 の人数）

survived_count = df["Survived"] == 1
group = df[survived_count].groupby("Gender")
# print(group.size())

#性別ごとに平均年齢を計算して Print する。
# print(df.groupby('Gender')["Age"].mean())
