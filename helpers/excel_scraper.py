import pandas as pd

class ExcelScraper:
    def __init__(self, file_path: str):
        """
        Initialize the ExcelScraper with the path to the Excel file.
        """
        self.file_path = file_path
        self.data = None
        # self.sheet_names = None
        self.load_excel() 

    def load_excel(self):
        """
        Load the Excel file and get the sheet names.
        """
        try:
            self.data = pd.ExcelFile(self.file_path)
            # print(self.data)
            # self.sheet_names = self.data.sheet_names
            # print(f"Excel file loaded successfully. Available sheets: {self.sheet_names}")
        except Exception as e:
            print(f"Error loading Excel file: {e}")

    def parse_excel(self):
        """
        Print out loaded excel to console
        """
        # Loop through the sheets and print their data
        # df_list = []
        # for sheet in self.data.sheet_names:
            # print(f"\nData from sheet: {sheet}")
            # Parse the sheet into a DataFrame
        df = self.data.parse()
            # Print the DataFrame
            # df_list.append(df)
        return df

    def get_headers(self):
        df = self.data.parse()
        header_names = df.columns
        return header_names
    
    def get_matrix(self):
        """Convert Data Frame to 2d matrix format"""
        ret = []
        ret.append(list(self.get_headers()))
        parsed_data = self.parse_excel()

        for index, row in parsed_data.iterrows():
            curr_dict = row.to_dict()
            ret.append(list(curr_dict.values()))

        return(ret)


    # def get_sheet(self, sheet_name):
    #     """
    #     Retrieve a specific sheet by name as a DataFrame.
    #     """
    #     if sheet_name in self.sheet_names:
    #         return pd.read_excel(self.file_path, sheet_name=sheet_name)
    #     else:
    #         print(f"Sheet '{sheet_name}' not found.")
    #         return None

    # def find_value(self, sheet_name, value):
    #     """
    #     Search for a specific value in the sheet.
    #     """
    #     sheet = self.get_sheet(sheet_name)
    #     if sheet is not None:
    #         result = sheet.isin([value])
    #         rows, cols = result.any(axis=1), result.any(axis=0)
    #         if rows.any() and cols.any():
    #             return sheet[rows]
    #         else:
    #             print(f"Value '{value}' not found in sheet '{sheet_name}'.")
    #     return None

    # def scrape_range(self, sheet_name, start_row, end_row, start_col, end_col):
    #     """
    #     Retrieve data from a specific range in the sheet.
    #     """
    #     sheet = self.get_sheet(sheet_name)
    #     if sheet is not None:
    #         return sheet.iloc[start_row:end_row, start_col:end_col]
    #     return None
