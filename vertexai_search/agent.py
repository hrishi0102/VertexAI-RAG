import os
from dotenv import load_dotenv
from google.adk.agents import Agent
from google.adk.tools import VertexAiSearchTool

load_dotenv()

# Configuration
DATASTORE_ID =  os.environ.get("DATASTORE_ID")

root_agent = Agent(
    name="vertexai_search",
    model="gemini-2.5-flash",
    instruction=f"""You are a helpful assistant that answers questions based on information found in the document store: {DATASTORE_ID}.
    Use the search tool to find relevant information before answering.
    If the answer isn't in the documents, say that you couldn't find the information.""",
    description="Enterprise document search assistant with Vertex AI Search capabilities",
    tools=[VertexAiSearchTool(data_store_id=DATASTORE_ID)]
)

## Trying to enforce grounding search, but still fails (answers all questions regardless)

# import os
# from dotenv import load_dotenv
# from google.adk.agents import Agent
# from google.adk.tools import VertexAiSearchTool

# load_dotenv()

# DATASTORE_ID = "projects/trusty-shine-464213-n0/locations/global/collections/default_collection/dataStores/paymanwebsite_1763042834752"

# # Initialize the Vertex AI Search tool
# search_tool = VertexAiSearchTool(data_store_id=DATASTORE_ID)

# # Define a wrapper that enforces grounding
# def grounded_search(query):
#     result = search_tool.run(query)
    
#     # Check if grounding returned results
#     grounding_chunks = getattr(result, "grounding_metadata", {}).get("grounding_chunks")
    
#     if not grounding_chunks or len(grounding_chunks) == 0:
#         return "I don’t have information about that in my datastore."
    
#     return result


# # Create the agent
# root_agent = Agent(
#     name="vertexai_grounded_agent",
#     model="gemini-2.5-flash",
#     description="Enterprise search assistant restricted to datastore content.",
#     instruction=(
#         "Use the VertexAiSearchTool ONLY when the user asks about information "
#         "that could be found in the datastore. "
#         "If the datastore doesn't contain relevant information, reply strictly with: "
#         "'I don’t have information about that in my datastore.' "
#         "Do not generate or guess answers. Always cite sources when available."
#     ),
#     tools=[search_tool],
# )

# # Optional — override the default tool call behavior to use our guard
# root_agent.tools[0].run = grounded_search

