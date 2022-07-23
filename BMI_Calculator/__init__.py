'''
    Python program to calculate the BMI of the Json data attached in same package
'''
import pandas as pd
# Read the Json data with file name BMI_data.json from same folder.
data_json=pd.read_json('BMI_data.json')

'''
    Funtion to calcuate the BMI and count of overWeight
'''
def BMI_calci(data_json):
    #Create and empyt list of BMI_Category and Health_Risk
    BMI_Category=[]
    Health_Risk=[]
    overWeight_Count=0
    #Calcuate BMI using the fromula and add as new column in dataframe data_json
    data_json['BMI']=data_json.WeightKg/(data_json.HeightCm/100)
    #mplementing switch case using ifelse to find BMI_Category and Health_Risk
    for i in range(len(data_json)):
      if(data_json.BMI[i]<=18.4):
        BMI_Category.insert(i,'Underweight')
        Health_Risk.insert(i,'Malnutrition risk')
      elif(data_json.BMI[i]>=18.5 and  data_json.BMI[i]<=24.9):
        BMI_Category.insert(i,'Normla weight')
        Health_Risk.insert(i,'Low risk')
      elif(data_json.BMI[i]>=25 and  data_json.BMI[i]<=29.9):
        BMI_Category.insert(i,' Overweight')
        Health_Risk.insert(i,'Enhanced risk')
        #Increment the count of overWeight_Count when BMI_Category is Overweight
        overWeight_Count+=1
      elif(data_json.BMI[i]>=30 and  data_json.BMI[i]<=34.9):
        BMI_Category.insert(i,'Moderately Obese')
        Health_Risk.insert(i,'Medium risk')
      elif(data_json.BMI[i]>=35 and  data_json.BMI[i]<=39.9):
        BMI_Category.insert(i,'Severely weight')
        Health_Risk.insert(i,'High risk')
      else:
        BMI_Category.insert(i,'Very severely obese')
        Health_Risk.insert(i,'Very high risk')
    data_json.insert(4,'BMI_Category',BMI_Category)
    data_json.insert(5,'Health_Risk',Health_Risk)
    return data_json,overWeight_Count


 
data_json,overWeight_Count=BMI_calci(data_json)
print(" *** BMI *** \n", data_json)
print("Over Weight Count = ",overWeight_Count)
