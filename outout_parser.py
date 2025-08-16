from typing import List
from langchain.output_parsers import PydanticOutputParser
from pydantic import BaseModel, Field


class Summary(BaseModel):
    summary: str = Field(description="summary of the person")
    facts: List[str] = Field(description="interesting facts about the person")

    def to_dict(self):
        return {"summary": self.summary, "facts": self.facts}
    
summary_parser = PydanticOutputParser(pydantic_object=Summary)
print(summary_parser.get_format_instructions())
