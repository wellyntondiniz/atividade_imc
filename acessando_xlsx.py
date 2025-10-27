import pandas as pd

arquivo_excel = "BloodBankDetails.csv"

#Leitura
#df = pd.read_csv(arquivo_excel)

#df = pd.read_csv("BloodBankDetails.csv", sep=';')
#df = pd.read_csv("BloodBankDetails.csv", encoding='ISO-8859-1')
#df = pd.read_csv("BloodBankDetails.csv", header=None)
df = pd.read_csv("BloodBankDetails.csv", usecols=["NAME"])

print(df)

df.to_excel('BloodBankDetails.xlsx', index=False)