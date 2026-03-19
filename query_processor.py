def process_query(query: str, llm):
    """
    Convert user input into structured intent
    """

    prompt = f"""
Extract structured info from the query.

Return JSON:
{{
  "intent": "...",
  "task": "...",
  "entities": {{}}
}}

Query: {query}

Only JSON.
"""

    res = llm.invoke(prompt)

    try:
        import json
        return json.loads(res.content)
    except:
        return {
            "intent": "general",
            "task": query,
            "entities": {}
        }