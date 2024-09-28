import helpers.openai_helper as gpt
from helpers.excel_scraper import ExcelScraper
import helpers.utilities as util
import ast

file_path = "test-data/SUM_USECASE/TEST_SUM.xlsx"
scraper = ExcelScraper(file_path=file_path)

excel_data = scraper.get_matrix()
# print(excel_data)


# print(list(scraper.get_headers()))


prompt = f"""Here is a 2d matrix that represents an excel sheet:
{excel_data}
Return a 2d matrix that adds the values in column 1 and column 2 and in puts the result in column 3 that is titled sum.
return just the 2d matrix with the result and nothing else
"""

# print(prompt)

sum_data_path = "/Users/danvasudevan/projects/excel-generator/test-data/SUM_USECASE"

resulting_excel = gpt.create_completion(prompt=prompt)
matrix_list = ast.literal_eval(resulting_excel)

util.generate_excel(input_matrix=matrix_list, folder_path=sum_data_path, file_name="RESULT_SUM")




