rm(list=ls())

library(lubridate)
library(igraph)

# working directory is "parl_scraping/networks"

load("graph-full/networks.Rdata")

# E(g)$weight



# ranks of edges/dialogues
table(E(g)$weight)


# regexpr(V(g)$id)



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