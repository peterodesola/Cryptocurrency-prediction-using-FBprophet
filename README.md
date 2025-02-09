# CRYPTOCURRENCY PREDICTION USING FB-PROPHET
## TABLE OF CONTENTS
- [INTRODUCTION](#INTRODUCTION)
- [CRYPTOCURRENCY](#CRYPTOCURRENCY)
- [PROBLEM DEFINITION](#PROBLEM-DEFINITION)
- [DATA COLLECTION](#DATA-COLLECTION)
- [DATA UNDERSTANDING](#DATA-UNDERSTANDING)
- [DATA PREPARATION](#DATA-PREPARATION)
- [DATA VISUALISATION](#DATA-VISUALISATION)
   - [UNIVARIATE ANALYSIS](#UNIVARIATE-ANALYSIS)
   - [MULTIVARIATE ANALYSIS](#MULTIVARIATE-ANALYSIS)
- [CORRELATION](#CORRELATION)
- [BITCOIN PRE-PROCESSING](#BITCOIN-PRE-PROCESSING)
- [MODEL DEVELOPMENT](#MODEL-DEVELOPMENT)
- [MODEL APPLICATION](#MODEL-APPLICATION)
    - [FORECAST USING FACEBOOK PROPHET](#FORECAST USING FACEBOOK PROPHET)
    - [SOFTWARE DEVELOPMENT](#SOFTWARE-DEVELOPMENT)
- [GRAPHICAL USER INTERFACE DEMO](#GRAPHICAL-USER-INTERFACE-DEMO)
- [EVALUATION](#EVALUATION)
- [RECOMMENDATION](#RECOMMENDATION)
- [CONCLUSION](#CONCLUSION)

  
## INTRODUCTION
Solent intelligence is a leading financial organisation which deals with stock and shares, savings and investments. They are into online investments platform that allows millions of subscribers with over 150 billion pounds worth of investment.
SOLiGence is a multiple stock trade investor that would like to design a platform for cryptocurrency predictions and so therefore, this project has been designed to predict cryptocurrency prices in order to know the prices of coins to make profit. 20 coins would be predicted using FBProphet machine learning model in the predictions of cryptocurrencies, the model will be trained to use real time cryptocurrency data which would be extracted from yahoo finance for predictions. 
## CRYPTOCURRENCY
Cryptocurrency can be defined as a way by which digital currency is used as medium of legal exchange through a computer network that does not depend on any central authority.
Cryptocurrencies are in the form of coins or tokens.
Examples of cryptocurrencies are Litecoin, Ethereum, Zcash, Dash, Ripple, Monero, Bitcoin Cash, NEO, Cardano, EOS.
Cryptocurrency is built on digital blockchain technology that can only be assessed online, it is a tradable digital asset, which does not exist physically like paper money. 
## PROBLEM DEFINITION
We aim to create a platform or application to predict cryptocurrencies prices in order to boost client’s interest to invest in the stock market.
## DATA COLLECTION
Real time data for 20 cryptocurrencies coins were extracted from yahoo finance into a csv format (my_crypto_data.csv), containing historical date, open, high, low, volume, dividends, stock split. Forecast csv files for each coin were also saved through the forecasted historical data for various coins forecasted.
Real time data was collected from yahoo finance in order to have validated and automated data uploaded by the users.
In the image below shows that there was no issue with the data, but there were some missing values.

![Screenshot 2022-05-09 222530](https://github.com/user-attachments/assets/94ce13f8-939f-4e39-8a7c-b0ff0b1887d4)

## DATA UNDERSTANDING
## NAME	DESCRIPTION	                                                                                DATA-TYPE	              EXAMPLE
-	Date:	  (The date of the stocked data was observed)	                                                  (Ordinal)	               (2019-03-01)
-	Open:	  (The stock price when the market opened each day)	                                            (Ratio)	                 (3853.757080)
-	High:	  (Attained highest price value over the period in the market)	                                (Ratio)	                 (3907.795410)
-	Low:	  (The lowest value over the period in the market)	                                            (Ratio)                	 (3851.692383)
-	Close:	(The stock closed price each day)	                                                            (Ratio)	                 (3859.583740)
-	Adjusted close:	(The stocked price when the market closed, adjusted for stock splits)	                (Ratio)	                 (3859.583740)
-	Volume:	 (Security total amount of changes over a given period of time)	                              (Ratio)                   (170038301.0)

## DATA PREPARATION
To ensure optimal model performance, our dataset must be meticulously prepared. Data sourced from platforms like Yahoo Finance can be messy and disorganized, with missing values that may severely compromise the accuracy of our stock predictions. Therefore, thorough data preparation is crucial to avoid erroneous outcomes.
After importing our CSV file—named “my_crypto_data.csv” and obtained via the Yahoo Finance API—we begin by inspecting the dataset for missing values. The following code (as shown in the image below) demonstrates how to perform this check.

![Screenshot 2022-05-11 022639](https://github.com/user-attachments/assets/418f0e34-5dd6-4e76-b634-65d68daa0472)

![Screenshot 2022-05-11 023350](https://github.com/user-attachments/assets/21ff0c9d-6234-445d-b3d1-5150bf5b2f67)

The image above demonstrates our method for checking missing values. We observed that most of the missing entries occurred in the "adjacent close" field; therefore, in our subsequent code, these values were dropped because they are not relevant to our predictions and constituted a significant portion of the data. All cryptocurrency data was collected from Yahoo Finance and pre-processed accordingly. While every coin underwent this preparation, Bitcoin is used as the primary example for illustration.

## DATA VISUALISATION
This is the aspect of machine learning where data are being explore through visualisation for better understanding and to have more insight of the data we are working with. The mean, median and mode of the dataset have been calculated and our dataset analysis can be divided into two, namely
The Univariate analysis: Univariate involves the use of one variable for data understanding.
The multivariate analysis: Multivariate analysis involves analysing with more than one variable.
The mean, median and mode results are shown in the image below
### MEDIAN
![Screenshot 2022-05-11 002920](https://github.com/user-attachments/assets/d890181b-66dd-4967-ae4f-6dbb2cfaab5f)

### MEAN
![Screenshot 2022-05-11 003000](https://github.com/user-attachments/assets/11f7e5ee-5553-4acb-869c-7e7608e95741)

### MODE
![Screenshot 2022-05-11 003038](https://github.com/user-attachments/assets/f3c647a4-2092-4e5e-8cfc-9186836f5f9a)

## Univariate analysis
The target variable which is ‘Close’ has been mostly used for the single variable analysis since it’s our dependent variable.
In the univariate analysis for volume below shows that there are outliers in the dataset, but we are not using volume for our target variable, so it has no effect on our prediction, also we are using fbprophet model which knows how to handle outliers as the model was designed in a robust way.

![Screenshot 2022-05-11 010442](https://github.com/user-attachments/assets/5247ecca-9b70-40b9-81f4-b09e534bbcfb)

![Screenshot 2022-05-11 010247](https://github.com/user-attachments/assets/92714186-5187-4955-bd98-98863844fa03)

## Multivariate Analysis
Analysing with multiple variables as shown that the attributes are highly similar as shown in the images below.

![Screenshot 2022-05-11 005549](https://github.com/user-attachments/assets/0f0c5351-3505-4960-b335-b37bedb70360)

![Screenshot 2022-05-11 005313](https://github.com/user-attachments/assets/9df02b9a-c378-4a5f-84f9-bb7e9640b92b)

## Correlation
The correlation shown in the table below has shown high correlation with the output. There is high correlation between Close, Open, Low and High, however no genuine correlation between volume and other variables.

![Screenshot 2022-05-11 012222](https://github.com/user-attachments/assets/1f309e7d-e4ea-4b82-acc3-48cb24a49584)

## BITCOIN PRE-PROCESSING
Bitcoin was introduced by Satoshi Nakamoto (2008), it is known as the world’s most valuable and profitable cryptocurrency, Bitcoin network of nodes was started in 2009. It is enabled by the blockchain technology and allows for peer-to-peer transactions secured by cryptography.
I have chosen a bitcoin of the cryptocurrencies extracted for illustration of data pre-processing and prediction using fbprophet.
Missing values was checked and non was found because we have fixed it generally initially.

![Screenshot 2022-05-11 033217](https://github.com/user-attachments/assets/df0e9605-19d0-4fb0-9115-fb3bd5a63e21)

We verified that our values were already in float format, so no additional conversion was necessary. For fbprophet, however, the independent variable (x) and dependent variable (y) need to be renamed to “ds” (representing the date) and “y” (representing the Close price), respectively. In our model, the Date serves as the independent variable, while the Close price—our target variable—is used on the y-axis. The Close price is particularly suitable because its output values are closely ranged, contributing to more accurate predictions.

![Screenshot 2022-05-11 034350](https://github.com/user-attachments/assets/fa242f15-ae09-4d25-b747-199fa5098faf)

![Screenshot 2022-05-11 040008](https://github.com/user-attachments/assets/b10cee06-d8c8-4bd6-8372-3535e61c4cfd)

## MODEL DEVELOPMENT
FBProphet is an open-source tool from Facebook that is designed for forecasting time series data, and it enlighten businesses to be understood and possibly it predicts the market prices. It is based on a decomposable additive model where non-linear trends are fit with seasonality; also, all holidays’ effects are put into account.
“FBProphet” was released in 2017, it is an open-source library available on R or Python which helps users to analyse and forecast time-series values.
Prophet is designed to forecast time series data based on an additive model whereby non-linear trends are fit yearly, weekly and daily seasonality, plus holiday effect. 
## WHY THE MODEL IS SUITABLE
-	FBProphet work best with several seasons of historical data that have strong seasonal effects.
-	It handles outliers and missing data well because it has a robust package.
-	It is an auto machine learning package that predicts data using seasonality which can be based on daily, weekly, monthly and yearly
Some important terminologies to take note:
-Trend: The trend shows the tendency of the data to increase or decrease over a long period of time and it filters out the seasonal variations.
-Seasonality: Seasonality is the variations that occur over a short period of time and is not prominent enough to be called a “trend”.
 The “Prophet Equation” fits, as mentioned above, trend, seasonality and holidays. This is given by,

                  y(t) = g(t) + s(t) + h(t) + e(t)
where,
-	g(t) is the trend (the changes that occurs over a long period of time)
-	s(t) refers to seasonality (periodic or short-term changes)
-	h(t) refers to how holidays affect the forecast
-	e(t) refers to the unconditional changes that is specific to a business or a person or a circumstance. It is also called the error term.
-	 y(t) is the forecast.
## MODEL APPLICATION
The model has been used in so many cryptocurrencies’ predictions and other machine learning projects which is one of the reasons I chose it and because it has been designed specifically for time series projects with so many automated functions. Some of the projects are “Bitcoin prediction using ARIMA AND FBProphet (Cayir, 2018)”, and “Nationwide sustainable renewable energy and Power-to-X deployment planning in South Korea assisted with forecasting model (Lim, 2021.)”.
Fbprophet gives information about upper and lower limit prediction, it does not just give only predicted values, which could be of great advantage to investors and traders.
FBProphet is going to predict coins ‘Close price’ according to the required date.
- Model application
There is need to split independent variable “Date” and dependent variable “Close”
Into “ds” and “y” in the columns respectively and to convert non-stationary data to stationary which also converts trends to more linear trends.

![Screenshot 2022-05-11 122121](https://github.com/user-attachments/assets/e7100231-a7a4-478f-a309-2d67e7605f0a)

FBProphet requires minimal pre-processing for cryptocurrency predictions— the steps outlined above are all that's needed. Now, we simply initialize the model by calling Prophet() and fit it using our dataset (named “prophet_btc”, based on the file name).
The same model was also applied to data for other cryptocurrencies to generate future forecasts.
![Screenshot 2022-05-11 125000](https://github.com/user-attachments/assets/197546b2-0ef9-42ca-9eac-cd7eb97c222b)
## FORECAST USING FACEBOOK PROPHET
With our dataset fully prepared for forecasting using the FBProphet model, we now intend to predict values 100 days into the future. Since the historical data is recorded daily, we set the number of periods to 100 so that each period corresponds to one day.

![Screenshot 2022-05-11 155621](https://github.com/user-attachments/assets/c0b9b3cf-b396-4190-8458-91da48007f82)

![Screenshot 2022-05-11 155621](https://github.com/user-attachments/assets/a1e49d2e-8e31-47c1-a006-adb06409b5e7)

![Screenshot 2022-05-11 162458](https://github.com/user-attachments/assets/03943a9c-b22b-4854-859f-88145a86dec4)

![Screenshot 2022-05-11 162643](https://github.com/user-attachments/assets/02b4e1a8-d883-49c8-bc35-140b016d5ae3)

Our dataset spans from 2019/03/01 to 2022/03/03, and the additional 100 days extend this timeline into the future. In the forecast output, "yhat" represents the predicted value, "yhat_upper" shows the upper limit of the forecast, and "yhat_lower" shows the lower limit. FBProphet includes internal visualization tools that allow us to display the forecast by simply passing the new forecast dataframe. The image below illustrates our Bitcoin forecast.
![Screenshot 2022-05-11 163139](https://github.com/user-attachments/assets/900251fe-d272-4cdf-acb8-910c7b08835b)

-	The black line represents the actual data
-	The blue line represents the predicted value
-	The shady area shows the upper limit and lower limit.
Now we can go on by visualising the trends with the plot_component function as shown below:
![Screenshot 2022-05-11 164810](https://github.com/user-attachments/assets/411348c0-0d4c-421e-8e41-ffa2513defe9)

There are clear daily, weekly, and yearly trends in Bitcoin's price. Our analysis of four to five years of historical data reveals that Bitcoin tends to peak toward the end of the year—particularly in November—and usually dips in the middle of the week (notably on Tuesdays and Thursdays). On a daily basis, price fluctuations are inconsistent, but outside these periods, the price remains relatively stable.
Based on these observations, our model provides actionable insights for cryptocurrency trading:
- Buy Signal: When Bitcoin's closing price falls below the predicted value (yhat), it suggests that the price may rebound, presenting an optimal buying opportunity.
- Sell Signal: Conversely, when the closing price is above yhat, it indicates a likelihood of a price drop, making it an optimal time to sell.
- Volatility Considerations: Given Bitcoin's inherent volatility, there are instances where the closing price may hover near the lower bound (yhat_lower) on some days and approach the upper bound (yhat_upper) on others. These three parameters—yhat, yhat_lower, and yhat_upper—provided by Facebook Prophet, form the basis for our investment decisions.
## SOFTWARE DEVELOPMENT
For the graphical user interface, we used Streamlit, an open-source application framework that simplifies the creation and deployment of data science applications. Streamlit enables data scientists and machine learning engineers to develop performant, custom applications in a short time frame, allowing businesses to interact directly with their models and data.

## Implementation Details
- The required libraries were imported, and additional packages were installed via the terminal using pip.
- This setup allowed the Streamlit application to seamlessly connect to our data, making it possible to visualize and interact with our forecast outputs in real time.
This approach not only streamlines the data processing and forecasting workflow but also provides an intuitive interface for end users to explore and make informed investment decisions based on our model’s predictions.
Then another file was created using python file, reason being that Jupiter file cannot work with streamlit. I created another file (python) and moved some of my codes into the new file for connection of crypto codes and the GUI. Real time data was extracted, we trained our data, dataset was split into x and y “date” and “Close” independent and target variables respectively. And finally our data was forecasted
Streamlit was created with a command (streamlit run cryptonw.py) for connection of the graphical user interface python. After the use of the  streamlit run command, a link was generated and the link is for the GUI.

![Screenshot 2022-05-13 034130](https://github.com/user-attachments/assets/e5c1737f-298d-435f-9f66-f145ffaa22f9)

## GRAPHICAL USER INTERFACE DEMO
![Screenshot 2022-05-13 041910](https://github.com/user-attachments/assets/d1918f88-3ec4-4056-a62a-e42cb913d597)

## EVALUATION
Model evaluation relies on performance metrics.  These metrics, such as mean squared error, mean absolute error, and root mean squared error, quantify the model's accuracy and inform performance analysis.

![Screenshot 2022-05-12 003227](https://github.com/user-attachments/assets/1840e120-fa80-49f3-a70a-52519555194b)

## RECOMMENDATION
This project is highly engaging and valuable. I recommend its continuation, as cryptocurrency trading is a significant and growing trend.  For future iterations, I suggest ensuring all library packages are compatible and optimized for accurate predictions.  Additionally, a thorough evaluation of various neural network models is crucial for project success.
## CONCLUSION
This project provided valuable insights into a range of machine learning and deep learning models, highlighting their performance characteristics in different contexts.  It also demonstrated the potential of digital currency trading and the advantages of cryptocurrency investment.  Through experimentation with various models, including some that proved unsuccessful, I gained a deeper understanding of model selection.  Ultimately, I discovered the effectiveness of FBprophet, particularly for time series analysis.  Finally, the project reinforced the wide availability and utility of Graphical User Interfaces (GUIs) for diverse project needs.



