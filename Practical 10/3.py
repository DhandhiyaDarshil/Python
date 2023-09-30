import time
import random
import functools

# Define a retry decorator
def retry(max_retries, delay=1, exceptions=(Exception,)):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            retries = 0
            while retries < max_retries:
                try:
                    result = func(*args, **kwargs)
                    return result  # If successful, return the result
                except exceptions as e:
                    print(f"Exception caught: {e}")
                    retries += 1
                    if retries < max_retries:
                        print(f"Retrying in {delay} seconds...")
                        time.sleep(delay)
                    else:
                        raise
        return wrapper
    return decorator

# Apply the retry decorator to the unreliable_function
@retry(max_retries=3, delay=2, exceptions=(ValueError,))
def unreliable_function():
    random_value = random.randint(1, 10)
    if random_value < 5:
        raise ValueError("Random error occurred.")
    return "Success!"

try:
    result = unreliable_function()
    print(result)
except Exception as e:
    print(f"Function failed after retrying: {e}")
