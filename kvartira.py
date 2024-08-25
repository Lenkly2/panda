from sklearn.model_selection import train_test_split
from sklearn.ensemble import GradientBoostingRegressor
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import mean_absolute_error, r2_score
import numpy as np
import pandas as pd

np.random.seed(42)
count = 1000

age = np.random.uniform(1900,2024,count)
area = np.random.uniform(2,300,count)
rooms = np.random.uniform(1,15,count)
distance = np.random.uniform(1,20,count)


price = (area * 1000 ) + (rooms * 5000) + (age) - (distance * 2000) 

data = pd.DataFrame({
    
"Area": area,
    "Rooms": rooms,
    "Distance": distance,
    "Age": age,
    "Price": price
})

x = data.drop("Price", axis=1)
y = data["Price"]

x_train,x_test,y_train,y_test = train_test_split(x,y,test_size=0.2, random_state=42)

sc = StandardScaler()
x_train = sc.fit_transform(x_train)
x_test = sc.transform(x_test)

model = GradientBoostingRegressor(n_estimators= 100, random_state= 42)
model.fit(x_train,y_train)

prediction = model.predict(x_test)

new_data = pd.DataFrame({
    "Area": [100],
    "Rooms": [3],
    "Distance": [1],
    "Age": [2000]

})

final_data = sc.transform(new_data)

prediction = model.predict(final_data)
print("priced",prediction[0],"$")