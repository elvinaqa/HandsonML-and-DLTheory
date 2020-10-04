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
