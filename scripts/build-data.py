import pandas as pd
import json
import os
from pathlib import Path

all_rows = []
all_columns = []

for excel_file in Path("private-data").glob("*.xlsx"):

    print(f"Processing {excel_file.name}")

    xls = pd.ExcelFile(excel_file)

    for sheet_name in xls.sheet_names:

        df = pd.read_excel(
            excel_file,
            sheet_name=sheet_name
        )

        if not all_columns:
            all_columns = list(df.columns)

        all_rows.extend(
            df.fillna("")
              .to_dict(orient="records")
        )

os.makedirs(
    "assets",
    exist_ok=True
)

output = {
    "columns": all_columns,
    "rows": all_rows
}

with open(
    "assets/data.json",
    "w",
    encoding="utf-8"
) as f:

    json.dump(
        output,
        f,
        ensure_ascii=False
    )

print(
    f"Generated {len(all_rows)} records"
)
