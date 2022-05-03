# INLS641-Project Final Report
# Data Analytics of COVID-19 in New York City After Omicron Entering the U.S.
## Goals
1. Differences before and after Omicron hits New York City
2. Differences of COVID-19 Data in each region of New York City

Our project goal is to study the Omicron variant's existing COVID-19 data in New York City.   Specifically, we want to learn the differences before and after Omicron hits New York City. For example, what has happened in terms of cases, hospitalizations, and deaths in New York City since Omicron entered the U.S.? Also, we want to discover the differences of COVID-19 data in each region to see the similarities and differences between each area of New York City. 

### User Personas:
Our initial idea is that we want to create this data visualization website for scientists and public users since we think that scientists in public health could use our website to help them collect more data and analyze the COVID-19 data more deeply. We also believe that the public may also be the target users since they would know where it is safer or where they should wear their masks and stay alert to the pandemic. It would also be helpful for international students like me. There are so many international students in the United States, especially in New York City. Our website could change their study plans based on our visual analytics of COVID-19 data.

After we finalized our prototype, we think that our users are not for professionals because we want to use the COVID-19 data in New York City to do a simple data visualization. Instead, our intended users are tourists or international students who are not familiar with New York City and have never been to New York City before. Therefore, this website is perfect for them because it has a simple design and user interactions.

### Analytical Questions
1.What has happened in New York City since Omicron entered the U.S.?
2.What are the differences in cases, hospitalizations, and deaths in New York City after Omicron entered the United States?
3.What are the differences of COVID-19 data in New York City in terms of different zip code areas?

## Data
In this project, we want to use reliable and accurate datasets. Therefore, we choose the COVID-19 Health Data in New York City from NYC Open Data, which includes the daily count of New York City residents who tested positive for SARS-CoV-2, number of hospitalizations, and number of deaths. Our team downloads the dataset directly from the open data of New York and stores the datasets as a CSV file. These datasets need further cleaning to collect relevant data for our project data visualization.

## Intended Visualization Design
Here are the two sketches we made for our website design. As you can see from our illustration, we initially want to have two pages for our website. The first page contains information, including confirmed cases and death cases after the Omicron hits New York City. It also has a New York City map with five regions on the map. We want to make it clickable so that if the users want to interact with the map to see the details of each area, they can click on that region, and there will be more detailed graphs on the second page.

For the second page, we want to have a line chart that includes all the information about COVID-19 data. For example, it should have the number of total cases, number of hospitalizations, and number of deaths. All three data will be on the same chart to show the comparison and relationship among these three attributes. On the left side, there will be a select box with the option to select different months to compare COVID-19 data with other months.

<div align="center"><img src="https://github.com/ChaoYuan99/INLS641-Project/blob/main/Prototype/Initial%20Sketch%20-%20First%20Page.jpg" alt="We can't find this image" width=70%></div>
<p align="center">Figure 1: Initial Sketch - First Page</p>

<div align="center"><img src="https://github.com/ChaoYuan99/INLS641-Project/blob/main/Prototype/Initial%20Sketch%20-%20Second%20Page.jpg" alt="We can't find this image" width=70%></div>
<p align="center">Figure 2: Initial Sketch - Second Page</p>

After our initial sketch, we want to make a sample prototype in Figma to be closer to our final version. We use three web pages to showcase our final project for this sample prototype. On our first page, we use a map that contains New York City with five regions. We labeled each area with a different color to identify the differences. We want to make a side-by-side comparison to have a more precise understanding of before and after Omicron hits New York City. The radius of the circle should also indicate the number of new cases. Although it does not show in our Figma sample prototype, it is our intended design decision. There will also be a mouse hover effect that provides more information, such as total cases, hospitalizations, and deaths when the mouse hovers in this region.

We want to create a heat map for the second page that shows the severity of COVID-19 cases in New York City. The heat map shows where the COVID-19 has the most outbreak since the color will be different. The darker the color, the more cases in that region. The second page gives people a general understanding of the COVID-19 spreading situation in New York City.

