import pandas as pd 
from typing import Optional

def preprocess(df: pd.DataFrame, cols: Optional[list] = None) -> pd.DataFrame:

    # df = raw_df.copy()


    if cols is None:
        cols = ["loan_amnt", "term", "int_rate", "installment", 
        "sub_grade", "emp_title", "emp_length", "home_ownership",
        "annual_inc", "verification_status", "loan_status", "purpose", 
        "title", "zip_code", "addr_state", "dti", "earliest_cr_line",
        "open_acc", "pub_rec", "revol_bal", "revol_util", "total_acc", 
        "initial_list_status", "application_type", "mort_acc", "pub_rec_bankruptcies"]

    df = df[cols]

    df = df.loc[df["loan_status"].isin(["Charged Off", "Fully Paid"])]

    df["term"] = df["term"].str.replace(" months", "").astype(int)

    cat = [col for col in df if df[col].dtype == "object"]
    df[cat] = df[cat].apply(lambda x: x.astype("category"))

    df["earliest_cr_line"] = pd.to_datetime(df["earliest_cr_line"]).dt.year.astype(int)

    df

    return df