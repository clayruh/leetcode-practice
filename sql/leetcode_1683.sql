# find IDs with invalid tweets, CHAR_LENGTH(content) > 15
SELECT tweet_id FROM tweets
WHERE CHAR_LENGTH(content) > 15