For the third page, we want to create charts only to show in-depth detail about COVID-19 in New York City. Therefore, we want to include line charts, scatterplots, and pie charts. Line charts will show the total number of confirmed cases since the COVID-19 outbreak, the total hospitalizations, and the total deaths.

<div align="center"><img src="https://github.com/ChaoYuan99/INLS641-Project/blob/main/Prototype/Figma%20Prototype%20-%20First%20Page.jpg" alt="We can't find this image" width=90%></div>
<p align="center">Figure 3: Figma Prototype - First Page</p>

<div align="center"><img src="https://github.com/ChaoYuan99/INLS641-Project/blob/main/Prototype/Figma%20Prototype%20-%20Second%20Page.jpg" alt="We can't find this image" width=90%></div>
<p align="center">Figure 4: Figma Prototype - Second Page</p>

<div align="center"><img src="https://github.com/ChaoYuan99/INLS641-Project/blob/main/Prototype/Figma%20Prototype%20-%20Third%20Page.jpg" alt="We can't find this image"></div>
<p align="center">Figure 5: Figma Prototype - Third Page</p>

## Data Transformation and Statistical Analysis
Since we collect the data from the NYC COVID-19’s official data website, the dataset is precise enough for us to do our project. All we need to do is calculate a seven-day average of the data. We want to calculate the seven-day average data because there are some errors in the dataset. Therefore, we calculate the seven-day average of new cases to eliminate some mistakes since not many testing sites operate during the weekend, making the confirmed cases data during the weekend lower than the weekly average. Friday and Monday’s data are generally higher than the weekly average. By doing the seven-day average calculation, we have a more accurate dataset.

## Final Design and Implementation
There will be a link at the bottom of the report to get a complete overview of the website. In this part of the report, there will be short explanations for each graph on each page. We will discuss the relationship with each graph in more detail in the discussion section.

In our final design prototype, we will have three pages. The first page contains five graphs. The first three graphs are line charts, and the other two are bar charts. The line charts show confirmed cases, hospitalizations, and deaths in New York City since the pandemic started. The bar charts show the COVID-19 cases by age group and by gender.

<div align="center"><img src="https://github.com/ChaoYuan99/INLS641-Project/blob/main/Final_design/Final%20Prototype%20-%20First%20Page.png" alt="We can't find this image"></div>
<p align="center">Figure 6: Final Prototype - First Page</p>

For the second page, we will stick with our sample prototype. We have a heat map in the second page. The darker the color, the more cases in that region. The heat map is built based on the zip code in our dataset.

<img src="https://github.com/ChaoYuan99/INLS641-Project/blob/main/Final_design/Final%20Prototype%20-%20Second%20Page%20-%20First%20Image.jpg" alt="We can't find this image">
<p align="center">Figure 7: Final Prototype - Second Page - First Image</p>

For the third page, we decide to show more details of COVID-19 data with four more images. Finally, we want to compare the Omicron variant specifically before and after it hits New York City for our last page. Therefore, we have two map-like images corresponding to the situation before and after COVID-19 hits New York City. We also have two pie charts below to show the percent of cases counted by region.

**Before Omicron Hits New York City**
<img src="https://github.com/ChaoYuan99/INLS641-Project/blob/main/Final_design/Final%20Prototype-Third%20Page-First%20Image.png" alt="We can't find this image">
<p align="center">Figure 8: Final Prototype - Third Page - First Image</p>

**After Omicron Hits New York City**
<img src="https://github.com/ChaoYuan99/INLS641-Project/blob/main/Final_design/Final%20Prototype%20-%20Third%20Page%20-%20Second%20Image.png" alt="We can't find this image">
<p align="center">Figure 9: Final Prototype - Third Page - Second Image</p>

**Before Omicron Hits New York City**

