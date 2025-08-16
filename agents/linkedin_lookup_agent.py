from dotenv import load_dotenv
from langchain_core.tools import Tool

load_dotenv()

from langchain_core.prompts import PromptTemplate
from langchain_ollama import ChatOllama
from langchain.agents import (
    create_react_agent,
    AgentExecutor,  # This is a run time of an agent
)

from langchain import hub
from tools.search_tool import get_profile_url_tavily


def lookup(name: str, technology: str, company: str):
    llm = ChatOllama(model="llama3:8b", temperature=0.7)

    template = """given the full name {name_of_person}, technology {technology}, company {company}
                I want you to get it me a link to their LinkedIn profile page.
                Your answer should contain only a URL"""

    prompt = PromptTemplate(
        template=template,
        input_variables=["name_of_person", "technology", "company"],
    )

    tools_for_agent = [
        Tool(
            name="Crawl Google for LinkedIn profile page, give more prefrence to company",
            description="useful for when you need to get the linkedin profile page URL",
            func=get_profile_url_tavily,
        )
    ]

    reast_prompt = hub.pull("hwchase17/react")
    agent = create_react_agent(
        llm=llm,
        tools=tools_for_agent,
        prompt=reast_prompt,
    )
    executor = AgentExecutor(
        agent=agent,
        tools=tools_for_agent,
        verbose=True,
        handle_parsing_errors=True,
    )
    try:
        result = executor.invoke(
            input={"input": prompt.format_prompt(name_of_person=name, technology=technology,company=company,)},
        )
        profile_url = result["output"]
        return profile_url
    except Exception as e:
        print(e)


if __name__ == "__main__":
    linked_url = lookup(name="Shobhit Gupta LinkedIn Profile", technology="Flutter, iOS, Dart", company="WIO Bank")
    print("Search Google For LinkedIn profile page")
    print(linked_url)
