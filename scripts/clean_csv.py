import pandas as pd

# Φόρτωση του αρχικού αρχείου από τον φάκελο raw
original_file = 'data/raw/bruse.csv'

# Φόρτωση με διαχωριστικό ελληνικό ερωτηματικό (;)
df = pd.read_csv(original_file, sep=';')

# Αφαίρεση τυχόν κενών γραμμών
df.dropna(how='all', inplace=True)

# Αποθήκευση σε νέο αρχείο processed
clean_file = 'data/processed/bruse_clean.csv'
df.to_csv(clean_file, index=False)

print(f'Το καθαρισμένο αρχείο αποθηκεύτηκε ως: {clean_file}')
print(df.head())
