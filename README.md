# HandsonML-and-DLTheory

TPU Processing 

# The Unreasonable Effectiveness of Data
In a famous paper published in 2001, Microsoft researchers Michele Banko and Eric
Brill showed that very different Machine Learning algorithms, including fairly simple
ones, performed almost identically well on a complex problem of natural language disambiguation

## The importance of data versus algorithms
As the authors put it: “these results suggest that we may want to reconsider the tradeoff between spending time and money on algorithm development versus spending it
on corpus development.”
The idea that data matters more than algorithms for complex problems was further
popularized by Peter Norvig et al. in a paper titled “The Unreasonable Effectiveness
of Data” published in 2009.10 It should be noted, however, that small- and mediumsized datasets are still very common, and it is not always easy or cheap to get extra
training data, so don’t abandon algorithms just yet.


### Popular open data repositories:

— UC Irvine Machine Learning Repository
— Kaggle datasets
— Amazon’s AWS datasets
• Meta portals (they list open data repositories):
— http://dataportals.org/
— http://opendatamonitor.eu/
— http://quandl.com/
• Other pages listing many popular open data repositories:
— Wikipedia’s list of Machine Learning datasets
— Quora.com question
— Datasets subreddit

## Pipeline
A sequence of data processing components is called a data pipeline. Pipelines are very
common in Machine Learning systems, since there is a lot of data to manipulate and
many data transformations to apply.
Components typically run asynchronously. Each component pulls in a large amount
of data, processes it, and spits out the result in another data store, and then some time
later the next component in the pipeline pulls this data and spits out its own output,
and so on. Each component is fairly self-contained: the interface between components
is simply the data store. This makes the system quite simple to grasp (with the help of
a data flow graph), and different teams can focus on different components. Moreover,
if a component breaks down, the downstream components can often continue to run
normally (at least for a while) by just using the last output from the broken compo‐
nent. This makes the architecture quite robust.
On the other hand, a broken component can go unnoticed for some time if proper
monitoring is not implemented.

# Data Analysis vs Analytics Difference
In today's data community, there is some ambiguity about the difference between analysis and analytics. That even happens among HR managers of the companies, finding it hart to differentiate between two, making flaws about finding Data Analytics Speacialists or Data Analysts. Knowing which one is who can definitely help to both sides during job interviews or applications.

Basically, Analysis is about chunking the whole data into small parts to do simpler investigations. One important point to mention about the difference is the PAST data. When doing Data Analysis, we have searching for the reasons about why we have such values in the data, why the value raised or downfell, what are the causes, and how it happened (ex: Stock price).

Talking about Analytics, it is about exploration of th potential future events rather than explaining the reasons of past events. All in all, we definitely need to do some analysis, before we can do analysis or predictions about future probabilities from current patterns.
We have 2 types of Analytics which are Qualitative and Quantitative

Qualitative Analytics is deciding upon your intuition and analysis of the data before you make next business move.
Quantitative, however, is the type of analytics where we decide based off of the algorithms and formulas.
Simple example would be about the clothing store owner. When he wants to decide which clothes to advertise during the year, he has 2 options to opt from. The first way is about reading newspapers, online articles to know more about the people's choice about the trends in terms of clothing. This is the Qualitative way of deciding on your business move.
Next option is about doing investigations on the past sales, following patterns during different months and deciding which clothes to advertise to grab the attention of the customers which is the way when we do Quantitative Analsysis.

# Bayesian Inference
>Sets and Events
>Interaction of Sets
>Union of Sets
>Mutually Exclusive Sets
>Dependent and independent Sets
>Conditional Probability Formula 
>The Law of Total Probability
>Additive Law
>Multiplication Law
>Bayes' Law

## Base Statistics

### Population and Sample

Data and Viz:
	Categorical - freq dist tables, bar chat, pie chart, pareto diagram/ 
	Numerical - freq dist tables, histogram,  
		Discrete
		Continuous
	Cross tables, scatter plots, 
Measurement Levels
	Qualitative
		Nominal - 4 seasons
		Ordinal - worse bad normal nice great
	Quantitative
		Interval - no true o (temprature)(in kelvin, we can say one temp is 2 times colder than the other)	
		Ratio - has zero
Univariate Measures
Mean, median, mode
mean - central tendency measure, however, easily affected by outliers.
median - middle number, not affected by extreme values
mode - most often freq

Skewness - Outliers
right - mean> median	
no skew = mean=median=mode
left - mean < median

Variability
Variance Dispersion
Std Deviation
Coefficient of Variation std/mean

Multivariate Measures
Covariance x-mean * y-mean > <  0
Correlation Covariance cov(x, y)/std(x) std(y)   -1 < x < 1


## Distribution
Normal Distribution - mean=median=mode => no skew
	Higher diversity, high variance, more flatten out the curve
Standard Normal Distribution - mean=0 variance=1
Central Limit Theorem

Standard Error sigma/sqrt n - if sample size increase, std error decreases

### Confidence Interval 
#### T Distribution: 
	Practical example would be about predicting how many shoes to keep in the shop exactly
	or, finding out which shop perform better than the other

#### Hypothesis Testing
	Null Hypo
	Alternative
Errors 
	Type I - Reject a True Null Hypo
	Type II - Accept a False Null Hypo

#### P-value


