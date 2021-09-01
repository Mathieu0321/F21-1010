
m4_include(../../../setup.m4)

# Lecture 5 - Testing

## Our Sample Chunk of Code

main.py
```
m4_include(step-5.py)
```

mi_to_km.py
```
m4_include(mi_to_km.py)
```

## Importance of Testing


### Deadly radiation therapy

The Therac-25 medical radiation therapy equipment was involved in
several cases where massive overdoses, often 100x the expected amount, of radiation was administered
to patients.  This killed at least 3 people.

This was not a one-time event.  IN 2000 in Parama City Florida
a set of "planning" software had an error that resulted in
a large set of patients receiving excessive rations.
Al teat 5 died.

In both cases tests did not check for all possible inputs 
and these should have been prevented with unit tests.

### Crashed into Mars

The Mars Climate Orbiter had a contractor that used English
units in calculating the distance from the orbiter to
the surface of mars.  The other software on the system
used metric.  A mile is not a kilometer and the MRO
mis-calculated how close to the surface it was.  Boom.
Years lost and $327 million incest.

### Knightb $440 Million Oops... 

Knight, a middle layer vendor in stock trading, attempted to
upgrade the system - without testing the software upgrade
process.  They failed to remove the old software when they
installed the new.  So the old software kept re-issuing trades
when the trade had already taken place and they lost $440
million in under 30 minutes.   This killed the company.

## Unit Tests

Our Pattern is:

1. Call some set of code
2. Know an expected result
3. Compare what we "got" from the call with "expected" values.
4. If they don't match - then report an error and count up the number of errors
5. Do more...



## Testing With State


## Pure Functional Testing


## Code Review


## Integration Testing



# Copyright

Copyright (C) University of Wyoming, 2021.


