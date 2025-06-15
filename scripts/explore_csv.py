import pandas as pd

# Φόρτωση του καθαρισμένου αρχείου
df = pd.read_csv('data/processed/bruse_clean.csv')

print("----- Πρώτες γραμμές -----")
print(df.head(), "\n")

print("----- Πληροφορίες DataFrame -----")
print(df.info(), "\n")

print("----- Κενές τιμές ανά στήλη -----")
print(df.isnull().sum(), "\n")

print("----- Περιγραφικά στατιστικά -----")
print(df.describe())
