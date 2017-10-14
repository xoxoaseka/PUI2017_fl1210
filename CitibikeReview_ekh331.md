# Overview

## In this file, I will:
1. Verify that null and alternative hypothesis are formulated correctly;
2. Verify that the data supports the project
 "if the a data has the appropriate features (variables) to answer the question, and if the data was properly pre-processed to extract the needed values"
 
3. Choose an appropriate test to test the null hypothesis
4. Provide additional comments, suggestions, and a suggested appropriate statistical test with justification.

# 1. Hypothesis review
The idea to be investgated is the following:
"Older people are less likely than younger people to use citibikes overnight (19:00-5:00)"
This is an interesting question, and I think it will come down to what designates "older"  versus "younger" people.
The idea above is somewhat imprecise, leaving it open to multiple interpretations. One such interpretation is the null and alternative hypothesis provided in the assignment: <br>


The following null hypothesis and alternative hypothesis are described. <br>
Null: "The ratio of older people (>=40) biking at night over all older people biking during a day is _the same_ or _higher_  than the ratio of younger people (< 40) biking at night to all the younger people biking during a day"
<p>
Alternative: The ratio of younger people biking at night over the total number of younger people riding a bike during a 24 hour period is greater than the ratio of older people riding a bike at night over the number of older people who ride bikes in the 24 hour period.
<p>

One way to write the null hypothesis that should be considered is that instead of having the proportions in a kind of inequality 
(young proportion is less than or equal to old proportion), the proportions should be set as equal to each other,
since we know nothing about the proportions. The default assumption should be that they are equal instead of an inequality.

The student chose an alpha of 0.05, meaning that under the null hypothesis, the probability of obtaining a result as least as significant would be 5%. 

<p>

# 2. Data review

The idea of older people having a different probability than younger people of riding Citibikes at certain times of day 
requires the use of age data and time data. Since we only care about when someone is attempting
to use a bike, we can only consider the start time of the citibike trip.

This is accurately reflected in the data chosen. The data are also cleaned and processed to have
only relevant information (age and trip start date in datetime format). This is all that is needed.

<p>

# 3. Choosing a Statistical Test
<p>
The null hypothesis is that these ratios are equal. We need to come up with some statistic with a dstribution under the null hypothesis. Let's say the null hypothesis is true.
We look at old people riding bikes. Some are riding at night, some in the morning/day. There is a fraction for each. The same applies to young people. Since we only care about night riders, there is an "old people" Bernoulli distribution and a "young people" Bernoulli distribution of ridership (binary yes/no to answer the question "is the ride at night?" for young people and old people). 

If the null hypothesis were true, there would only be one distribution from which the samples of both young and olf riders are pulled. So, we should check to see if the samples come from the same or different populations (is there only one distribution or are there two?).

The data are obviously not normal-- a person is either a night rider or they are not-- so a non-parametric test is required. 

There is one treatment variable, and the data are unpaired. There are at least 30 observations per sample, as we are dealing with many Citibike trips, so the desired statistical test is the <b>z-test for unpaired data</b>.


