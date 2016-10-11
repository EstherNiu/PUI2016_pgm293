## Citibike peer- review ##

The null hypothesis is correctly formulated in words and formulae.

I need the weather data to be extracted live in the notebook. Alternatively I need a discussion of why that cannot be done, and a description of how to do that. In this case (it cannot be extracted live) if it is not too large the data should be checked in the current directory and accesses directly from it, if it is too large a subset of the data should be made available as example and to allow the notebook to work.

The data wrengling is technically fine, but not finished.

1. you are extracting the trip duration, when your hypotheses are forumlated in terms of number of trips, not of trip duration.

2. the data is not grouped by week yet, so we still have just a bunch of trip durations for days in july. you need to count them per week


3. the weather data is still in days, not weeks as well

4. you have not joined the 2 notebooks, so that we still do not have the precipitation per week and numbers of ride per week


At that point the data MAY support the question IF you have two weeks in the weather data with SIgNIFICANTLY different precipitation. So the way you set it up now you need

1. a test of means for the precipitations for the 4 weeks of july (t test for example)

2. a test of means for the number of rides per week

3. assess if you see a statistically significance difference in test 2 between weeks that were statistically different in test 1
