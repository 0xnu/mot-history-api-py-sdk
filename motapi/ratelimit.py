"""The module provides rate-limiting decorators for functions and methods.

It allows limiting the number of times a function can be called within a specified period.
"""

import time
from functools import wraps


class RateLimitExceeded(Exception):
    """Exception raised when the rate limit is exceeded."""

    def __init__(self, message: str, sleep_time: float):
        """
        Initialize the RateLimitExceeded exception.

        Args:
            message (str): The error message.
            sleep_time (float): The time to sleep before retrying.
        """
        super().__init__(message)
        self.sleep_time = sleep_time


def sleep_and_retry(func):
    """
    A decorator that catches RateLimitExceeded exceptions and retries the function after sleeping.

    Args:
        func (callable): The function to be decorated.

    Returns:
        callable: The wrapped function that implements the sleep and retry behaviour.
    """
    @wraps(func)
    def wrapper(*args, **kwargs):
        while True:
            try:
                return func(*args, **kwargs)
            except RateLimitExceeded as e:
                time.sleep(e.sleep_time)
    return wrapper


def limits(calls=15, period=900, raise_on_limit=True):
    """
    A decorator factory that returns a decorator to rate limit function calls.

    Args:
        calls (int): The maximum number of calls allowed within the specified period.
        period (int): The time period in seconds for which the calls are counted.
        raise_on_limit (bool): If True, raises RateLimitExceeded when limit is reached.
                               If False, blocks until the function can be called again.

    Returns:
        callable: A decorator that implements the rate limiting behaviour.
    """
    def decorator(func):
        # Initialize the state for tracking function calls
        func.__last_reset = time.monotonic()
        func.__num_calls = 0

        @wraps(func)
        def wrapper(*args, **kwargs):
            # Check if we need to reset the call count
            now = time.monotonic()
            time_since_reset = now - func.__last_reset
            if time_since_reset > period:
                func.__num_calls = 0
                func.__last_reset = now

            # Check if we've exceeded the rate limit
            if func.__num_calls >= calls:
                sleep_time = period - time_since_reset
                if raise_on_limit:
                    raise RateLimitExceeded("Rate limit exceeded", sleep_time)
                else:
                    time.sleep(sleep_time)
                    return wrapper(*args, **kwargs)

            # Call the function and increment the call count
            func.__num_calls += 1
            return func(*args, **kwargs)

        return wrapper

    return decorator
