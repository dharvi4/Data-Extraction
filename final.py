import re
import pandas as pd
import numpy as np

file = open("PhoneNumbers.txt" , encoding = "utf-8")

text=file.read()

pattern = r'[91]-[8-9][0-9]-\d{4}-\d{4}'

PhoneNumbers = re.findall(pattern, text)
arr = np.array(PhoneNumbers)

for i in PhoneNumbers:
    print(i)

df = pd.DataFrame([arr]).T
df.to_csv('phone.csv', index= False)

print(df)
