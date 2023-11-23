import pandas
import sys

df = pandas.read_csv(sys.argv[1])
print("Input CSV:")
print(df.head(5))

# If TransactionType.credit, keep amount
# If TransactionType.debit, negate amount
for index, row in df.iterrows():
    if row['Transaction Type'] == 'credit':
        amount = row['Amount']
    elif row['Transaction Type'] == 'debit':
        amount = -row['Amount']
    df.at[index, 'Amount'] = amount

# Rename columns
df.rename(columns={
    'Date': 'Date',
    'Description': 'Payee',
    'Category': 'Category',
    'Amount': 'Amount'
}, inplace=True)

df = df[['Date', 'Payee', 'Category', 'Amount']]
print("Output CSV:")
print(df.head(5))

# Write to CSV at the directory specified by the second argument (keep filename)
filename = sys.argv[1].split('/')[-1]
df.to_csv(sys.argv[2] + '/' + filename, index=False)
