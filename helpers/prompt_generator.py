


def generate_prompt(excel_data: list, user_prompt: str):
    prompt_template = f"""Here is a 2d matrix that represents an excel sheet:
    {excel_data}
    Return a 2d matrix that does the following: {user_prompt}
    return just the 2d matrix with the result and nothing else. The first item in the array is the headers for the excel sheet. 
    Make sure to include those headers in the resulting 2d matrix as well.
    Ensure you add no additional text to your response outside of the 2d array.
    I am using the 2d matrix to automate a task and any additionaly content outside of the matrix will mess up the automation.
    """

    return prompt_template

