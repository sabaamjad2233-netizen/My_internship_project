import pandas as pd
import joblib
import os
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.metrics import classification_report, accuracy_score, confusion_matrix, precision_recall_fscore_support

def run_evaluation():
    print("\n--- [STEP 4/4] Evaluating Model & Generating Metrics ---")
    df = pd.read_csv('data/cleaned_data.csv')
    test_df = df[df['split'] == 'test'].dropna(subset=['cleaned_review'])
    
    X_test = test_df['cleaned_review']
    y_test = test_df['sentiment']
    
    model = joblib.load('models/sentiment_model.pkl')
    vectorizer = joblib.load('models/vectorizer.pkl')
    
    X_test_vec = vectorizer.transform(X_test)
    y_pred = model.predict(X_test_vec)
    
    acc = accuracy_score(y_test, y_pred)
    precision, recall, f1, _ = precision_recall_fscore_support(y_test, y_pred, average='weighted')
    class_rep = classification_report(y_test, y_pred)
    
    # Save Confusion Matrix Plot
    cm = confusion_matrix(y_test, y_pred, labels=['negative', 'positive'])
    plt.figure(figsize=(5, 4))
    sns.heatmap(cm, annot=True, fmt='d', cmap='Blues', 
                xticklabels=['Negative', 'Positive'], 
                yticklabels=['Negative', 'Positive'])
    plt.xlabel('Predicted')
    plt.ylabel('Actual')
    plt.title('Confusion Matrix')
    plt.tight_layout()
    
    os.makedirs('reports', exist_ok=True)
    plt.savefig('reports/confusion_matrix.png', dpi=150)
    plt.close()
    
    # Write Markdown Evaluation Report
    report_content = (
        "# Sentiment Model Evaluation Report\n\n"
        "## Model: TF-IDF + Logistic Regression\n\n"
        "## Summary Metrics\n"
        f"- **Accuracy:** {acc:.4f}\n"
        f"- **Precision:** {precision:.4f}\n"
        f"- **Recall:** {recall:.4f}\n"
        f"- **F1 Score:** {f1:.4f}\n\n"
        "## Classification Report\n"
        "```text\n"
        f"{class_rep}\n"
        "```\n"
    )
    
    with open('reports/evaluation_report.md', 'w', encoding='utf-8') as f:
        f.write(report_content)
        
    print(f"✓ Accuracy: {acc:.4f}")
    print("✓ Evaluation Report & Confusion Matrix saved in 'reports/'.")

if __name__ == '__main__':
    run_evaluation()