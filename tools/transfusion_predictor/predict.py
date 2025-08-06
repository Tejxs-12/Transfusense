# tools/transfusion_predictor/predict.py

from datetime import datetime, timedelta
import pandas as pd

def predict_next_transfusion_date(current_date, hemoglobin_level, transfusion_interval):
    """
    Predicts the next transfusion date based on current date, hemoglobin level,
    and typical transfusion interval.

    Parameters:
        current_date (str): The current date in 'YYYY-MM-DD' format.
        hemoglobin_level (float): The patient's current hemoglobin level.
        transfusion_interval (int): Expected interval between transfusions in days.

    Returns:
        str: Predicted next transfusion date in 'YYYY-MM-DD' format, or None if error.
    """
    try:
        current_dt = datetime.strptime(current_date, "%Y-%m-%d")

        # Optional logic: adjust interval based on hemoglobin level
        if hemoglobin_level < 7.0:
            transfusion_interval -= 2
        elif hemoglobin_level > 10.0:
            transfusion_interval += 2

        predicted_date = current_dt + timedelta(days=transfusion_interval)
        return predicted_date.strftime("%Y-%m-%d")

    except Exception as e:
        print(f"[TransfusionPredictor] Error in prediction: {e}")
        return None


def predict_from_csv(csv_path):
    """
    Reads the latest record from the CSV and predicts the next transfusion date.

    Assumes the CSV has columns: 'date', 'hemoglobin', 'interval'

    Returns:
        str: Predicted date or None if error.
    """
    try:
        df = pd.read_csv(csv_path)

        if df.empty:
            raise ValueError("CSV file is empty.")

        # Use the last row
        latest = df.iloc[-1]

        current_date = str(latest['date']).strip()
        hemoglobin = float(latest['hemoglobin'])
        interval = int(latest['interval'])

        return predict_next_transfusion_date(current_date, hemoglobin, interval)

    except Exception as e:
        print(f"[TransfusionPredictor] Failed to read from CSV: {e}")
        return None

def predict_from_summary(summary_text):
    """
    Parses the summary to extract last transfusion date and estimate the next one.

    Returns:
        str: Predicted next date or error message.
    """
    import re
    from datetime import datetime, timedelta

    # Try to extract a date in YYYY-MM-DD or DD-MM-YYYY format
    date_patterns = [
        r"\b(\d{4}-\d{2}-\d{2})\b",   # YYYY-MM-DD
        r"\b(\d{2}-\d{2}-\d{4})\b"    # DD-MM-YYYY
    ]

    for pattern in date_patterns:
        match = re.search(pattern, summary_text)
        if match:
            date_str = match.group(1)
            try:
                # Try both formats
                if "-" in date_str and len(date_str.split("-")[0]) == 4:
                    last_date = datetime.strptime(date_str, "%Y-%m-%d")
                else:
                    last_date = datetime.strptime(date_str, "%d-%m-%Y")

                # Use default interval of 21 days
                next_date = last_date + timedelta(days=21)
                return next_date.strftime("%Y-%m-%d")

            except Exception as e:
                return f"Error parsing date: {e}"

    return "No valid transfusion date found in summary."
