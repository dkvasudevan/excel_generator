from fastapi import FastAPI, File
import helpers.openai_helper as gpt
from helpers.excel_scraper import ExcelScraper
import helpers.utilities as util
import helpers.prompt_generator as pg
import ast
import os
import uuid
from dotenv import load_dotenv
app = FastAPI()

load_dotenv()

project_dir = os.getenv('PROJECT_DIR')

#add the values from column 1 and column 2. Put the sum in column 3
@app.get("/")
async def root():
    return {"message": "Welcome to excel generator"}

@app.post("/excel")
async def create_excel(user_prompt: str, file_data: bytes = File()):
    # file_path = "test-data/SUM_USECASE/TEST_SUM.xlsx"
    scraper = ExcelScraper(file_data=file_data)
    excel_data = scraper.get_matrix()
    prompt = pg.generate_prompt(excel_data=excel_data, user_prompt= user_prompt)
    sum_data_path = f"{project_dir}out-data"
    resulting_excel = gpt.create_completion(prompt=prompt)
    matrix_list = ast.literal_eval(resulting_excel)
    print(matrix_list)
    myuuid = uuid.uuid4()

    myuuid = str(myuuid)
    util.generate_excel(input_matrix=matrix_list, folder_path=sum_data_path, file_name=myuuid)



