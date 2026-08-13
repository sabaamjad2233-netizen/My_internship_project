def apply_confidence_filter(df, threshold=0.80):
    # Agar confidence 80% (0.80) se kam hai toh usko Review ke liye mark kar do
    df['filtered_prediction'] = df.apply(
        lambda row: row['predicted'] if row['confidence'] >= threshold else 'Needs Manual Review', 
        axis=1
    )
    
    # Stats calculate karna
    accepted = df[df['filtered_prediction'] != 'Needs Manual Review']
    flagged = df[df['filtered_prediction'] == 'Needs Manual Review']
    
    print("=== CONFIDENCE FILTERING ===")
    print(f"Threshold Set: {threshold * 100}%")
    print(f"Accepted Predictions: {len(accepted)}")
    print(f"Flagged for Manual Review: {len(flagged)}\n")
    
    return df