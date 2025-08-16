from langchain_community.tools.tavily_search import TavilySearchResults

def get_profile_url_tavily(name: str):
    """Searches for LinkedIn or Twitter Profiles pages"""
    search = TavilySearchResults()
    results = search.run(f"{name}")
    return results
