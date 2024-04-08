from openai import OpenAI
import json

client = OpenAI()

# 같은 날씨값을 출력해주는 것으로 하드코딩되어있는 예시더미코드입니다.
# 실제 제품에서는 백엔드 API나 외부 API를 적용할 수 있습니다.
def get_current_weather(location, unit="fahrenheit"):
    """Get the current weather in a given location"""
    if "tokyo" in location.lower():
        return json.dumps({"location": "Tokyo", "temperature": "10", "unit": unit})
    elif "san francisco" in location.lower():
        return json.dumps({"location": "San Francisco", "temperature": "72", "unit": unit})
    elif "paris" in location.lower():
        return json.dumps({"location": "Paris", "temperature": "22", "unit": unit})
    else:
        return json.dumps({"location": location, "temperature": "unknown"})

# https://platform.openai.com/docs/api-reference/chat 
# 위의 링크를 같이 참조하여 Chat object의 구조를 파악하시기 바랍니다.
def run_conversation():

    # Step 1: 모델에 메시지와 functions를 입력한다.
    model = "gpt-3.5-turbo-0125"
    messages = [{"role": "user", "content": "What's the weather like in San Francisco, Tokyo, and Paris?"}]
    tools = [
        {
            "type": "function",         # type은 function 밖에 지원하지 않는다. (240408)
            "function": {               # function calling 정의
                # 위에서 정의했던 함수 입력
                "name": "get_current_weather",        
                "description": "Get the current weather in a given location",
                # function에 들어갈 parameter 정의
                "parameters": {         
                    "type": "object",
                    "properties": {
                        "location": {
                            "type": "string",
                            "description": "The city and state, e.g. San Francisco, CA",
                        },
                        "unit": {"type": "string", "enum": ["celsius", "fahrenheit"]},
                    },
                    # 필수 파라미터
                    "required": ["location"],   
                },
            },
        }
    ]

    # 파라미터들을 입력하여, chatgpt API를 호출한다.
    response = client.chat.completions.create(
        model=model,
        messages=messages,
        tools=tools,
        tool_choice="auto",  # auto is default, but we'll be explicit
    )
    response_message = response.choices[0].message
    tool_calls = response_message.tool_calls

    # Step 2: 호출할 functions가 있는지 확인한다. 
    if tool_calls:

        # Step 3 : 모델이 functions를 호출한다.

        # Note: the JSON respons는 항상 유효하지 않을 수 있습니다. 에러를 주의하세요.
        # 해당 예시에서는 하나의 function을 사용하였으나, 여러 개도 가능합니다.
        available_functions = {
            "get_current_weather": get_current_weather,
        } 
        
        # assistant의 답변을 메시지 리스트에 담는다.
        messages.append(response_message)  

        # Step 4: 모델로 각 function 호출을 위해 정보를 보내고, 그에 따른 function response를 보낸다.
        for tool_call in tool_calls:
            function_name = tool_call.function.name
            function_to_call = available_functions[function_name]
            function_args = json.loads(tool_call.function.arguments)
            function_response = function_to_call(
                location=function_args.get("location"),
                unit=function_args.get("unit"),
            )
            # function response를 메시지 리스트에 담는다.
            messages.append(
                {
                    "tool_call_id": tool_call.id,
                    "role": "tool",
                    "name": function_name,
                    "content": function_response,
                }
            )  
            
        # function response를 볼 수 있는 모델의 새 응답을 받아옵니다.  
        second_response = client.chat.completions.create(
            model="gpt-3.5-turbo-0125",
            messages=messages
            )
        return second_response
    
print(run_conversation())