import pandas as pd

def load_data(anonymized_path, auxiliary_path):
    anon = pd.read_csv(anonymized_path)
    aux = pd.read_csv(auxiliary_path)
    return anon, aux


def link_records(anon_df, aux_df):
    merged = anon_df.merge(aux_df, on=["age", "zip3", "gender"])
    counts = merged.groupby("anon_id")["name"].transform("count")
    unique = merged[counts == 1]
    return unique[["anon_id", "name"]].rename(columns={"name": "matched_name"})


def deanonymization_rate(matches_df, anon_df):
    return len(matches_df) / len(anon_df)