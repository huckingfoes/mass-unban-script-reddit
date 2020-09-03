import praw
from datetime import datetime
from dateutil.parser import parse

# EDIT THESE
START_BAN_PERIOD = "YYYY-MM-DD" # date to start unbanning
END_BAN_PERIOD = "YYYY-MM-DD" # date to stop unbanning
SUBREDDIT_NAME = "SUBREDDIT" # subreddit you want to mass-unban;

botName = "mass-unban-bot"
botDescription = "A mass unbanning script by u/huckingfoes"

reddit = praw.Reddit(botName, user_agent=botDescription)

startDate = parse(START_BAN_PERIOD)
endDate = parse(END_BAN_PERIOD)

subreddit = reddit.subreddit(SUBREDDIT_NAME)

for bannedUser in subreddit.banned(limit=None):
	unixTimestamp = int(bannedUser.date)
	currentBanDate = datetime.utcfromtimestamp(unixTimestamp)
	
	if (currentBanDate > startDate) and (currentBanDate < endDate): 
#		subreddit.banned.remove(bannedUser)
		print('Unbanned: ' + '{}: {}'.format(bannedUser, bannedUser.note))
	