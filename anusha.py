import requests
import json
from requests.api import options,request
r=requests.get("https://saral.navgurukul.org/api/courses")
d=r.json()
#print(d)
def available(): 
    with open("myfile.json","w") as f:
        json.dump(d,f,indent=4)
count=0
listOfCourseIds=[]
for i in d["availableCourses"]:
    count=count+1
    print(count,i["name"],i["id"])
    listOfCourseIds.append(i["id"])
for courses in d["availableCourses"]:
    course=int(input("enter your courses"))
    select=d["availableCourses"][course-1]["id"]
    var=requests.get("http://saral.navgurukul.org/api/courses/"+str(select)+"/exercises")
    data=var.json()
    print(data)
    slug=[]
    
listOfCourseIds=[]
available()
while course
 