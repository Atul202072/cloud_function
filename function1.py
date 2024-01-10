import json
import random
import time

def function1(request):
    # Generate a random number between 0 and 1
    random_value = random.random()

    # 50% probability of success (status code 200)
    if random_value < 0.5:
        response_data = {"result": "Success!"}
        status_code = 200
    # 25% probability of throwing an error (status code 500)
    elif random_value < 0.75:
        response_data = {"error": "Internal Server Error"}
        status_code = 500
    # 25% probability of timeout (no response sent)
    else:
        # Simulate a timeout by delaying the response for a longer time
        time.sleep(5)  # You can adjust the sleep time as needed
        response_data = {"error": "Timeout Error"}
        status_code = 504

    # Convert the response data to a JSON string
    response_body = json.dumps(response_data)

    # Set up the response with appropriate headers and status code
    headers = {"Content-Type": "application/json"}
    return response_body, status_code, headers
