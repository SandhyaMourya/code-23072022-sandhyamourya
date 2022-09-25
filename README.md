# code-23072022-sandhyamourya
BMI(Body Mass Index) Calculator

Problem Statement

Given the following JSON data

[{"Gender": "Male", "HeightCm": 171, "WeightKg": 96 },

{ "Gender": "Male", "HeightCm": 161, "WeightKg": 85 },

{ "Gender": "Male", "HeightCm": 180, "WeightKg": 77 },

{ "Gender": "Female", "HeightCm": 166, "WeightKg": 62},

{"Gender": "Female", "HeightCm": 150, "WeightKg": 70},

{"Gender": "Female", "HeightCm": 167, "WeightKg": 82}]

as the input with weight and height parameters of a person, we have to perform the following:

1) Calculate the BMI (Body Mass Index) using Formula 1, BMI Category and Health risk
from Table 1 of the person and add them as 3 new columns

2) Count the total number of overweight people using ranges in the column BMI Category
of Table 1

Formula 1 - BMI

BMI(kg/m2) = mass(kg) / height(m)2

The BMI (Body Mass Index) in (kg/m2) is equal to the weight in kilograms (kg) divided by yourheight in meters squared (m)2.

For example, if you are 175cm (1.75m) in height and 75kg in weight, you can calculate your BMI as follows:

75kg / (1.75m2) = 24.49kg/m2

Table 1 - BMI Category and the Health Risk.

BMI Category   ;     BMI Range (kg/m2); Health risk

Underweight   ;      18.4 and below    ;Malnutrition risk

Normal weight    ;   18.5 - 24.9    ;   Low risk

Overweight       ;   25 - 29.9       ;  Enhanced risk

Moderately obese   ; 30 - 34.9       ;  Medium risk

Severely obese   ;   35 - 39.9        ; High risk

Very severely obese ;40 and above  ;    Very high risk


***Note- Run __init__.py file to get the output if you want to add more data open BMI_data.json file and add few more entries stored BMI_Calcuator folder. ***

......
