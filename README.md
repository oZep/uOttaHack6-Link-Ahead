# Link Ahead

## Challenge
This project is for CSE Machine Learning Challenge:

> **Challenge**: Build a project that uses Machine Learning; Our criteria include application performance, focusing on speed, accuracy, model size, and resource allocation.

## Inspiration
I found an interesting dataset on Kaggle when I was starting to lose hope on making something for this Hackaton. I stumbled upon one about discriminating between phishing links and regular links, I thought it would be an interesting challenge to tackle with my time. Even with the constant advertisements and warnings the Government of Canada outputs exposing these scams, we hear about the elderly, young kids, and unknowing adults falling prey to phishing schemes on the news daily. Taking a real life challenge and applying Machine Learning, and taking it to a point where people from any tech background could use it, seemed like a rewarding task-- One I couldn't pass up.

## What it does
**Link Ahead** is a **machine learning** model and tool that can be used to discriminate between phishing links and non-phishing links with a *92.59% accuracy*. Using this model, I constructed a **Web Application** to allow others to input any link of choice and test the trustworthiness of it. The background ranges from shades of red -- green to demonstrate the severity visibly. I also created a **Google Chrome Extension** that can be used to scan and test the safety of all the links available on any webpage.

## How we built it
To build this tool, I used ...... To build the web app, I used Flask, HTML/CSS/JS. To build the API, I used Flask and data processed via python from the Kaggle source. To build the Google Chrome Extension, I used HTML/CS/JS, while calling to my API repeatedly.

## Challenges we ran into
- Getting a Flask application to be hosted on Vercel [UnSolved - Went with 3 other options then decided to set up out own server]
- Editing Chrome's Manifest to allow access to all web pages [Solved]

## Accomplishments that we're proud of
Despite it all, I was able to solo develop a product that is usable and a helpful tool for everyone’s day to day life.

## What we learned
how to use Flask to build a webpage and API. 
how to utilise the pandas library dataframes to commute row calculations instantly. 
how to call APIs within a Chrome Extension.

## What's next for Link Ahead
Find somewhere to host indefinitely, and upload the chrome extension for approval to be posted on the Chrome Web Store. 

  
[Github] https://github.com/oZep/uOttaHack6-Link-Ahead

[Slides] https://docs.google.com/presentation/d/1_gk9gpgYydGDOnoFh71wkYx1LNCpRqqVUksM8woCePU/edit?usp=sharing

