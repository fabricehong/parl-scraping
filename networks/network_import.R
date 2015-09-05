rm(list=ls())

library(lubridate)
library(igraph)

# working directory is "parl_scraping/networks"

arcs <- read.csv("graph-full/graph.csv", sep="&", header = FALSE, stringsAsFactors = FALSE)
colnames(arcs) <- c("source", "target", "object", "date")

# sources and targets

# objects
arcs$object <- as.factor(arcs$object)

# dates
dates <- ymd(arcs$date)
arcs$date <- as.character(ymd(arcs$date))

# vertices
vertices <- read.csv("graph-full/nodes.csv", sep="&", header=FALSE, stringsAsFactors = FALSE)
colnames(vertices) <- c("id", "surname", "name", "canton", "polgroup")

# create graph
g.all <- graph.data.frame(arcs, vertices=vertices)
g <- g.all
E(g)$weight <- 1
g <- simplify(g)
E(g)$weight

table(E(g)$weight)

# plot(degree(g, mode = "in"), degree(g, mode = "out"))

V(g)$color <- "white"
V(g)$label <- NA
V(g)$size <- 2
E(g)$width <- E(g)$weight

pdf("network_dialogues.pdf")
par(mar=c(0,0,0,0))
plot(g)
dev.off()