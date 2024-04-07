# from langchain.memory import ConversationBufferWindowMemory

def prompt_test():

    response_schemas = [
        ResponseSchema(name="answer", description="answer to the user's question"),
        ResponseSchema(name="source", description="source used to answer the user's question, should be a website.")
    ]
    output_parser = StructuredOutputParser.from_response_schemas(response_schemas)
    format_instructions = output_parser.get_format_instructions()
    prompt = ChatPromptTemplate(
        messages=[
            HumanMessagePromptTemplate.from_template(
                "answer the users question as best as possible.\n{format_instructions}\n{question}")
        ],
        input_variables=["question"],
        partial_variables={"format_instructions": format_instructions}
    )


if __name__ == '__main__':
    prompt_test()
