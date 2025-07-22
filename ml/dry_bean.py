import pandas as pd
from sklearn import tree 
from sklearn.metrics import classification_report
from sklearn.model_selection import train_test_split
model = None 

data = pd.read_csv('/Users/catherinepan/Downloads/DryBeanDataset/Dry_Bean_Dataset.csv')
print(data.head())

model = tree.DecisionTreeClassifier()

X_df = data.iloc[:,:-1]
y_df = data['Class']
X_train, X_test, y_train, y_test = train_test_split(
    X_df, y_df, test_size=0.3, random_state=42
    )

model.fit(X_df, y_df)
# tree.plot_tree(model)

y_pred = model.predict(X_test)
print(classification_report(y_test, y_pred))