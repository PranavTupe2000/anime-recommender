from langchain_groq import ChatGroq


class AnimeRecommender:
    def __init__(self, prompt, retriever, api_key: str, model_name: str):
        # Groq chat model (langchain_groq)
        self.llm = ChatGroq(api_key=api_key, model=model_name, temperature=0)
        self.prompt = prompt
        self.retriever = retriever

    def get_recommendation(self, query: str) -> str:
        # Retrieve relevant documents using the Runnable interface
        # as_retriever() returns a Runnable that expects invoke(query)
        docs = self.retriever.invoke(query)

        # Build context from retrieved documents (top documents joined)
        context = "\n\n---\n\n".join([d.page_content for d in docs]) if docs else ""

        # Format the prompt using the PromptTemplate passed in
        try:
            formatted = self.prompt.format(context=context, question=query)
        except Exception:
            # Fallback: simple concatenation if prompt isn't a PromptTemplate
            formatted = f"Context:\n{context}\n\nQuestion: {query}"

        # Invoke the chat model and return the text content
        ai_msg = self.llm.invoke(formatted)

        # AIMessage object has `.content`; convert to str for safety
        return str(getattr(ai_msg, "content", ai_msg))