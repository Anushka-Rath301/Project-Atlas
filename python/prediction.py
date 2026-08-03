import pandas as pd
df=pd.read_csv("D:/Anushka Projects/pandas/clean_dataset.csv")

X=df[["Voltage","Current","Vibration","Temperature"]]
y=df["Health Status"]

from sklearn.model_selection import train_test_split
X_train,X_test,y_train,y_test=train_test_split(X,y,stratify=y,test_size=0.2)

from sklearn.ensemble import RandomForestClassifier
rf=RandomForestClassifier(n_estimators=150,criterion='entropy',max_depth=8,min_samples_split=10,random_state=42,class_weight='balanced')
rf.fit(X_train,y_train)

y_pred=rf.predict(X_test)

from sklearn.metrics import confusion_matrix
print(confusion_matrix(y_test,y_pred))

from sklearn.metrics import classification_report
print(classification_report(y_test,y_pred))

print(rf.feature_importances_)
print('accuracy=',rf.score(X_test,y_test))

print(rf.classes_)
print(rf.predict_proba(X_test))

import joblib
joblib.dump(rf, "motor_health_model.pkl")
print("Model saved successfully!")
