from InstagramAPI import InstagramAPI

## enter yor user name & password yor self
InstagramAPI = InstagramAPI("user name","password")   #my own info
InstagramAPI .login()   #log in to insta

if(InstagramAPI.login()):  #like a post by using post's id media
    result = InstagramAPI.like("enter id media")   #find the id media by left click on post and choose view source code and look for 'id media'
    print(result)
else:
   print("No")
if(InstagramAPI.login()):   #ulike a post by using post's id media
    result2 = InstagramAPI.unlike("enter id media")   # #find the id media by left click on post and choose view source code and look for 'id media'
    print(result2)
else:
   print("No")
if(InstagramAPI.login()):   #follow apage by using page's id
    result3 = InstagramAPI.follow("enter page's id")   # #find the page's id by left click on page and choose view source code and look for 'id'
    print(result3)
else:
   print("No")   
if(InstagramAPI.login()):   #ufollow apage by using page's id
    result4 = InstagramAPI.unfollow("enter page's id")   #find the page's id by left click on page and choose view source code and look for 'id'
    print(result4)
else:
   print("No")   
