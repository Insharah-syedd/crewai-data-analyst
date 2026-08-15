from crewai.tools import BaseTool
from pydantic import BaseModel, Field
from typing import Type
import pandas as pd
import os


class CSVInfoToolInput(BaseModel):
    file_path: str = Field(
        ...,
        description="The path to the CSV file that needs to be analyzed."
    )


class CSVInfoTool(BaseTool):
    name: str = "csv_info_tool"

    description: str = (
        "Reads a CSV file using pandas and provides detailed information "
        "including rows, columns, data types, missing values, duplicates, "
        "statistics, correlations, and basic data patterns."
    )

    args_schema: Type[BaseModel] = CSVInfoToolInput

    def _run(self, file_path: str) -> str:

        if not os.path.exists(file_path):
            return f"File not found at path: {file_path}"

        try:
            df = pd.read_csv(file_path)

            result = []

            result.append("CSV DATA ANALYSIS")
            result.append("=" * 50)

            result.append(f"Number of rows: {df.shape[0]}")
            result.append(f"Number of columns: {df.shape[1]}")

            result.append("\nColumn names:")
            result.append(", ".join(df.columns.astype(str)))

            result.append("\nData types:")
            result.append(df.dtypes.to_string())

            result.append("\nMissing values:")
            result.append(df.isnull().sum().to_string())

            result.append(
                f"\nDuplicate rows: {df.duplicated().sum()}"
            )

            result.append("\nDescriptive statistics:")
            result.append(df.describe(include="all").to_string())

            numeric_df = df.select_dtypes(include="number")

            if not numeric_df.empty:
                result.append("\nNumerical correlations:")
                result.append(numeric_df.corr().to_string())

            result.append("\nFirst 10 rows:")
            result.append(df.head(10).to_string())

            return "\n".join(result)

        except Exception as e:
            return f"Error analyzing CSV file: {str(e)}"