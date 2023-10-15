# Crime Analysis

The imported CSV file contains approximately 3116 rows, 21 columns. The goal of this project was to familiarize myself with the libraries of Python including, but not limited to, NumPY, seaborn, Matplotlib, sci-kit learn, and more.
![image](https://github.com/moonneer/crime_analysis/assets/108647944/51600b8b-01d7-4ab3-8f18-86cbfc00c4b8)

In the below three images, I built functions to clean the data, prepare it for some visual analysis, and demonstrate the frequency of rates of crime growth within several states. These functions can take in, as arguments, any state + csv file formatted in the same order to give an accurate visual representation of said data.

![image](https://github.com/moonneer/crime_analysis/assets/108647944/ffa25201-679a-4f56-985e-9cc52f11f82b)
![image](https://github.com/moonneer/crime_analysis/assets/108647944/9acc4dc9-6f56-454f-922c-de9e8bd36698)

The above three images are respectively, the rise in crime rates in California and Utah. Only California, amongst the two, witnessed a sharp decrease in crime rates.

![image](https://github.com/moonneer/crime_analysis/assets/108647944/fb7ce96f-612a-4db8-936a-5d826ce8c350)

Then, to further empower the tools available to myself for better analysis. I built a state-by-state visualization, enabling one to compare two or more states on the same graph. This much, was not that difficult.
And then, I ran the regression algorithm to see whether or not Utah will continue experiencing a growth in crime rates for the years following 2019, notwithstanding the fact that it has witnessed a sharp increase in the last 59 years. I trained it on past data, and let it run a predictive model of future crime rates. Not very surprisingly, the results are displayed below.

![image](https://github.com/moonneer/crime_analysis/assets/108647944/ea00c001-3e65-4e79-b926-0a1bdcc238d7)
