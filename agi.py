import requests
import re
import random
import threading

def extract_python_code(text):
    matches = re.findall(r'```python\n(.*?)\n```', text, re.DOTALL)
    return matches[0] if matches else None

def timed_input(prompt, timeout):
    print(prompt, end=' ', flush=True)
    input_result = [None]

    def input_thread(input_result):
        try:
            input_result[0] = input()
        except EOFError:
            pass

    thread = threading.Thread(target=input_thread, args=(input_result,))
    thread.start()
    thread.join(timeout)
    
    if thread.is_alive():
        print("\nTimeout! Moving to the next attempt.")
        thread.join()
        return None
    return input_result[0]

def generate_code(api_endpoint, initial_prompt, max_attempts, max_new_tokens, timeout):
    prompt = initial_prompt
    for attempt in range(max_attempts):
        print(f"Attempt {attempt + 1} of {max_attempts}")
        data_payload = {
            "prompt": prompt,
            "max_tokens": max_new_tokens,
            "temperature": random.uniform(0.0, 1.0),
            "top_p": random.uniform(0.0, 1.0),
        }

        response = requests.post(api_endpoint, json=data_payload)

        if response.status_code == 200:
            generated_text = response.json()['choices'][0]['text']
            print(f"Generated Text:\n{generated_text}")

            code = extract_python_code(generated_text)
            if code:
                print("Extracted Code:\n", code)
                # Add your code execution logic here, if necessary and safe
                user_input = timed_input("Do you accept this solution? (y/n): ", timeout)
                if user_input and user_input.lower() == 'y':
                    return code
                else:
                    prompt += "\n# Previous attempt did not produce an acceptable solution. Please try again."
            else:
                print("No executable code found.")
                prompt += "\n# No executable code found in the previous attempt. Please try again."
        else:
            print(f"Failed to generate text. Status code: {response.status_code}")

    return None

# Configuration for the script
api_endpoint = "http://127.0.0.1:5000/v1/completions"  # Replace with your actual API endpoint
initial_prompt = "Create a simple Python script for a basic task."
max_attempts = random.randint(0, 200)
max_new_tokens = random.randint(0, 10000)
input_timeout = 10  # Set the timeout in seconds

# Run the script
generated_code = generate_code(api_endpoint, initial_prompt, max_attempts, max_new_tokens, input_timeout)

if generated_code:
    print("Code execution completed successfully.")
    print("\nGenerated Code:\n", generated_code)
else:
    print("Script ended without a successful execution.")
