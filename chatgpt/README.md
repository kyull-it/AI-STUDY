# ChatGPT API
### Function Calling 테스트
* [Document](https://platform.openai.com/docs/guides/function-calling)

### Environment 구축
1. openai 패키지 설치
```shell
pip install openai
```
2. openai api key 시스템 환경변수 설정
```shell
export OPENAI_API_KEY=<user_api_key>
```
3. python 실행
```shell
python3 asst_func_call.py
```

### Result
```
ChatCompletion(
    id='chatcmpl-9BdFoo0CAq8RCMSoMewThFVwEwsS8', 
    choices=[Choice(
        finish_reason='stop', 
        index=0, 
        logprobs=None, 
        message=ChatCompletionMessage(content='The current weather in:
            - San Francisco is 72°C and sunny
            - Tokyo is 10°C and cloudy
            - Paris is 22°C and partly cloudy', 
        role='assistant', 
        function_call=None, 
        tool_calls=None))], 
    created=1712559528, 
    model='gpt-3.5-turbo-0125', 
    object='chat.completion', 
    system_fingerprint='fp_b28b39ffa8', 
    usage=CompletionUsage(
            completion_tokens=33, 
            prompt_tokens=169, 
            total_tokens=202))
```

### Price
![image](https://github.com/kyull-it/AI-STUDY/assets/67450333/fda720ec-41b5-4cc3-99be-4e871aea7eb9)
