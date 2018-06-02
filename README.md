# Member Compendium
[![Build Status](https://travis-ci.org/trianglefraternitymtu/member-compendium.svg?branch=master)](https://travis-ci.org/trianglefraternitymtu/member-compendium) [![Coverage Status](https://coveralls.io/repos/github/trianglefraternitymtu/member-compendium/badge.svg?branch=master)](https://coveralls.io/github/trianglefraternitymtu/member-compendium?branch=master)

A central tool for all of the chapters needs.

Supported Tools:
- [ ] Sober Drive Organizer
- [ ] Chapter Dinner Organizer
- [ ] New member on-boarding
- [ ] Easier Webhooks
- [ ] Roster
  - [ ] Seniority Points
  - [ ] Member Status
- [x] Triangle Code of Ethics

## Creating your own

If you're a Triangle chapter, looking to add this to your own Slack team. You can deploy this application directly to [Heroku](https://www.heroku.com/) using this deploy button.

[![Deploy](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy)

If you're looking to adopt this for your organization, you should fork this repository and make the changes you're looking for. Make sure to update the [app.json](app.json) with URLs so your new repository, and then the deployment to [Heroku](https://www.heroku.com/) will go smoothly.

## Development

After cloning this repository locally, one the first things your going to need to do in order to be able to run it is to create an `.env` file.

The following variables need to be populated in order to run the application locally. If you have something deployed already, it's probably best to just use the same values from the server environment.

Variable|Purpose
:---:|:---:
DJANGO_SECRET_KEY|Secret used by Django
SLACK_CLIENT_ID|The client ID that Slack uses to identify your application
SLACK_CLIENT_SECRET|The secret that Slack has generated for your application. You can regenerate this value if you accidentally make it public, but you should make an effort to keep this private.
SLACK_VERIFICATION_TOKEN|The message verification token that Slack has generated for your application. You can regenerate this value if you accidentally make it public, but you should make an effort to keep this private.
SLACK_API_TOKEN|This is the Application API token that is generated for your application when it is installed onto your Slack team. This should be kept private.
BOT_API_TOKEN|This is the Bot user API token that is generated for your application's bot user when it is installed onto your Slack team. This should be kept private.


### Environment Installation

### Docker Environment
