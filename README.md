# Final-Year-Project-ChatBot
## How to run 
------------------


To run this bot you have to follow 4 steps.
### 1- Rasa installation

You must install the latest version of Rasa Core. It is highly recommended that you create a virtual environment and then proceed with the installations
#### i- Creating virtual enviroment
conda create –Rayan python=3.6

#### ii- Activating the new environment to use it
WINDOWS: activate bot
LINUX, macOS: source activate bot

#### iii - Installing the latest Rasa stack and NLU
python -m pip install rasa_nlu[spacy] (https://rasa.com/docs/nlu/installation/)

#### iv - Rasa Core
python -m pip install -U rasa_core (https://rasa.com/docs/core/installation/)

#### v - Language model
python -m spacy download en_core_web_md python -m spacy link en_core_web_md en --force;

##### Note: The Project file contains all the files needed and requirement.text with all the dependencies listed in them.


### 2) Setting Slack application
Let’s us create a slack integration by creating a slack app. Let’s go through the process of creating a Slack app.
* Create a Slack account and go to https://api.slack.com/. Now choose either an existing development Slack workplace(in case you have one) or create a new one. Name it DemoWorkplace or anything you like.
* Now create a Slack app in DemoWorkplace and give it a name ‘Rayan’.
* Start adding features and functionalities to the app. We’ll first create a ‘bot user’ under the ‘Bots’ Tab and integrate it into the app. This will make the app conversational. Save all the changes made.
45
* Start adding features and functionalities to the app. We’ll first create a botuser under the Bots Tab and integrate it into the app. This will make the app conversational. Since this bot will be created as a user, we can choose to keep it constantly online. Save all the changes made.
* Lastly, we need to install this app into our workplace which we defined earlier. Authorize it and we have our app ready and integrated into the workplace.please follow the process in the example here: https://cdn-images-1.medium.com/max/600/1*nNCR8wmXVkQOAZJ7BTEspg.gif


### 3) Setting ngrok Ngrok is a multi-platform tunnelling, reverse proxy software that establishes secure tunnels from a public endpoint such as the internet to a locally running network service. 
* 1- Download ngrok from here https://dashboard.ngrok.com/user/login
* 2- Unzip to install.
* 3- Run ngrok from unzipped file

Once run pass it ./ngrok http 5004

If everything works you should see example of a window below.

<p align="center"><img src = "images/ngrok.PNG" ></p>

You will later need to copy the generated ngrok URL to the slack in the following steps.


### 4) Deploying the bot on Slack
In the project file you will find run_app.py which will integrate the chatbot with the slack app 

But first you need to run the custom actions created for this bot, it can be done through running

`$ python -m rasa_core_sdk.endpoint --actions actions 

Now you need to run the run_app.py but first you Make sure to provide the slack token in the run_app.py it can be found under variable name Input channel.

<p align="center"><img src = "images/snipet.PNG" ></p>

* The slack token can be obtained as followed.

<p align="center"><img src = "images/slack.PNG" ></p>

* Now go to the event subscriptions page on Slack

<p align="center"><img src = "images/event.PNG" ></p>
* Provide the url gained from the ngrok and paste at Request URL to verify. 
* Subscribe to workplace events by adding bot user event. Save all changes

<p align="center"><img src = "images/event2.PNG" ></p>

## Ensure!

* That the custom actions server is running 
* Ngrok is running on port 5004 
* Run.py is running 

Now navigate to the slack interface and chat with the bot ‘Rayan’!


