GEN_QUESTION_JSON_FORMAT = {
        "Question": "here you will write the question",
        "Answer": """here you will write one or more answers in a python list format.
                   if there are more than one answer - the first answer in the list 
                   will be the correct answer, and the rest - the wrong ones. """,
        "Explanations": """here you will include explanations for the answer/s in a python list.
                        Make sure that the index of the explanation inside this list
                        corresponds to the index of the relevant answer in the 
                        answers list. For example: Explanation: ['explanation 1'] will
                        be the explanation to answer inside index 0 of the answers list."""
}