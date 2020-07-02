# Startups Assessment using Machine Learning

During final semester we got a chance to work for a crowdfunding company name RedCrow which works with early-stage startups and help them to achieve their desired crowdfunding. And we where asked to come up with a solution that helps or adds value to their client/startup companies acheive their desired goals effectively. We have build a prototype of a web application that aids as a tool for both inverstor and company/startup.

**For Investor:** Provided Startup inputs such as(Location, Market, Years, Funding,etc) tools can predict the success probability of a startup.

* Trust : estimate the position of startups
  * Can help startups to predict their prospect based on historical analysis
  * Investors to get confidence on startups and associated domain
  
  Data Source : https://www.kaggle.com/mauriciocap/crunchbase2013


**For Startups/Companies:** Provided startup information and its social media features such as Followers and Following, tool can predict its success probability from one funding round to another, so that startups can strategize their social presence before organizing crowdfunding campaigns or stage funding. 

* Stage evolution : startups movement from Seed to Stage A
  * Support hypothesis of association between funding stage with digital & social presence
  * Probability of startups to establish Seed and Series A funding position

Data Source : Web Scraped from Angelist.co/compnies (for startup info) and Twitter(for startups social presence)


 
![World Finance Review](https://github.com/Sagar401/Startup_Assessment_using_ML/blob/master/startups_world_finance_review.jpg)

# Startups Assessment using Machine Learning

A startup company grows and grows until it proven itself – we had a prolific engagement with RedCrow (crowdfunding platform) company during our final semester capstone project work. RedCrow connects financial and human capital to healthcare start-ups. Despite of the fact that there are several prominent reasons for a startup to fail, “funding” still stands as foremost as this is the backbone of any unit to operate. There have been several studies in past in order to forecast the growth and success of startups. This project offers a web-based comprehensive decision-making tool to cater two broader spaces:

**Predict the final position of startup (operational or close):** able to support startups, investors and investment platforms like RedCrow to predict the unicorn’s prospects.

* Analytical Approach:
  * Data Source: https://www.kaggle.com/mauriciocap/crunchbase2013
  * Key Features: Average Funding, Total Funding, Delta between First and Last funding, No of Investors, Funding Rounds, Market Category etc.
  * Outcome: Startups Stage as Operational Or Close

![StartupPositionFlow](https://github.com/Sagar401/Startup_Assessment_using_ML/blob/master/PositionFlow.jpg)

** **

**Stage evolution : startups movement from Seed to Stage A:** 
  * Support hypothesis of association between funding stage with digital & social presence
  * Probability of startups to establish Seed and Series A funding position


* Analytical Approach:
  * Data Source: Web Scraped from Angelist.co/companies (for startup info) and Twitter(for startups social presence)
  * Key Features: Total Funding, Annual Funding, Size, Market Category and Twitter Followers etc.
  * Outcome: Raised 2m (0- No, 1- Yes) for Seed Stage and Raised 12m( 0- No, 1- Yes) for Series A

![StartupStageFlow](https://github.com/Sagar401/Startup_Assessment_using_ML/blob/master/StageFlow.jpg)

** **

**CRISP-DM Methodology:** - for improvised outcome
![WebAppFlow](https://github.com/Sagar401/Startup_Assessment_using_ML/blob/master/WebAppFlow.jpg)

** **

**Web Application Demo** - Startup Operational Position Prediction 
![WebAppDemo](https://github.com/Sagar401/Startup_Assessment_using_ML/blob/master/WebApp.gif)
