from src.scraper import run_scraper
from src.cleaner import run_cleaner
from src.train_model import run_trainer
from src.evaluate import run_evaluation

def main():
    print("==================================================")
    print("    STARTING COMPLETE SENTIMENT PIPELINE RUN      ")
    print("==================================================")
    
    try:
        run_scraper()
        run_cleaner()
        run_trainer()
        run_evaluation()
        
        print("\n==================================================")
        print(" SUCCESS: ALL PIPELINE STAGES EXECUTED PERFECTLY!")
        print("==================================================")
    except Exception as e:
        print(f"\n❌ Error occurred during pipeline execution: {str(e)}")

if __name__ == '__main__':
    main()