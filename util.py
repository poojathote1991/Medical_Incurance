import pickle
import json
import numpy as np
import config
model_file_name=config.MODEL_FILE_PATH
with open(model_file_name,'rb') as f:
    model=pickle.load(f)
json_file_name=config.JSON_FILE_PATH
with open(json_file_name,'r') as f:
    json_data=json.load(f)

def get_predicted_price(age,gender,bmi,children,smoker,region):


    gender=json_data['Gender'][gender]
    smoker=json_data['Smoker'][smoker]
    region="region_"+region
    region_index=json_data['Column Names'].index(region)
    test_array=np.zeros([1,model.n_features_in_])
    test_array[0,0]=age
    test_array[0,1]=gender
    test_array[0,2]=bmi
    test_array[0,3]=children
    test_array[0,4]=smoker
    
    test_array[0][region_index]=1
    predicted_charges=np.around(model.predict(test_array)[0],3)
    return predicted_charges