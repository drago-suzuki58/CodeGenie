from google import genai
import os

class CodeGenie:
    def __init__(self, model=None, api_key="API_KEY", cache_dir="./cache"):
        self.client = genai.Client(api_key=api_key)
        self.model = model
        self.cache_dir = cache_dir

    def __getattr__(self, name):
        def wrapper(*args, **kwargs):
            if self._is_cached(name):
                with open(f"{self.cache_dir}/{name}.py", "r", encoding="utf-8") as f:
                    code = f.read()
                print("Cached code:\n", code)
            else:
                if not self.model:
                    raise ValueError("Please provide a model name to generate code.")
                prompt = self._create_prompt(name, args, kwargs)
                response = self.client.models.generate_content(
                    model=self.model,
                    contents=prompt
                )
                self._save_cache(response.text, name)
                print("Generated code:\n", response.text)
                code = response.text

            if code is None:
                raise ValueError("Generated code or Cached code is None and cannot be executed.")

            input("Press Any Key to execute the code...")
            exec_globals = {}
            exec(code, exec_globals)
            exec_globals[name](*args, **kwargs)
        return wrapper

    def _create_prompt(self, name, args, kwargs):
        return f"""# You are an embedded AI. Please generate executable Python code according to the following conditions:
# - Generate executable Python code based on the function name and list of arguments
# - Appropriately use the arguments within the generated code
# - Infer the user's intent and generate code that matches the function name
# - Ensure the generated code is executable
# - Comment out irrelevant sections
# - Do not output Markdown or triple backticks (```python)
# - Import statements are written inside functions. Do not import unnecessary libraries.

# Function name and list of arguments
# Function name: {name}
# *args: {args}
# *kwargs: {kwargs}

# Output the executable Python code below"""

    def _save_cache(self, text, name):
        os.makedirs(self.cache_dir, exist_ok=True)
        with open(f"{self.cache_dir}/{name}.py", "w", encoding="utf-8") as f:
            f.write(text)

    def _is_cached(self, name):
        return os.path.exists(f"{self.cache_dir}/{name}.py")
