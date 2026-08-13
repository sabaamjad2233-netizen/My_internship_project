import pandas as pd

def perform_error_analysis(df):
    # 1. Total errors nikalna (jahan actual aur predicted match na hon)
    errors = df[df['actual'] != df['predicted']].copy()
    
    # 2. False Positives (Actual Negative '0' tha, par model ne Positive '1' bol diya)
    false_positives = errors[(errors['actual'] == 0) & (errors['predicted'] == 1)]
    
    # 3. Sarcasm / Taana (Khas words jaise 'great', 'wow', 'thanks' ho par actual text negative ho)
    sarcastic_words = ['great', 'awesome', 'thanks', 'wonderful', 'perfect', 'love']
    sarcasm_cases = false_positives[
        false_positives['text'].str.lower().str.contains('|'.join(sarcastic_words), na=False)
    ]
    
    # 4. Ambiguous Sentiment (Model confidence score 0.45 aur 0.55 ke beech mein phase)
    ambiguous_cases = df[(df['confidence'] >= 0.45) & (df['confidence'] <= 0.55)]
    
    print("=== ERROR ANALYSIS REPORT ===")
    print(f"Total Test Samples: {len(df)}")
    print(f"Total Errors: {len(errors)}")
    print(f"1. False Positives Count: {len(false_positives)}")
    print(f"2. Sarcasm Cases Found: {len(sarcasm_cases)}")
    print(f"3. Ambiguous Sentiment Cases: {len(ambiguous_cases)}\n")
    
    return errors, false_positives, sarcasm_cases, ambiguous_cases