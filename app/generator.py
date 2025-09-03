from transformers import pipeline

class Generator:
    def __init__(self, model_name="google/flan-t5-base"):
        self.pipe = pipeline("text2text-generation", model=model_name)

    def generate(self, query, context, max_new_tokens=100):
        # If no context found, return fallback immediately
        if not context or context.strip() == "":
            return "Sorry, I don't know the answer to that."

        # Otherwise, ask model with explicit instruction
        prompt = (
            f"Answer the question using the context below. "
            f"If the context does not contain the answer, say you don't know.\n\n"
            f"Context: {context}\n\nQuestion: {query}"
        )

        response = self.pipe(prompt, max_new_tokens=max_new_tokens)
        return response[0]["generated_text"].strip()




# from transformers import pipeline

# class Generator:
#     def __init__(self, model_name="google/flan-t5-base"):    #  distilgpt2
#         self.pipe = pipeline("text-generation", model=model_name)

#     def generate(self, query, context, max_new_tokens=100):
#         prompt = f"Context: {context}\nQuestion: {query}\nAnswer:"
#         response = self.pipe(prompt, max_new_tokens=max_new_tokens)
#         return response[0]["generated_text"]
