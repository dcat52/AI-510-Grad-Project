## CPSC 510 Classification Project Fall 2017

Fork this project into your private group, clone your fork into your user space, make changes as needed, commit, and push to your fork.

You are given:
 * `project510.py` - sample file demonstrating loading, saving, and processing data
 * `project510Data.csv` - data file; it is up to you to separate this file into testing and training data

You are to design a classification program for this data.  You may use any of the prior projects code, and you may use other libraries available online at your discretion.

You will submit your source file(s) with at least three methods for each classifier:
 * `train` - takes in a `csv` file and trains the system given the data
  * The method should return a `tuple` with all relevant parameters
 * `test` - takes a `csv` file with labeled data and trained parameters
  * Returns the total loss for all data points (1/2 sum squared error)
 * `classify` - takes a `csv` file and returns a list of classifications for each element
  * If a data element is not relevant to classifier, set label to `None`.

 In addition to your source code, submit a "pickle" file containing your best trained parameters.  Your `test` and `classify` methods should accept their parameters as an argument.

 Saving to and loading from the pickle file should be done separate from the methods.

We will assume that the `csv` files are all of the same format; you will just ignore the given label when classifying.  If an input column has value less than -2.0, then ignore that entry; for training/testing if a label has value less than -2.0, then it should be skipped.

Our goal is to define a technique that works with four different classification problems:
* classify columns 0-5 as input with column 10 as label
* classify columns 0-6 & 9  as input with column 10 as label
* classify columns 0-6 & 9  as input with column 11 as label
* classify columns 0-6 & 9 & 10  as input with column 11 as label

Some provided data may have invalid data (< -2.0) for some problems, and should be skipped.

You may use any technique we covered in class (e.g. k-nearest neighbor, ANN/DL, Bayesian networks).
You may use another AI technique with prior permission.
You may use online tools and external libraries provided you document the required steps, and explain the approach well.

### Submission

You're not done yet!

Make sure to commit your code and push to your personal fork.

By default pickle (`*.pkl`) files are ignored when committing because binary files
are not as nice for gitlab.  Submit your pickle file, directions document, and your presentation to Scholar.

The due date for the submission is *Friday 1-December at 11:59PM*.
Note: Some of you will be giving presentations prior to this date on Wednesday.

Presentations should be approximately 15 minutes long with good style.
Presentations less than 12 minutes and more than 18 minutes will be penalized.
Expect about 2 minutes of questions after each presentation.

Presentations should cover approach, design, results, and analysis with suggestions for
improving the classifier.

You are required to give a presentation to pass the class; you cannot take a zero on
this assignment and sacrifice the letter grade.  

The project will be graded according to:
 * 50% - grade assigned to your end of semester presentation covering design and results
  * Mostly this grade is based on quality of presentation, and on the design of system, and analysis, and not on quality of results
 * 10% - results of classifying columns 2-5 as input with column 10 as label (fewer valid data points)
 * 10% - results of classifying columns 2-4 as input with column 10 as label (most valid data)
 * 10% - results of classifying columns 0-5 as input with column 10 as label (fewer valid data points)
 * 10% - results of classifying columns 2-5 & 9  as input with column 10 as label
 *  5% - results of classifying columns 2-6 & 9  as input with column 11 as label
 *  5% - results of classifying columns 0-6 & 9 & 10  as input with column 11 as label
</div>
For the individual classifier results grade, I will based 50% on effort for each stage, and 50% on actual quality of classification.
A good design and presentation can get you 50% of score, without attempting code.
An honest effort at implementing your design for each classification problem above, can get you another 25%.  The remaining 25% will be based on the actual quality of your classifier against the data that I have held out.

You may write separate programs for each, or have a variable that you set when calling the programs.
In my example code, I set a ``columns`` list to choose my input data that is selected.

You must provide detailed instructions on running your code given an appropriate `csv` file.