<div align="center"><img src="https://github.com/ChaoYuan99/INLS641-Project/blob/main/Final_design/Final%20Prototype%20-%20Third%20Page%20-%20Third%20Image.png" alt="We can't find this image"></div>
<p align="center">Figure 10: Final Prototype - Third Page - Third Image</p>

**After Omicron Hits New York City**

<div align="center"><img src="https://github.com/ChaoYuan99/INLS641-Project/blob/main/Final_design/Final%20Prototype%20-%20Third%20Page%20-%20Fourth%20Image.png" alt="We can't find this image" ></div>
<p align="center">Figure 11: Final Prototype - Third Page - Fourth Image</p>

## Discussion
In our project, each team member contributes the same and has different roles in building up the final project. Jessica develops a schedule to ensure the project’s steady progression throughout the semester. The schedule outlined soft deadlines for the team to complete different project parts. She also writes code using D3 to create two pie charts for page three of the project. The two pie charts produce a before-and-after-Omicron comparison of the proportion of cases in each borough of New York. Jessica also creates two bar charts using Tableau, embedded on page one of the project. Both bar charts convey the number of Omicron cases in New York; however, one bar chart categorizes the cases based on age group while the other shows the cases divided by sex. Lawrence is in charge of all the presentations and visual slides. He is also in charge of designing the Figma mockups and writing the final report. Haoyu mainly focuses on the following things. First of all, as the person who proposes the project, Haoyu revises the proposal and makes it connect with the team’s ideas through discussion with the teammates. At the same time, Haoyu is responsible for organizing each group meeting. Haoyu also proposes and sketches the design for the page he was responsible for in the visualization design. As for writing the code, Haoyu first uses D3.js to construct two line charts, one to reflect the overall New York City’s COVID-19 situation and the other to select any of the five New York City districts through a selection box to explore the differences in each area. However, in the later communication with the team members, our team finds that the graphs made in Python might contain more information and be more user-friendly, so Chao and Haoyu use Python to make the line chart part of the project. Chao creates a three-page website with all the images and charts we create based on our data of COVID-19. He also uses D3.js and Python to make the rest of the data visualization embedded into our website.

For our first page, we want to show our audience the COVID-19 situation, which means the time is from the initial outbreak to now. Therefore, we create three charts that count new cases, hospitalizations, and deaths. We also create two bar charts indicating the age distribution and sex in which people test positive for COVID-19. Our team wants people to have a general understanding of the whole COVID-19 situation till now.

For our second page, we want to show the overall distribution based on the zip code in the dataset. This is an overview of the map so that the people who visit our website can see more details on the following page. 

We mainly focused on the differences before and after Omicron hits New York City for the third page. For the first two visualizations, we want to show the differences in COVID-19 confirmed cases in each area before and after COVID-19 hits New York City. The radius indicates the number of cases. As the image shows, the radius of the circle in each region of New York City increases, which means there are more confirmed cases after Omicron hits New York City. After this side-by-side comparison, we also include two pie charts with different regions in New York City in different colors to show the differences, specifically changes that happened in each area of New York City during the Omicron period. 

All in all, I think our group project is a great implementation and a sample website for people who need information about the COVID-19 situation in New York City. These people could be international students, tourists from foreign countries, or travelers from different states who want to know more about COVID-19 and the Omicron variant in New York City. Our website is an excellent implementation for these people.

## Ethical and Societal Considerations
There are still many things to consider, especially from an ethical and societal standpoint. Ethically, I think it is beneficial for the people who want to travel to New York City to visit our website based on the current COVID-19 situation around the world. However, we did collect data from the NYC official website, so I think the data is reliable enough for us to do the research.

From a societal standpoint, I think this project is suitable for people new to the country and minorities who have not come to New York City before. Therefore, I think it is great for society because it helps people know the COVID-19 situation better through our website. Of course, it is a small contribution to society, but we believe these people will better learn about the COVID-19 situation in New York City. 
