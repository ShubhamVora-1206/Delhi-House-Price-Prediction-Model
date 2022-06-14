import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)

dat = pd.read_csv(r'C:\Users\acer\Downloads\MagicBricks.csv')
# dat.head()
# dat.info()
# dat.describe()
#get_ipython().run_line_magic('matplotlib', 'inline')
import matplotlib.pyplot as plt
#dat.hist(bins = 50, figsize = (20,15))
#save_fig("att_hist_plots")
#plt.show()
dat.isnull().sum()
import seaborn as sns
#sns.regplot(y = 'Area', x = 'Price', data = dat)
pd.options.mode.chained_assignment = None
dat["Per_Sqft"] = dat["Per_Sqft"].fillna(value = dat["Price"]/dat["Area"])
dat["Bathroom"] = dat["Bathroom"].fillna(value = dat["Bathroom"].median())
dat_f = dat
dat_f.isnull().sum()
dat_f = dat
# dat_f.head(10)
from sklearn.preprocessing import LabelEncoder
or_enc = LabelEncoder()
#dat_f = dat_f.dropna()
dat_f["Type"] = or_enc.fit_transform(dat_f["Type"].astype('str'))
dat_f["Locality"] = or_enc.fit_transform(dat_f["Locality"].astype('str'))
dat_f["Status"] = or_enc.fit_transform(dat_f["Status"])
dat_f["Transaction"] = or_enc.fit_transform(dat_f["Transaction"])
#dat_f.head()
dat = dat.drop_duplicates()
#dat.head()
sns.heatmap(dat_f.corr(),annot=True)
sns.heatmap(dat.corr(), annot=True)
from sklearn.preprocessing import StandardScaler
scaler=StandardScaler()
X = dat_f.drop(columns=['Price', 'Furnishing', 'Parking'])
tmp = dat_f.drop(columns=['Furnishing', 'Parking'])
tmp.isnull().sum()
y=dat_f['Price'].values
for i in y:
    if(pd.isna(i)):
        print("aaa")
from sklearn.model_selection import train_test_split
X_train,X_test,y_train,y_test=train_test_split(X,y,train_size=0.9,random_state=2)
# print(X_train.shape)
# print(X_test.shape)
# print(y_train.shape)
# print(y_test.shape)
from sklearn.ensemble import RandomForestRegressor
rf= RandomForestRegressor(n_estimators=100,random_state=0)
rf.fit(X_train, y_train)
y_pred1=rf.predict(X_test)
#r2_score(y_test,y_pred1) 
user = [[750.0,2,2.0,139,1,0,0,6667.0]]
#print(user[0][1])
userdf = pd.DataFrame(data= user)
pred2 =rf.predict(user)
pred2
#new_input=list(input().split())
# new_input=[750.0,2,2.0,139,1,0,0,6667.0]
# user[0][0] = float(new_input[0])
# user[0][1] = int(new_input[1])
# user[0][2] = float(new_input[2])
# user[0][3] = int(new_input[3])
# user[0][4] = int(new_input[4])
# user[0][5] = int(new_input[5])
# user[0][6] = int(new_input[6])
# user[0][7] = float(new_input[7])
# pred = rf.predict(user)
# print(pred[0])
