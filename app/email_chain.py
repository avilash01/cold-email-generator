import os
from dotenv import load_dotenv

from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import JsonOutputParser
from langchain_core.exceptions import OutputParserException

load_dotenv()


class Chain:
    def __init__(self):
        self.llm = ChatGroq(
            groq_api_key=os.getenv("GROQ_API_KEY"),
            model="llama-3.1-8b-instant",
            temperature=0
        )

    def extract_jobs(self, cleaned_text):
        prompt_extract = PromptTemplate.from_template(
            """
            SCRAPED TEXT FROM WEBSITE:
            {page_data}

            ### INSTRUCTION:
            The text is from the career's page of a website.
            Extract the job postings and return them in JSON format
            with the following keys:
            - role
            - experience
            - skills
            - description

            Only return valid JSON.
            """
        )

        chain_extract = prompt_extract | self.llm
        response = chain_extract.invoke({"page_data": cleaned_text})

        try:
            json_parser = JsonOutputParser()
            parsed_output = json_parser.parse(response.content)
        except OutputParserException as e:
            raise OutputParserException(f"Failed to parse JSON output: {e}")

        return parsed_output if isinstance(parsed_output, list) else [parsed_output]

    def write_mail(self, job, links):
        prompt_email = PromptTemplate.from_template(
            """
            ### JOB DESCRIPTION:
            {job_description}

            ### INSTRUCTION:
            You are Avilash, a Business Development Executive at Atlassian.
            Atlassian is an AI & software consulting company focused on
            automating business processes.

            Write a cold email to the client addressing their needs.
            Include the most relevant portfolio links from:
            {link_list}

            Do NOT include a preamble.

            ### EMAIL:
            """
        )

        chain_email = prompt_email | self.llm
        response = chain_email.invoke(
            {
                "job_description": str(job),
                "link_list": links
            }
        )

        return response.content
