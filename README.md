# Project McNulty

## Project Summary

### Intro
America has a electoral participation problem. Our turnout of ~55% of voting age adults for the 2016 presidential election put us [below the vast majority of developed democracies around the world](http://www.pewresearch.org/fact-tank/2018/05/21/u-s-voter-turnout-trails-most-developed-countries/). Another notable fact about the 2016 US presidential election was the outcome -- here was a political outsider who played by none of the established rules of politics and came out victorious. Regardless of position on the political spectrum, many have seen his election as a paradigm shift in the American political system. And presumably, there are many voters who in response have sat up to take notice and engaged more in politics in whatever form. So for my classification project I set out to identify these individuals so that organizations could conduct effective outreach to those who are interested.

### Data
In order to build a model to approach this question, I looked at [this Summer 2017 Pew Research Political Typology survey](http://www.people-press.org/dataset/political-typology-2017/). One of the 164 questions they asked their ~5,000 respondents was "since Donald Trump’s election, would you say you are paying, more, less, or the same amount of attention to politics as you used to?" I chose this question to represent my predictive target, simplifying the response as a binary classification of either more engaged or not, since we're really only trying to reach out to those who are engaging with renewed interest. In addition I selected 20 other primarily demographic features for ease of gathering when deploying the model to identify more people going forward. 

### Analysis
I tried using range of classification models to get some predictive power out of the data. Here are the average results across training cross-validation folds for each just using scikitlearn out of the box implementations:
Model | Accuracy | Precision | Recall
-----|-----|-----|-----|
SVM | 59% | 60% | 71% |
Logistic Regression | 59% | 61% | 68% |
Decision Tree | 59% | 54% | 57% |
K Nearest Neighbors | 58% | 59% | 68% |
Random Forest | 55% | 58% | 55% |
Naive Bayes | 54% | 58% | 45% |

