from pathlib import Path

import kagglehub
import pandas as pd

path = kagglehub.dataset_download("yasserhessein/gallstone")
output = Path("data/raw/gallstone.csv")
output.parent.mkdir(parents=True, exist_ok=True)
final_path = Path(path) / "Gallstone_csv.csv"
if not final_path.is_file():
    raise FileNotFoundError(f"Dataset file not found: {final_path}. Try again.")
pd.read_csv(final_path).to_csv(output, index=False)
print(f"Dataset successfully downloaded to {output}")
