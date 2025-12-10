import pandas as pd

class AnimeDataLoader:
    def __init__(self, original_csv:str, processed_csv:str):
        self.original_csv = original_csv
        self.processed_csv = processed_csv
        
    def load_and_process(self):
        df = pd.read_csv(self.original_csv, encoding="utf-8").dropna()
        
        # Check for missing column
        required_columns = {"Name", "Genres", "sypnopsis"}
        missing_columns = required_columns - set(df.columns)
        if missing_columns:
            raise ValueError(f"Missing column(s) in csv file: {', '.join(missing_columns)}")
        
        # Combine the required columns into one,
        # And save it into new csv file
        # Create a single combined text column (vectorized concatenation)
        df['combined_info'] = (
            "Title: " + df["Name"].astype(str)
            + " Overview: " + df["sypnopsis"].astype(str)
            + " Genres: " + df["Genres"].astype(str)
        )

        df[["combined_info"]].to_csv(self.processed_csv, encoding="utf-8", index=False)
        
        return self.processed_csv