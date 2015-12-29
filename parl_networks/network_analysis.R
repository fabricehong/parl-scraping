rm(list=ls())

library(lubridate)
library(igraph)

# working directory is "parl_scraping/parl_networks"

load("graph-full/networks-all.Rdata")
load("graph-full/networks-sessions.Rdata")

###############################
### Réseaux toutes sessions ###
###############################

# ranks of edges/dialogues
table(E(g)$weight)

# plotting
g$layout <- layout_with_kk(g)

V(g)$color <- rainbow(length(levels(factor(V(g)$polgroup))))[factor(V(g)$polgroup)]
V(g)$label <- paste(V(g)$surname, V(g)$name, sep=" ")
V(g)$size <- 2

E(g)$color <- "gray"
E(g)[which(E(g)$weight == 1)]$color <- NA
E(g)$width <- sqrt(E(g)$weight)
E(g)$arrow.size <- .1

pdf("network_dialogues.pdf", width = 50, height = 50)
par(mar=c(0,0,0,0))
plot(g)
dev.off()

############################
### Réseaux par sessions ###
############################

g.sessions <- list(g1995, g1999, g2003, g2007, g2011)
g.sessions.simplified <- g.sessions

for (i in 1:length(g.sessions)) {
	E(g.sessions[[i]])$weight <- 1
	g.sessions[[i]] <- simplify(g.sessions[[i]])
}

for (i in 1:length(g.sessions)) {
	print(table(E(g.sessions[[i]])$weight))
}

# plotting
plot.graph <- function(g) {
	g$layout <- layout_with_kk(g)

	V(g)$color <- rainbow(length(levels(factor(V(g)$polgroup))))[factor(V(g)$polgroup)]
	V(g)$label <- paste(V(g)$surname, V(g)$name, sep = " ")
	V(g)$size <- log(degree(g, mode = "all"))
	V(g)$label.cex <- log(degree(g, mode = "all"))

	E(g)$color <- "gray"
	E(g)$width <- sqrt(E(g)$weight)
	E(g)$arrow.size <- 2
	E(g)$curved <- TRUE

	plot(g)
	legend(-1, -0.3, legend=levels(factor(V(g)$polgroup)), pch = 19, col=V(g)$color, cex = 10)
}

pdf("test.pdf", width = 100, height = 100)
par(mar=c(0,0,0,0))
plot.graph(g.sessions[[1]])
dev.off()