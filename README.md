<h1 align="center"> Pili-Balita Fast API </h1>

This repository is part of [Pili-Balita](https://github.com/jeraldconstantino/pili-balita) project. It contains machine learning model that would be deployed in [Heroku](https://www.heroku.com/) cloud platform to accessed by the Pili-Balita software via Internet.  

## Machine Learning Deployment in Heroku
1. Visit the [Heroku](https://www.heroku.com/) website. 
2. Create an account. If you already have one, you may proceed to log in it. 
3. Once you successfully logged in, click the "new" dropdown button that can be found at the top-right part, and hit the `create new app`.  
4. Provide an your desired App name. Once inputted, there is an indicator there if the name you've provided is available.
5. Add a payment method. (Don't worry, Heroku will not charge you at this time)
6. After that, hit the `create app` button.
7. The deployment method in Heroku have three different options, but choose GitHub. 
8. Next, connect this repository by searching the pili-balita-fast-API and hit the `connect` button.
9. Make sure that you have click the `Enable Automatic Deploys` button, so that whenever there is a changes happened in this repository, it will be automatically updated on the other side. 
10. Choose the `main` branch and hit the `Deploy Branch` button. At this moment, the build has started if you observed the logs. 
