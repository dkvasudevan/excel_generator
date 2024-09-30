from fastapi import FastAPI
import helpers.openai_helper as gpt
from helpers.excel_scraper import ExcelScraper
import helpers.utilities as util
import helpers.prompt_generator as pg
import ast
app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.post("/excel")
async def create_excel(user_prompt: str):
    file_path = "test-data/SUM_USECASE/TEST_SUM.xlsx"
    scraper = ExcelScraper(file_path=file_path)
    excel_data = scraper.get_matrix()
    prompt = pg.generate_prompt(excel_data=excel_data, user_prompt= user_prompt)
    sum_data_path = "/Users/danvasudevan/projects/excel-generator/test-data/SUM_USECASE"
    resulting_excel = gpt.create_completion(prompt=prompt)
    matrix_list = ast.literal_eval(resulting_excel)
    util.generate_excel(input_matrix=matrix_list, folder_path=sum_data_path, file_name="RESULT_SUM")




