# Python_tests
## README

---

### Twitter API Wrapper

This Python library provides a simple wrapper for interacting with the Twitter API. It allows users to post tweets, retrieve user avatars, and extract hashtags from messages.

**Note:** This project was developed as part of an online Python programming course.

#### Usage

1. **Installation:**
   - Clone this repository or download the source code.
   - Install the required dependencies using `pip install -r requirements.txt`.

2. **Initialization:**
   - Create an instance of the `Twitter` class by providing optional `backend` and `username` parameters.
   - Example:
     ```python
     from twitter import Twitter

     twitter = Twitter(backend=None, username="example_user")
     ```

3. **Posting Tweets:**
   - Use the `tweet` method to post a tweet with a message.
   - Example:
     ```python
     twitter.tweet("Hello, Twitter!")
     ```

4. **Retrieving User Avatar:**
   - Obtain the user avatar URL using the `get_user_avatar` method.
   - Example:
     ```python
     avatar_url = twitter.get_user_avatar()
     ```

5. **Finding Hashtags:**
   - Extract hashtags from a tweet message using the `find_hashtags` method.
   - Example:
     ```python
     hashtags = twitter.find_hashtags("Excited for #Python programming!")
     ```

6. **Version Information:**
   - Access the version information of the Twitter library using the `version` attribute.
   - Example:
     ```python
     version = twitter.version
     ```

#### Example Usage

```python
from twitter import Twitter

# Create a Twitter instance
twitter = Twitter(backend=None, username="example_user")

# Post a tweet
twitter.tweet("Hello, Twitter!")

# Retrieve user avatar URL
avatar_url = twitter.get_user_avatar()

# Find hashtags in a message
hashtags = twitter.find_hashtags("Excited for #Python programming!")

# Access library version
version = twitter.version
```

#### Testing

The library includes a set of unit tests to ensure its proper functionality. The tests cover various scenarios, including posting tweets, handling message length, retrieving avatars, and extracting hashtags.

To run the tests, execute the following command:

```bash
pytest test_twitter.py
```

---

*This project was developed based on the concepts learned during an online Python programming course.*
 
