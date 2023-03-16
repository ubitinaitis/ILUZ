<div align = "center">
<h1>*:･ﾟ✧  ILUZ  *:･ﾟ✧</h1>


---

<b>I.L.U.Z</b> is a simple MVP budgeting tool that can be used to track personal finances where users can specify short-term and long-term budgeting goals. It's tailored to allow users to meet their desired personalized financing needs!

There are three kinds of accounts one can have.<br></br></div>
+ A ‘<b>Budget master</b>’ can create separate profiles called ‘family plans’ for group expenses or designate a sub-account to represent a dependent with limited access compared to a main personal account.<br>
+ A ‘<b>Dependent</b>’ represents a user that isn’t fully financially independent and therefore extends from a family plan. They have an allowance to budget, but don’t have access to the full range of features that the owner of the account has. <br>
+ An ‘<b>Individual</b>’ works the same way– though they can be fully independent under a budget master’s family, they can view other profiles, but have limited access to editing anything but their own. Families of different sizes and financial situations have trouble budgeting their personal finances against the unit as a whole.
<br></br>Our app aims to create an efficient environment for family budgeting while setting up dependent’s for budgeting effectively in the future by viewing budgeting from a goal-oriented perspective.

![Wireframe](https://cdn.discordapp.com/attachments/1036674636827598989/1045138625920241754/image.png)

---

## <b>Table of Contents</b>
+ [Technologies](#technologies)
  - [How are they used?](#how-are-they-used)
+ [Entities](#entities)
  - [Budget Master](#budget-master)
  - [Independent](#independent)
  - [Dependent](#dependent)
+ [Challenges](#challenges)
  - [POST Requests](#post-requests)
+ [Continued Development](#continued-development)

<br>

---

## Technologies

- MySQL
- Docker
- Flask (Python)
- Ngrok
- Datagrip
- Appsmith

### How are they used

MySQL and Datagrip help build out the database used for this project. We've bootstrapped the database with sample/fake data-- fake budget masters, dependents, and independents that each contain fake attribute values pertaining to their entity type.<br>
Our REST API (Representational State Transfer Application Programming Interface), where the GET/POST request magic happens, is built in Flask (with Python!)<br>
Flask (a very lightweight, digestable Python web-building framework) communicates with ngrok, which allows a link from our localized project to a url on the internet, where its information can be used and parsed.<br>
Lastly, we built a UI in Appsmith (a very bare-bones drag-and-drop front-end maker) to consume our Rest API, and help finally connect user action to our back-end.

---

## Entities

<br>

### Budget Master

![Budget Master](https://cdn.discordapp.com/attachments/777710877636952096/1077650982617481277/image.png)

### Independent

![Independent](https://cdn.discordapp.com/attachments/777710877636952096/1077651065295601664/image.png)

### Dependent

![Dependent](https://cdn.discordapp.com/attachments/777710877636952096/1077651110451486811/image.png)

---

<br></br>

## Challenges

### POST Requests

POST requests were by far the trickiest to implement for us. POST involves the creation of a new custom entity based on the information put in for the attributes. We ran into many issues with this-- the particular syntax of our boilerplate, right down to the names and extensions of the files, was so sensitive. One attribute out of order could cause Flask to simply not recognize what the user was attempting to do, by any means. To solve this, we took care to research, learn, and accept the tricky Flask syntax, and all of its nuances. To rush into a project with prior experience in many other languages isn't enough-- it is not necessary to not learn as you go, but to learn beforehand. 

---

<br></br>

## Continued Development

- Appsmith connects an easy, stressless, quick front-end to our back-end. However, it is not very intuitive, and is rather constricting. In order to make a clean, customizeable front-end, we plan on connecting our project to a React-based web-hosted service instead.
