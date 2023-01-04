<h1 align="center"> Pili-Balita Fast API </h1>

This repository is part of [Pili-Balita](https://github.com/jeraldconstantino/pili-balita) project. It contains machine learning model that would be deployed in [Heroku](https://www.heroku.com/) cloud platform to accessed by the Pili-Balita software via the Internet.  

## Machine Learning Deployment in Heroku
1. Visit the [Heroku](https://www.heroku.com/) website. 
2. Create an account. If you already have one, you may proceed to log in it. 
3. Once you successfully logged in, click the "new" dropdown button that can be found at the top-right part, and hit the `create new app`.  
4. Provide your desired App name. Once inputted, there is an indicator if the name you've provided is available.
5. Add a payment method. (Don't worry, Heroku will not charge you at this time)
6. After that, hit the `create app` button.
7. The deployment method in Heroku have three different options, but choose GitHub instead. 
8. Next, connect this repository by searching the pili-balita-fast-API and hit the `connect` button.
9. Make sure that you have click the `Enable Automatic Deploys` button, so that whenever there is a changes happened in this repository, it will be automatically updated on the other side. 
10. Choose the `main` branch and hit the `Deploy Branch` button. At this moment, the deployment begins as observed the logs. During this stage, it will take some time to process and each library you have inputted on the [requirements.txt](https://github.com/jeraldconstantino/pili-balita-fast-API/blob/main/requirements.txt) file will be installed.
11. Once the deployment stage is successfull, the URL would be generated at the last part of the logs. The generated URL link can be used to PUSH data and acquire the desired information. You can also copy the URL by hitting the `view` button and manually copy the link from the URL holder of your browser.
12. Copy that URL and paste it within the [url.py](https://github.com/jeraldconstantino/pili-balita/blob/main/url.py) file from the [Pili-Balita](https://github.com/jeraldconstantino/pili-balita) repository.
13. Test the URL by PUSHing data to verify if the URL is working.

## Open for Contribution
1. Clone repository and create a new branch: 
```
$ git clone https://github.com/jeraldconstantino/pili-balita-fast-API
$ git checkout https://github.com/jeraldconstantino/pili-balita-fast-API -b name_for_new_branch
```
2. Make changes and test.
3. Submit [Pull Request](https://github.com/jeraldconstantino/pili-balita-fast-API/pulls) with comprehensive description of changes.

### Bug Reports & Feature Requests
Kindly use the [issue tracker](https://github.com/jeraldconstantino/pili-balita-fast-API/issues) to report any bugs or file feature requests.
