import pandas as pd

class AnimeDataLoader:
    def __init__(self, original_csv:str, processed_csv:str):
        self.original_csv = original_csv
        self.processed_csv = processed_csv
        
    def load_and_process(self):
        df = pd.load_csv(self.original_csv, encoding="utf-8", error_bad_line=False).dropna()
        
        # Check for missing column
        required_columns = ["Name", "Genres", "sypnopsis"]
        missing_columns = required_columns - set(df.columns)
        if missing_columns:
            raise ValueError("Missing column in csv file")
        
        # Combine the required columns into one,
        # And save it into new csv file
        df['combined_info'] = [
            "Title: " + df["Name"] + " Overview: " +df["sypnopsis"] + " Genres: " + df["Genres"]
        ]

        df[["combined_info"]].to_csv(self.processed_csv, encoding="utf-8", index=False)
        
        return self.processed_csv