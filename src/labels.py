import pandas as pd

# fixed education order
edu_order = [
    "No schooling",
    "Nursery–Grade 4",
    "Grades 5–8",
    "Grade 9",
    "Grade 10",
    "Grade 11",
    "Grade 12 (HS, no diploma)",
    "1 year of college",
    "2 years of college",
    "3 years of college",
    "4 years of college (Bachelor's)",
    "5+ years of college (Graduate)",
    "Missing"
]

edu_labels = {
        0:"No schooling",
        1:"Nursery–Grade 4",
        2:"Grades 5–8",
        3:"Grade 9",
        4:"Grade 10",
        5:"Grade 11",
        6:"Grade 12 (HS, no diploma)",
        7:"1 year of college",
        8:"2 years of college",
        9:"3 years of college",
        10:"4 years of college (Bachelor's)",
        11:"5+ years of college (Graduate)",
        99:"Missing"
    }

def label_education(df, source_col="EDUC", target_col="EDUC_label"):
    df[target_col] = df[source_col].map(edu_labels)
    df[target_col] = pd.Categorical(df[target_col], categories=edu_order, ordered=True)
    return df