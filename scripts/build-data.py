import pandas as pd
import json
import os

excel_file = (
    "private-data/"
    "Lactate labeled metabolites.xlsx"
)

all_rows = []

xls = pd.ExcelFile(excel_file)

for sheet_name in xls.sheet_names:

    df = pd.read_excel(
        excel_file,
        sheet_name=sheet_name
    )

    all_rows.extend(
        df.fillna("")
          .to_dict(
              orient="records"
          )
    )

os.makedirs(
    "assets",
    exist_ok=True
)

with open(
    "assets/data.json",
    "w",
    encoding="utf-8"
) as f:

    json.dump(
        all_rows,
        f,
        ensure_ascii=False
    )