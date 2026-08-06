import os
import pandas as pd
from src.preprocessor import TextPreprocessor
from src.extractor import KeywordExtractor

def start():
    prep = TextPreprocessor()
    ext = KeywordExtractor()
    
    file_path = os.path.join("data", "posts.txt")
    output_txt_path = os.path.join("data", "output.txt")
    
    if not os.path.exists(file_path):
        print("Error: posts.txt file nahi mili!")
        return

    with open(file_path, "r", encoding="utf-8") as f:
        posts = [line.strip() for line in f if line.strip()]

    data = []
    txt_lines = []

    print("\n--- WEEK 5: KEYWORD EXTRACTION RESULT ---\n")

    for idx, post in enumerate(posts, 1):
        tokens = prep.tokenize_and_clean(post)
        keywords = ext.get_keywords(post)
        
        # Terminal & Text Output Formatting
        res = f"[Post {idx}]: {post}\nClean Tokens: {tokens}\nExtracted Keywords: {keywords}\n" + "-"*50 + "\n"
        print(res)
        txt_lines.append(res)
        
        # CSV Data Collection
        data.append({"Post": post, "Keywords": ", ".join(keywords)})

    # data/output.txt Update Karein
    with open(output_txt_path, "w", encoding="utf-8") as f:
        f.writelines(txt_lines)

    # output/keywords.csv Save Karein
    os.makedirs("output", exist_ok=True)
    pd.DataFrame(data).to_csv("output/keywords.csv", index=False)
    
    print("Assignment Completed Successfully!")
    print("Updated Files: 'data/output.txt' & 'output/keywords.csv'\n")

if __name__ == "__main__":
    start()