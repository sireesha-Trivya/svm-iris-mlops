import joblib
import pandas as pd

from sklearn.datasets import load_iris
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC

# ----------------------------------------------------
# Load Dataset
# ----------------------------------------------------

iris = load_iris()

X = pd.DataFrame(
    iris.data,
    columns=iris.feature_names
)

y = iris.target

print("=" * 60)
print("IRIS DATASET LOADED")
print("=" * 60)

print(f"Features Shape : {X.shape}")
print(f"Labels Shape   : {y.shape}")

# ----------------------------------------------------
# Train Test Split
# ----------------------------------------------------

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

print("\nTraining Samples :", len(X_train))
print("Testing Samples  :", len(X_test))

# ----------------------------------------------------
# Train Model
# ----------------------------------------------------

model = SVC(kernel="linear")

model.fit(X_train, y_train)

print("\nModel Training Completed")

# ----------------------------------------------------
# Prediction
# ----------------------------------------------------

predictions = model.predict(X_test)

# ----------------------------------------------------
# Evaluation
# ----------------------------------------------------

accuracy = accuracy_score(y_test, predictions)

print("\nAccuracy")
print(f"{accuracy:.2%}")

print("\nClassification Report")
print(classification_report(y_test, predictions))

print("\nConfusion Matrix")
print(confusion_matrix(y_test, predictions))

# ----------------------------------------------------
# Save Model
# ----------------------------------------------------

joblib.dump(model, "model/svm_model.joblib")

print("\nModel Saved Successfully!")
print("Location : model/svm_model.joblib")
