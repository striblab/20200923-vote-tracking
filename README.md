# 2020 early vote tracking

## Setup
- Rename .env.sample to .env, and check for any settings you need to adjust for your local aws setup.
- Make sure there is a /src/scraper/json/versions folder
- If you want to deploy test versions with surge, be sure you have surge installed globally (`npm install -g surge`)

Then:
```
npm install
npm run dev
```

## Running the scraper
When new data comes out on Fridays, the scraper will download the new weekly data and update the overall timeseries on S3.

As long as things are working well, you only need to run the .sh command below.

But for debugging purposes, inside the .sh command, `scrape_county_list.py` will create a version file of the current weekly data, and then `combine_weekly_versions.py` will merge all the existing versions together. The rest of the .sh command is checking if the json has changed and appears valid, and if so it uploads a new version to S3.
```
cd src/scraper
pipenv install <-- First time only
pipenv shell
./deploy_county_list.sh
```

## Deploying to CMS
Code from public/index.html goes into an LCD like previously. Then run `npm run deploy` and choose "production" to update the static files. There should be at least an h1 and a few paragraphs hardcoded into index.html/the LCD for SEO purposes, otherwise Google will mostly ignore it.


## General svelte/buildpack notes

This is a project template for [Svelte](https://svelte.dev) apps. It lives at https://github.com/striblab/svelte3-template-webpack and is a fork of https://github.com/sveltejs/template-webpack.

To create a new project based on this template using [degit](https://github.com/Rich-Harris/degit):

```bash
npx degit striblab/svelte3-template-webpack svelte-app
cd svelte-app
```

*Note that you will need to have [Node.js](https://nodejs.org) installed.*


## Get started

Install the dependencies...

```bash
cd svelte-app
npm install
```

...then start webpack:

```bash
npm run dev
```

Navigate to [localhost:8080](http://localhost:8080). You should see your app running. Edit a component file in `src`, save it, and the page should reload with your changes.

### Deploying with [surge](https://surge.sh/)

Install `surge` if you haven't already:

```bash
npm install -g surge
```

Then, from within your project folder:

```bash
npm run build
surge public
```
