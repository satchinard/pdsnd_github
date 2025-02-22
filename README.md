### Date created
6th october 2019.

### Project Title
Bike Share Data

### Description

Over the past decade, bicycle-sharing systems have been growing in number and popularity in cities across the world. Bicycle-sharing systems allow users to rent bicycles on a very short-term basis for a price. This allows people to borrow a bike from point A and return it at point B, though they can also return it to the same location if they'd like to just go for a ride. Regardless, each bike can serve several users per day.

Thanks to the rise in information technologies, it is easy for a user of the system to access a dock within the system to unlock or return bicycles. These technologies also provide a wealth of data that can be used to explore how these bike-sharing systems are used.

In this project, you will use data provided by [Motivate](https://www.motivateco.com/), a bike share system provider for many major cities in the United States, to uncover bike share usage patterns. You will compare the system usage between three large cities: Chicago, New York City, and Washington, DC.

#### The Datasets

Randomly selected data files contain the same core six (6) columns:

Column title | Data example
-------------|--------------
Start Time | 2017-01-01 00:07:57
End Time | 2017-01-01 00:20:53
Trip Duration | in seconds - e.g., 776
Start Station | Broadway & Barry Ave
End Station | Sedgwick St & North Ave
User Type | Subscriber or Customer

Some cities files also have the following two columns:

**Gender** and **Birth Year**

##### Statistics Computed

You will learn about bike share use in cities by computing a variety of descriptive statistics. This project will provide the following information:

* 1 Popular times of travel (i.e., occurs most often in the start time)**

 - most common month
 - most common day of week
 - most common hour of day


* 2 Popular stations and trip

 - most common start station
 - most common end station
 - most common trip from start to end (i.e., most frequent combination of start station and end station)


* 3 Trip duration

 - total travel time
 - average travel time


* 4 User info

 - counts of each user type
 - counts of each gender (only available for NYC and Chicago)
 - earliest, most recent, most common year of birth (only available for NYC and Chicago)

### Files used
bikeshare.py contains the Python code.

You will need the three city dataset files too:
 - chicago.csv
 - new_york_city.csv
 - washington.csv

### Credits
Feel free to update the code to fit your objectives.
