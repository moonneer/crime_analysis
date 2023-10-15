from SCVS import *

state_crime_data = get_state_crime_data('state_crime.csv')

# 1. Growth Percentage:

# Alabama
alabama = growth_percentage(state_crime_data, 1960, 2019, 'Alabama', 'Data.Population')
"""The state of Alabama saw a 50.9% increase in their population from the year 1960 to 2019"""

# California 
cali = growth_percentage(state_crime_data, 1980, 2019, 'California', 'Data.Rates.Violent.Murder')
"""California experienced a whopping decrease of 70.3% in murder across their state from 1980 to 2019."""

# Utah
utah = growth_percentage(state_crime_data, 2010, 2012, 'Utah', 'Data.Rates.Violent.Rape')
utah_new = growth_percentage(state_crime_data, 2010, 2019, 'Utah', 'Data.Rates.Violent.Rape')
"""Utah's rape cases decreased by 6.8% throughout the years 2010 and 2012 however it increased by 60.5% from the year 2010 to 2019."""

# 2. Visual Model

# Alabama
vis_alabama = visual_model(state_crime_data, 1960, 2019, 'Alabama', 'Data.Population')

# California
vis_cali = visual_model(state_crime_data, 1980, 2019, 'California', 'Data.Rates.Violent.Murder')

# Utah
vis_utah = visual_model(state_crime_data, 2010, 2019, 'Utah', 'Data.Rates.Violent.Rape')


# 3. Comparing Data:

# California vs New York

ala_uta = compare('Alabama', 'New York', 2003, 2016, 'Data.Rates.Property.Burglary', state_crime_data)


# 4. Prediction:

# Utah
utah = predict_category(state_crime_data, 'Utah', 'Data.Population', 2020, 2023)
predict_graph = prediction_model_graph(state_crime_data, 'Utah', 'Data.Population', 2020, 2023)

"""Due to the implemented algorithm being the linear regresssion model, this algorithm can only predict
linear growths, it is unable to make near-accurate predictions when parabolas or unpredicted patterns are involved;
thus it is best used for linearly increasing population growths."""

