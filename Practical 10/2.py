import time
import functools

# Define a rate limiting decorator
def rate_limit(limit, period):
    def decorator(func):
        calls = []

        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            now = time.time()
            calls[:] = [call for call in calls if now - call < period]

            if len(calls) < limit:
                calls.append(now)
                return func(*args, **kwargs)
            else:
                raise Exception("Rate limit exceeded. Try again later.")

        return wrapper

    return decorator

# Apply the rate limiting decorator to the API endpoint function
@rate_limit(limit=5, period=60)  # Allow 5 calls per minute
def api_endpoint(request_data):
    return "Response data"

# Call the API endpoint function and handle rate limit exceptions
for _ in range(7):
    try:
        print(api_endpoint("some_request_data"))
    except Exception as e:
        print(e)
