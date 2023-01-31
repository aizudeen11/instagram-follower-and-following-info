from bs4 import BeautifulSoup
import pandas as pd

with open("followers.html") as fp:
    soup = BeautifulSoup(fp, 'html.parser')

follower_list = []
following_list = []
for followers in soup.find_all('a'):
    x = followers.get_text()
    follower_list.append(x)

with open("following.html") as fp:
    soup = BeautifulSoup(fp, 'html.parser')

for following in soup.find_all('a'):
    x = following.get_text()
    following_list.append(x)

follower_or_following = list(set(follower_list).symmetric_difference(set(following_list)))
follower_and_following = list(set(follower_list).intersection(set(following_list)))
following_only = list(set(following_list).symmetric_difference(set(follower_and_following)))
follower_only = list(set(follower_list).symmetric_difference(set(follower_and_following)))

lists = [follower_list, following_list, follower_or_following, follower_and_following, following_only, follower_only]
df = pd.concat([pd.Series(x) for x in lists], axis=1)
df.columns = ["follower_list", "following_list", "follower_or_following", "follower_and_following", "following_only", "follower_only"]
print(df)
df.to_csv("Aizudeen follower and following info.csv")