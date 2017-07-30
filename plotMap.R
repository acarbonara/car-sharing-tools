library(ggmap)
library("ggplot2")
library(plyr)

dataset = read.table('heatmap-900-5000-00-23.csv')

names(dataset)=c('x','y','color')
dftotal = data.frame(x=dataset$x,y=dataset$y, col=dataset$color)

### Set a range
lat <- c(min(dataset$y),max(dataset$y))                
lon <- c(min(dataset$x),max(dataset$x)) 

lat
lon

palette <- c("#000000","#000099")
palette <- c(palette, "#990099","#BB0099")
palette <- c(palette, "#EE0099","#FF00AA")
palette <- c(palette, "#FF00FF","#FF77FF")
palette <- c(palette, "#77AA77","#33FF33")
palette <- c(palette, "#00FF00","#00FF00")
palette <- c(palette, "#00FF00","#00FF00")
palette <- c(palette, "#00FF00","#00FF00")
palette <- c(palette, "#00FF00","#00FF00")
palette <- c(palette, "#00FF00","#00FF00")
palette <- c(palette, "#00FF00","#00FF00")
palette <- c(palette, "#00FF00","#00FF00")
palette <- c(palette, "#00FF00","#00FF00")
palette <- c(palette, "#00FF00","#00FF00")
palette <- c(palette, "#00FF00","#00FF00")
palette <- c(palette, "#00FF00","#00FF00")
palette <- c(palette, "#00FF00","#00FF00")
palette <- c(palette, "#00FF00","#00FF00")
palette <- c(palette, "#00FF00","#00FF00")
palette <- c(palette, "#00FF00","#00FF00")
bb <- c(0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40)
bb <- c(0,1,2,3,4,5,6,7,8,9)


### Get a map
map <- get_map(location = c(lon = mean(lon), lat = mean(lat)), zoom = 13, maptype = "roadmap", source = "google")
#map <- get_map(location = c(min(lon), min(lat), max(lon), max(lat)), source = "osm")

### When you draw a figure, you limit lon and lat.      
ggmap(map)

pdf(paste("map.pdf", sep=""))

#ggmap(map) +
#	scale_x_continuous(limits = lon, expand = c(0,0)) +
 # 	scale_y_continuous(limits = lat, expand = c(0,0)) +
  #  geom_polygon(data=dftotal, aes(x=x, y=y, group=factor(col), fill=factor(col), colour=NA, alpha=0.5)) +
	#scale_fill_gradientn(colours=rev(brewer.pal(9,"RdYlGn")), labels=percent) +
#	scale_fill_gradientn(colours=palette, labels=factor(col)) +
#	labs(fill="") +
#	theme_nothing(legend=TRUE)

ggplot(dftotal, aes(x=x, y=y, colour=factor(col), fill=factor(col))) +
  	geom_tile(aes(alpha=0.5)) +
 	scale_x_continuous(limits = lon, expand = c(0,0)) +
  	scale_y_continuous(limits = lat, expand = c(0,0)) +
#  	scale_fill_manual(values=palette,breaks = bb, labels=c("0","1","2","3","4","5","6","7","8","9 or more")) +
  	#scale_colour_manual(values=palette,breaks = bb) +
#  scale_x_continuous(limits = c(11.33, 11.36), expand = c(0, 0)) +
#  scale_y_continuous(limits = c(44.49, 44.5), expand = c(0, 0)) +
#  scale_x_continuous(expand = c(0,0), limits=c(40,110)) +
#  scale_y_continuous(expand = c(0,0), limits=c(10,80)) +
  	theme(axis.text.y = element_blank()) +
  	theme(axis.text.x = element_blank()) +
  	theme(axis.title.y = element_blank()) +
  	theme(axis.title.x = element_blank()) +
  	theme(axis.ticks.y = element_blank()) +
  	theme(axis.ticks.x = element_blank()) +
  	guides(color=FALSE) +
  	guides(alpha=FALSE) +
  	guides(fill=FALSE)
#  theme(panel.grid.major = element_blank(), panel.grid.major = element_blank()) +
#  scale_colour_manual(values=c('#000000','#FF0000')) +
#  theme(legend.position = "bottom") +
#  theme(legend.title = element_blank()) 

dev.off()
