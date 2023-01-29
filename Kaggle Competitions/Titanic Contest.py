#1# LIBRARIES & CSVs FILES

import numpy as np
import pandas as pd
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.ensemble import RandomForestClassifier



DataTraining = pd.read_csv(r'C:\Users\Nicho\Desktop\Seattle Pacific University\Data Mining\Titanic Competition\train.csv')
DataTesting = pd.read_csv(r'C:\Users\Nicho\Desktop\Seattle Pacific University\Data Mining\Titanic Competition\test.csv')



#2# DATA PREPARATION

def remove_zero_fares(row):
    if row.Fare == 0:
        row.Fare = np.NaN
    return row


DataTraining_Alt = DataTraining.apply(remove_zero_fares, axis=1)   # remove values with no fares at all
DataTesting_Alt = DataTesting.apply(remove_zero_fares, axis=1)


DataTraining_Alt['Title'] = DataTraining_Alt['Name'].apply(lambda x: x.split(',')[1].split('.')[0].strip())
DataTesting_Alt['Title'] = DataTesting_Alt['Name'].apply(lambda x: x.split(',')[1].split('.')[0].strip())


DataTraining_Alt['Title'].replace(['Mme', 'Ms', 'Lady', 'Mlle', 'the Countess', 'Dona'], 'Miss', inplace=True)  # Replace female titles
DataTesting_Alt['Title'].replace(['Mme', 'Ms', 'Lady', 'Mlle', 'the Countess', 'Dona'], 'Miss', inplace=True)


DataTraining_Alt['Title'].replace(['Major', 'Col', 'Capt', 'Don', 'Sir', 'Jonkheer'], 'Mr', inplace=True)  # Replace male titles
DataTesting_Alt['Title'].replace(['Major', 'Col', 'Capt', 'Don', 'Sir', 'Jonkheer'], 'Mr', inplace=True)


DataTraining_Alt['Ticket_let'] = DataTraining_Alt.Ticket.apply(lambda x: x[:2])  # reduced ticket to 2 letters
DataTesting_Alt['Ticket_let'] = DataTesting_Alt.Ticket.apply(lambda x: x[:2])


DataTraining_Alt['Ticket_len'] = DataTraining_Alt.Ticket.apply(lambda x: len(x))  # Ticket length as numeric reference
DataTesting_Alt['Ticket_len'] = DataTesting_Alt.Ticket.apply(lambda x: len(x))


DataTraining_Alt['Fam_size'] = DataTraining_Alt['SibSp'] + DataTraining_Alt['Parch'] + 1   # Creation of a new attribute
DataTesting_Alt['Fam_size'] = DataTesting_Alt['SibSp'] + DataTesting_Alt['Parch'] + 1


DataTraining_Alt['Fam_type'] = pd.cut(DataTraining_Alt.Fam_size, [0,1,4,7,11], labels=['Solo', 'Small', 'Big', 'Very Big'])  # Creation of four groups
DataTesting_Alt['Fam_type'] = pd.cut(DataTesting_Alt.Fam_size, [0,1,4,7,11], labels=['Solo', 'Small', 'Big', 'Very Big'])



#3# DATA PROCESSING

y = DataTraining_Alt['Survived']
features = ['Pclass', 'Fare', 'Title', 'Embarked', 'Fam_type', 'Ticket_len', 'Ticket_let']
x = DataTraining_Alt[features]

numerical_cols = ['Fare']
categorical_cols = ['Pclass', 'Title', 'Embarked', 'Fam_type', 'Ticket_len', 'Ticket_let']


numerical_transformer = SimpleImputer(strategy='median')  # Numerical data

# Categorical data
categorical_transformer = Pipeline(steps=[
    ('imputer', SimpleImputer(strategy='most_frequent')),
    ('onehot', OneHotEncoder(handle_unknown='ignore'))
])

# Bundling
preprocessor = ColumnTransformer(
    transformers=[
        ('num', numerical_transformer, numerical_cols),
        ('cat', categorical_transformer, categorical_cols)
    ])



#4# DATA MODELING

Conduit = Pipeline(steps=[
    ('preprocessor', preprocessor),
    ('model', RandomForestClassifier(random_state=0, n_estimators=500, max_depth=5))
])



#5# EVALUATION & RESULTS

Conduit.fit(x,y)

x_test = DataTesting_Alt[features]

predictions = Conduit.predict(x_test)

output = pd.DataFrame({'PassengerId': DataTesting_Alt.PassengerId, 'Survived': predictions})
output.to_csv('Proof.csv', index=False)







