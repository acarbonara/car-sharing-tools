library(ggplot2)
library(ggmap)

args = commandArgs(trailingOnly=TRUE)

if (length(args)==0) {
  stop("At least one argument must be supplied (input file).n", call.=FALSE)
}

## Reading in the data
dataset <- read.table(args[1])
names(dataset) = c('LON','LAT','NUM')
dataset <- dataset[dataset$NUM > 1, ]
df = data.frame(x=dataset$LON, y=dataset$LAT, cluster=dataset$NUM)
#df <- ddply(df, names(df), summarize, N = sum(df$NUM))

### Set a range
lat <- c(min(dataset$LAT),max(dataset$LAT))
lon <- c(min(dataset$LON),max(dataset$LON))

lat
lon

palette <- c("#FFFFD4", "#FED98E", "#FE9929", "#D95F0E", "#993404")
filestring <- gsub(".csv", ".png", args[1])
png(filename = filestring, width = 1024, height = 800, units = 'px')
m <- get_map(location = c(lon=mean(lon), lat=mean(lat)), zoom = "auto", maptype = "terrain", source = "google")
g <- ggmap(m) + scale_x_continuous(limits = lon, expand = c(0,0)) + scale_y_continuous(limits = lat, expand = c(0,0))
g <- g + geom_point(aes(x=x, y=y, color=cluster), data=df) + geom_point(alpha=1.0)
g + scale_color_gradient(low="red",high="yellow") + xlab("Longitude") + ylab("Latitude")

#ggplot(df, aes(df$LON, df$LAT,color=NUM)) + geom_point() +
#        scale_color_gradient(low="yellow",high="red") + xlab("Longitude") + ylab("Latitude")
#ggmap(m) + geom_point(aes(df$LON, df$LAT,color=NUM), data=df) + geom_point(alpha=0.3) + scale_color_gradient(low="blue",high="red") + xlab("Longitude") + ylab("Latitude")
