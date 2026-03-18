from dotenv import load_dotenv
from langchain.agents import create_agent
from langchain_core.runnables.history import RunnableWithMessageHistory
from langchain_core.messages import HumanMessage
from langchain_community.chat_message_histories import FileChatMessageHistory
from langchain_groq import ChatGroq
from tools_registry import load_all_tools
import os
from AgentLogger import log_info,log_error

load_dotenv()

def get_session_history(session_id: str):
    os.makedirs("memory", exist_ok=True)
    return FileChatMessageHistory(f"memory/{session_id}.json")


system_prompt = """
You are a system automation AI.

IMPORTANT RULES:
1. If a user request can be solved using tools, call the tool immediately.
2. Do NOT create plans unless absolutely required.
3. Prefer executing tools instead of explaining actions.
4. Keep responses short.
"""

llm = ChatGroq(
    model="openai/gpt-oss-20b",
    temperature=0,
    max_tokens=400,
)

agent = create_agent(
    model=llm,
    tools=load_all_tools(),
    system_prompt=system_prompt
)

agent_with_memory = RunnableWithMessageHistory(
    agent,
    get_session_history,
    input_messages_key="messages",
)

print("\n🤖 AI System Agent Ready")
print("Type 'exit' to quit\n")



def run_agent(query: str,session_id: str = "default"):
    try:
        log_info(f"User Query: {query}")

        response = agent_with_memory.invoke(
            {"messages": [HumanMessage(content=query)]},
            config={"configurable": {"session_id": session_id},
                "recursion_limit": 50 }
        )

        return response["messages"][-1].content
    except Exception as e:
        log_error(f"Error: {str(e)}")
        return "Something went wrong"