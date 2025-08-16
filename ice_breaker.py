from typing import Tuple
from dotenv import load_dotenv
from langchain.prompts.prompt import PromptTemplate
from langchain_ollama import ChatOllama

from agents.linkedin_lookup_agent import lookup
from third_parties.linkedin import scrape_linkedin_profile
from outout_parser import Summary, summary_parser

def ice_breaker(name: str, technology: str, company: str) -> Tuple[Summary, str]:
    linkedin_url = lookup(name, technology, company)
    linkedin_data = scrape_linkedin_profile(linkedin_url)
    
    summary_template = """
    given the Linkedin information {information} about a person I want you to create:
    1. A short summary
    2. two interesting facts about them

    \n{format_instructions}
    """

    summary_prompt_template = PromptTemplate(
        input_variables=["information"], template=summary_template,
        partial_variables={"format_instructions": summary_parser.get_format_instructions()}
    )

    llm = ChatOllama(model="llama3:8b", temperature=0.5)

    # LCEL
    chain = summary_prompt_template | llm | summary_parser
    res: Summary = chain.invoke(input={"information": linkedin_data})

    print("*** Response ***")
    return res, linkedin_data.get("photoUrl")

# if __name__ == "__main__":
#     load_dotenv()
#     result = ice_breaker(name="Shobhit Gupta", technology="Flutter, iOS, Dart", company="WIO Bank")
#     print(result)

