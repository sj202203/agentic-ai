from ollama import chat
import tools



def run_agent(user_txt: str):
    messages = [
        {
            "role":"system",
            "content": (
                "You are an assistant that must use tools for math and note saving. "
                "Do not answer math directly in text. "
                "If you need a tool, call the tool given by me."
            )
        },{
            "role":"user",
            "content": user_txt
        }
    ]

    while True:
        response = chat(
            model="qwen3",
            messages=messages,
            tools=[tools.calculator, tools.save_note],
        )

        messages.append(response.message)

        tool_calls = response.message.tool_calls or []

        if not tool_calls:
            return response.message.content

        # Normal tool-calling path
        if tool_calls:
            for call in tool_calls:

                if call.function.name=="calculator":
                    result=tools.calculator(**call.function.arguments)
                elif call.function.name == "save_note":
                    result = tools.save_note(**call.function.arguments)
                else:
                    result = "Unknown tool"
                
                messages.append(
                    {
                        "role":"tool",
                        "tool_name": call.function.name,
                        "content": str(result)
                    }
                )
 
if __name__ == "__main__":
    print("Type exit to quit")

    while True:
        user_txt = input("\nYou: ").strip()
        if user_txt.lower() in {"quit","exit"}:
            break
        
        print("Agent:",run_agent(user_txt))