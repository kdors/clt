# Visualizing the Central Limit Theorem for Sums

This is a website made using flask that helps to visualize the central limit theorem when applied to sums. Using the box model, summing up a number of draws taken randomly with replacement from a box with specified "tickets" will eventually follow the normal distribution regardless of the contents of the box as the number of draws taken increases.

The expected value of the sum of the draws is the average of the box multiplied by the number of draws.
The standard error of the sum of the draws is the standard deviation of the box multiplied by the square root of the number of draws. This can be seen for larger numbers of draws.

This flask app allows you to choose the number of draws you want to take and the number of trials you want to do. As the number of draws increases, and at a good trial size, the data begins to closely resemble the normal probability distribution.

The visualization was created using Chart.js.
The app requirements are listed in requirements.txt.
