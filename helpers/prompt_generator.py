


def generate_prompt(excel_data: list, user_prompt: str):
    prompt_template = f"""Here is a 2d matrix that represents an excel sheet:
    {excel_data}
    Return a 2d matrix that does the following: {user_prompt}
    return just the 2d matrix with the result and nothing else
    """

    return prompt_template

