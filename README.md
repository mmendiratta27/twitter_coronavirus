# Coronavirus Twitter Analysis

In this project, I scanned all geotagged tweets sent in 2020 to learn more about the usage of various health related hashtags. This meant parsing through approximately 3.6 billion geotagged tweets to visualize yearlong trends. To manage this dataset, I used MapReduce to create parallel code and optimize run time.

## Mapping the Data

I created a shell script, `run_maps.sh`, to run each day of tweets separately using `nohup` and `&`. The command to run this shell script effectively is: 
```
nohup bash run_maps.sh
```
This utilizes the `map.py` file to process the zip file of an individual day and track language and country attributes of a desired set of hashtags. For this project, I focused on health related hashtags. These hashtags can be found and modified in `map.py`, and the results of `map.py` are stored in the `outputs` folder. 

## Reduce

The `reduce.py` file merges the output files of map.py by the file extension. In essence, this combines each day's worth of data to create a dataset representative of the year, which allowed me to then create visualizations. I used the follow commands to reduce the files:
```
$ python3 ./src/reduce.py --input_paths outputs/geoTwitter*.lang --output_path=reduced.lang
$ python3 ./src/reduce.py --input_paths outputs/geoTwitter*.country --output_path=reduced.country
```
These commands create two files, `reduced.lang` and `reduced.country`, that can then be used for visualizations. 

## Visualization

The `visualize.py` file has two inputs that take multiple arguments, `--input_path` and `--key`. It then generates a barplot of the top 10 languages or countries (based on `--input_path`) that used the hashtags entered in `--key`. The results are stored in png files. I created 4 graphs with the command
```
$ python3 ./src/visualize.py --input_path 'reduced.lang' 'reduced.country' --key '#coronavirus' '#코로나바이러스'.
```
## Top 10 Languages That Used #coronavirus in 2020

<img src=coronavirus_lang.png width=100% />

## Top 10 Countries That Used #coronavirus in 2020

<img src=coronavirus_country.png width=100% />

## Top 10 Languages That Used #코로나바이러스 in 2020

<img src=코로나바이러스_lang.png width=100% />

## Top 10 Countries That Used #코로나바이러스 in 2020

<img src=코로나바이러스_country.png width=100% />

## Alternative Reduce

Another method I explored was using one file, `alternative_reduce.py` to reduce and visualize the data in a line plot. This can take multiple hashtags as input via the command prompt `--keys` and plot the usage of each tweet globally throughout the year. One example of this is displayed below with the command:

```
$ python3 ./src/alternative_reduce.py --keys '#flu' '#sick'
```

## Usage of #flu and #sick in 2020

<img src=flu_sick.png width=100% />

## Conclusion

In this project, I used MapReduce to parse through and visualize an extremely large, professional dataset. This utilized parallel computing techniques, data processing, and matplotlib visualizations. 
