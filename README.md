# Visualzing Central Limit Theorem

This is a flask app that helps to visualize the central limit theorem. Using the box model, summing up a number of draws taken randomly with replacement will eventually follow the normal distribution regardless of the makeup of the box as the number of draws taken increases.

The expected value of the sum of the draws is the average of the box multiplied by the number of draws.
The standard error of the sum of the draws is the standard deviation of the box multipied by the square root of the number of draws.

This app allows you to choose the number of draws you want to take and the number of trials you want to do. As the number of draws increases, and at a good trial size, the data begins to closely resemble the normal probability distribution.

The visualization was created using Chart.js. 
The app requirements are listed in requirements.txt.


