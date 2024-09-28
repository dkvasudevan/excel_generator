import pandas as pd
import os


def generate_excel(input_matrix: list, folder_path: str, file_name: str) -> None:
    """ Generate an excel file based on the matrix generated by chatGPT result """


    # Create a DataFrame from the 2D matrix
    df = pd.DataFrame(input_matrix[1:], columns=input_matrix[0])

    if ".xlsx" not in file_name:
        file_name = file_name + ".xlsx"

    os.makedirs(folder_path, exist_ok=True)
    
    file_path = os.path.join(folder_path, file_name)

    # Write the DataFrame to an Excel file
    df.to_excel(file_path, index=False)

    print("Excel file has been generated successfully.")
