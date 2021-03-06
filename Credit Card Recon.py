# import pandas as pd
import pandas as pd

# read CSV files
Ascend_Pre = pd.read_csv('Ascend.csv')
CyberSource_Pre = pd.read_csv('CyberSource.csv')

#Rename column in CyberSource file so we can set a key
CyberSource_Pre = CyberSource_Pre.rename(columns={'Merchant Reference Number':'External Payment Gateway ID'})

#Join files based on the key, return rows from CyberSource that appear in Ascend, save as new file
inner_join = pd.merge(CyberSource_Pre, Ascend_Pre, on = 'External Payment Gateway ID', how = 'inner')

#Delete rows containing 'Fail' or 'Reversal' in the 'Applications' column
inner_join = inner_join[~inner_join.Applications.str.contains("Fail")]
inner_join = inner_join[~inner_join.Applications.str.contains("Reversal")]

#Select columns to display
inner_join = inner_join[['Date and Time', 'External Payment Gateway ID', 'Last Name', 'First Name', 'Email',
                         'Amount', 'Currency', 'Applications', 'Payment Method', 'Transaction Reference Number',
                         'Authorization Code', 'Billing Address1', 'Billing City', 'Billing State', 'Billing Postal Code',
                         'Billing Country', 'Appeal']]

#Save csv file to drive
inner_join.to_csv('W:/CC Recon - Pre CyberSource/Inner_join.csv')

print(inner_join)


#print(type(CyberSource_Pre))
#print(type(Ascend_Pre))
