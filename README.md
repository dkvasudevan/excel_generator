# Introduction
This repo is the backend for an AI Excel Guru application. All you have to do is simply input an excel sheet, tell the AI what analysis you want done on the excel sheet and it will generate the output for you.
Backend Tech Stack: Python, Fast API, OpenAI API


NOTE: This is still a work in progress and have many things on the roadmap including:
- Integrate langchain
- Allow data analysis across excel sheets
- Continue to iterate on more complex use cases.

# Setup Prerequisites
## Download Docker
Instructions here: https://docs.docker.com/get-started/get-docker/

# Installation instructions
1. Clone this repository
2. Open Terminal and CD to the project
3. Run ```chmod +x ./run_excel_ai.sh``` and ```./run_excel_ai.sh```. Your application is now running and this can be verified in the docker desktop application
4. Go to http://localhost:8000/docs on your browser to see the FastAPI docs and interact with the AI (frontend is on the roadmap)
