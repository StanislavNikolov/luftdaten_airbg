# Findings
Many people speculate old cars are the reason for the bad air quality in Sofia. I found no evidance of that claim, on the contrary - cars seem to have no effect at all.  
![Average PM2.5 concentration in Sofia](/assets/Figure_1_closeup.png?raw=true)  
As you can see, the least poluted times are around 12:00-13:00, with a pretty constant "dirty" part repeating every day through the night. This suggest that heating is a bigger polutant.  

![Average PM2.5 concentration in Sofia](/assets/Figure_2.png?raw=true)  
On this map you can see the locations for stations that most frequently report themselves as top 3 most poluted in Sofia - the area of the circle proportional to the number of times this happened. Again, areas around the center are the cleanest, although there are some of the busyest in the city.  
Take a look at `assets/`, there's some interactive graphs to play around.

# Where I gathered data from
Long story short: some guys found that building your own weather stations is quite cheap. Told the world and made an open api through which everybody can send data from their own home-owned stations. Got popular. See more at:
 * https://luftdaten.info/en/home-en/
 * http://archive.luftdaten.info/

# If you want to do it yourself (not for for the faint-hearted)

```
# all scripts expect you are in the root of this repo
./scripts/download/main.sh
./scripts/analyze/main.sh
```

Beware, datasets are around 500MB per day, by default last 30 days are downloaded. Tune `head -n xxx` in download/main.js to change that.  
Analysis typically takes a few minutes as well, be patients; Look at the last line of analyze/main.js for a bit quicker method (random sampling of data instead of all).  
Look at `analyzeFromFileList.py` for different modes, there are 'local' averages and worst station reports to csv, plotting with matplotlib.
