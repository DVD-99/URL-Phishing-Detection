# Detecting Phishing URLs using Machine Learning

Almost 70% of cyber-attacks that take place are phishing, mainly public, information, financial services websites are the once which are more prone to phishing attacks.

```main.py```
It is the primary driver function, which has a Decision Tree model User has to enter the URL when prompted; it then calls the Features.py and predicts where legitimate or not.

```Features.py```
This file contains the implementation of all the 30 features required to convert the given URL into the features.

```clasification_compare.py```
I used the sklearn library for SVM, Decision Tree, Naive Bayes, and a function to plot a graph.

Trained the machine learning models with a dataset of 6157 phishing websites and 4898 legitimate websites. The URL is transformed into 30 features, as mentioned in [Phishing Websites Features!](http://eprints.hud.ac.uk/id/eprint/24330/6/MohammadPhishing14July2015.pdf)

![graph](https://github.com/DVD-99/URL-Phishing-Detection/blob/main/graph.PNG)

The Decision tree has the highest accuracy with 95.05 compared to various machine learning classification algorithms. Depending on the accuracy so far, choose the Decision Tree Algorithm. The problem here is that criminals are making new strategies to counter our defense measures. So, we need algorithms that continually adapt to new examples and features of phishing URLs. Online learning algorithms provide better learning methods compared to batch-based learning mechanisms.
