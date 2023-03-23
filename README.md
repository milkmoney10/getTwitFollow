# getTwitFollow

For ubuntu

git clone https://github.com/milkmoney10/getTwitFollow.git
<br>
cd getTwitFollow
<br>
source bin/activate
<br>
pip install -r requirements.txt
<br>
<br>
Add your keys/tokens and Twitter handles you want to look up. Max number of accounts ran at once is 15 iirc. Rate limit is 15 accounts every 15 minutes. You could modify the script, add a list of accounts to look up, and manually rerun the script with your next list. Just ask in TG for help with that if you need
<br>
Script will give error if you're rate limited or if you look up a private account - error probably is something like <Response [401]>
<br>
<br>
Run with: python3 twitFollowNoUi.py
<br>
<br>
Example output:



![Screenshot from 2023-03-23 16-58-34](https://user-images.githubusercontent.com/105143285/227374211-bdcd2699-c0ae-4994-9165-4872cd12eb9d.png)
