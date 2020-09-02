# mass-unban-script

Allows moderators to mass unban users between a date range.

1. pip3 install -r requirements.txt
2. Replace values in praw-example.ini with your API information
3. Rename praw-example.ini to praw.ini
4. Edit the constants on the top of mass-unbanner.py to specify dates and subreddit
5. Run the script: python3 mass-unbanner.py
    5.1 Note: This will NOT affect any users yet.
6. You'll see all the users print out that are within the range you specified, to be unbanned
7. If this is correct, un-comment (remove #) on line 25 to enable ban removal behavior
8. Congrats. You've just unbanned thousands of users.
