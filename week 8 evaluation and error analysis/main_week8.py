import pandas as pd
from error_analysis import perform_error_analysis
from confidence_filter import apply_confidence_filter

# 1. CSV File load karna
df = pd.read_csv('data/test_data.csv')

# 2. Error Analysis Chalao
errors, fp, sarcasm, ambiguous = perform_error_analysis(df)

# 3. Confidence Filter Chalao
filtered_df = apply_confidence_filter(df, threshold=0.80)

# 4. CSV Files Mein Output Save Karna
filtered_df.to_csv('reports/final_output.csv', index=False)
fp.to_csv('reports/false_positives.csv', index=False)
sarcasm.to_csv('reports/sarcasm_cases.csv', index=False)

print("Done! All report files updated successfully.")