# Python Facebook messenger webhook with FastAPI on Glitch

![Alt Text](https://dev-to-uploads.s3.amazonaws.com/i/zbu4maxpcvm05rs7zfep.jpg)

This webhook can be accessed on [Glitch](https://glitch.com/~wit-ai-pywebhook) and re-used ("remixed") to start a new project.

## Demo

![The facebook messenger output](https://cdn.glitch.com/529fa55b-87a8-4024-9f8a-84d263c206b3%2Fmessenger.png?v=1597507445635)

![Logging output](https://cdn.glitch.com/529fa55b-87a8-4024-9f8a-84d263c206b3%2Flogs.png?v=1597507449109)

Also check out Scott's [introduction video](https://bit.ly/310kdfG) on setting up facebook messenger based on his node.js app.

## Requirements

- Python 3.6+
- FastAPI
- Uvicorn

## API Gateway features

- **GET verification** of a received _challenge_
- **POST message reponse** after validating the signature _X-Hub-Signature_ of the received message

# Verify the Webhook

The webhook will return the received variable "challenge" as required by [Facebook's instructions](https://developers.facebook.com/docs/messenger-platform/webhook) to set up a webhook. You will have to add the webhook in your Messenger settings for each App, which you can access on [Facebook Developers](https://developers.facebook.com/).

![Added webhook](https://cdn.glitch.com/529fa55b-87a8-4024-9f8a-84d263c206b3%2Fappsettings.png?v=1597508804453)

## Respond to a message received on a Facebook Page

After glueing your app together with a facebook page and this webhook you will be able to focus your _pythonista skills_ on the responses of your virtual alter ego.

## Wit.ai Hackathon 3 submission

This webhook will be used as a contribution for the 2020 Facebook Hackathon Series, Hackathon 3 with the submission deadline as of _7 September 2020_. This contribution aims to tickle some strategic points out of the judges and particularly encourages all the smart data scientists out there to focus on their algorithmic models to make a compelling case for a friendly, clever and helpful chatbot.

## Pull Requests, Issues, Comments

All feedback is welcome. Hope to hear if you find this contribution useful. The repo is [here](https://github.com/factorlive/fbmessenger-pywebhook).

ToDo list:

- Refactored [dependency](https://fastapi.tiangolo.com/tutorial/dependencies/) to check signature
- Util function to package outgoing message
- Full testing coverage with test client
- Add response time to logs
- Explain code line by line in Readme