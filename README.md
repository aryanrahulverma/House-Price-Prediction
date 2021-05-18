# House Price Prediction
Consider moving to a new city and not knowing anything about that area or the city. And the broker you hired is not that selfless, so he may tell you the price that is nowhere close to its actual value. Or even if you are constructing the house, the builder with no proper knowledge may go over your budget. But with proper house price prediction model he can make construction estimation plan with not much difficulty.

## Workflow
![image](https://user-images.githubusercontent.com/64376922/114908352-a5633980-9e39-11eb-8348-28de71069a42.png)

## Deployment
#### Input Form
![image](https://user-images.githubusercontent.com/64376922/118694985-4d4d9780-b82a-11eb-9591-b329537ceb1a.png)

#### Prediction
![image](https://user-images.githubusercontent.com/64376922/118694926-4030a880-b82a-11eb-8df6-0d0be05729a0.png)

I deployed my model on a webpage using Flask. The form takes input for the model and acts as test set. The data is provided to the model and the house price is predicted.

## Summary
For simplicity, many people solve problem with linear regression with one feature and one target. But most problems solved with help of linear regression model require more than one feature. To get the best result there are many parameters to take into consideration.
For example, if we want to calculate eligibility of a person to apply for loan, apart from his income we also need to consider his credit score that is his CIBIL score as well.
So, we have implemented linear regression with multiple features for house price prediction that helps conservative people with their budgets and business strategies, who are looking to purchase a new home. The current method includes the estimation of house prices without predicting future market conditions and price changes as appropriate. 

We used various libraries to ease the work and get better understanding of what has been done. Some libraries used are – 
1.	Pandas – to read and manipulate data as per requirement
2.	Numpy – to vectorize our data and prepare for use in efficient calculations 
3.	Sklearn – it provides many built-in functions that are required for linear regression . It simplifies code and reduces extra work
4.	Flask - to deploy my machine learning model on the webpage.

First the data is loaded into data frame using panda’s library and separated the features and target. Then regression model is defined, and object created for the same. After that, we fit the model with help of sklearn library and train the model with the training set that was split from the main dataset. After constructing the model, we are ready to use that model to predict house prices.
