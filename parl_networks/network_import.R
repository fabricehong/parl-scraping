rm(list=ls())

library(lubridate)
library(igraph)

# working directory is "parl_scraping/parl_networks"

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

# create graph with multiple arcs
g.all <- graph.data.frame(arcs, vertices=vertices)

# create simplified graph
g <- g.all
E(g)$weight <- 1
g <- simplify(g)

# create graphs of each sessions (will reduce the number of nodes and allow comparisons)

ef1995 <- new_interval(ymd("1996-01-01"), ymd("1999-12-31"))
ef1999 <- new_interval(ymd("2000-01-01"), ymd("2003-12-31"))
ef2003 <- new_interval(ymd("2004-01-01"), ymd("2007-12-31"))
ef2007 <- new_interval(ymd("2008-01-01"), ymd("2011-12-31"))
ef2011 <- new_interval(ymd("2012-01-01"), ymd("2015-12-31"))

int <- c(ef1995, ef1999, ef2003, ef2007, ef2011)

g1995 <- subgraph.edges(g.all, eids=E(g.all)[ymd(E(g.all)$date) %within% ef1995])
g1999 <- subgraph.edges(g.all, eids=E(g.all)[ymd(E(g.all)$date) %within% ef1999])
g2003 <- subgraph.edges(g.all, eids=E(g.all)[ymd(E(g.all)$date) %within% ef2003])
g2007 <- subgraph.edges(g.all, eids=E(g.all)[ymd(E(g.all)$date) %within% ef2007])
g2011 <- subgraph.edges(g.all, eids=E(g.all)[ymd(E(g.all)$date) %within% ef2011])

# save network
# g.all is the network with multiple arcs
save(g, g.all, file="graph-full/networks-all.Rdata")
save(g1995, g1999, g2003, g2007, g2011, file="graph-full/networks-sessions.Rdata")
