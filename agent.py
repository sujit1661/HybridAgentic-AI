from dotenv import load_dotenv
from langchain.agents import create_agent
from langchain_core.runnables.history import RunnableWithMessageHistory
from langchain_core.messages import HumanMessage, SystemMessage
from langchain_community.chat_message_histories import FileChatMessageHistory
from langchain_groq import ChatGroq
from tools_registry import load_all_tools
import os

load_dotenv(verbose=True)



def get_session_history(session_id: str):
    os.makedirs("memory", exist_ok=True)
    return FileChatMessageHistory(f"memory/{session_id}.json")




llm = ChatGroq(
    model="openai/gpt-oss-20b",
    temperature=0,
    max_tokens=400,
)



agent = create_agent(
    model=llm,
    tools=load_all_tools()
)



system_prompt = """
You are a system automation AI.

IMPORTANT RULES:
1. If a user request can be solved using tools, call the tool immediately.
2. Do NOT create plans unless absolutely required.
3. Do NOT explain steps unless the user asks.
4. Prefer executing tools instead of describing actions.
5. Keep responses short.

When a user asks to create, run, delete, modify, install, or search something,
use the available tools directly.
"""



agent_with_memory = RunnableWithMessageHistory(
    agent,
    get_session_history,
    input_messages_key="messages",
)



print("\n🤖 AI System Agent Ready")
print("Type 'exit' to quit\n")

while True:
    user = input("You: ")
    if user.lower() == "exit":
        break

    response = agent_with_memory.invoke(
        {
            "messages": [
                SystemMessage(content=system_prompt),
                HumanMessage(content=user),
            ]
        },
        config={"configurable": {"session_id": "user1"}}
    )

    print("AI:", response["messages"][-1].content)