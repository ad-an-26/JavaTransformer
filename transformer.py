from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langchain.schema import HumanMessage, SystemMessage

load_dotenv()

def transform_java_code(user_code):
  system_prompt = (
    "You are a Java code modernization expert. Convert Java 8 code into Java 21 using features like:\n"
        "- `record` (instead of simple classes with getters)\n"
        "- enhanced switch\n"
        "- type inference (var)\n"
        "- sealed classes\n"
        "- pattern matching\n"
        "- virtual threads (via `Executors.newVirtualThreadPerTaskExecutor()` — this is the correct Java 21 API)\n"
        "`try-with-resources` for managing executors or resources safely"
        "Rules:"
        "- Keep the **logic and output the same** as the original."
        "- **Ensure the transformed Java 21 code is 100% syntactically correct and complete**:"
          "- Include all necessary `import` statements."
          "- Ensure all braces (`{}`) are closed properly."
          "- Place `record` and `sealed` classes **outside** the `main()` method or any other methods."
          "- Avoid placing class definitions inside methods."
          "- Use best practices in formatting."
        "Ensure the logic stays the same and the output should be same as well. Ensure the Java 21 code is complete, syntactically correct, and does not include any extra explanation. Place records and classes at the appropriate scope (e.g. outside main methods). Only return a complete compilable code block."
        "Do NOT include any explanations, comments, or markdown (e.g. no ```java or ```)."
        "Only return the final Java 21 code — as it would appear in a `.java` file."
        "The output must be ready to compile and run without modification."
  )

  model = ChatOpenAI(model="gpt-4", temperature=0.3)

  messages = [
    SystemMessage(content=system_prompt),
    HumanMessage(content=user_code)
  ]

  response = model.invoke(messages)
  return response.content