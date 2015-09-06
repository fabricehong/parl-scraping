######
## Subject: Uncover semantic similarity between members of the Swiss Parliament [experimental]
## Context: Started during the Election Hackdays at Le Temps in Switzerland (http://make.opendata.ch/wiki/event:2015-09)
##
## TODO:
## - execute on the whole dataset (language detection take a lot of time...)
## - improve preprocessing (tokenization, stopwords removing, stemming)
## - plot in Tableau with the other dimensions
## - validate by a human
## - integrate parties
## - handle German and Italian
##
## Author: Pierre-Alexandre Fonta (@pa_fonta)
######

install.packages("textcat")
install.packages("tm")
install.packages("SnowballC")

library(textcat)
library(tm)
library(SnowballC)

###

setwd("./parl-scraping")

unzip("./data/items-full-final-with-bio.csv.zip")
df.raw <- read.csv(file="items-full-final-with-bio.csv", na.strings=c(""), stringsAsFactors=F)
df.raw <- df.raw[1:5000,] # FIXME

df.raw$lang <- textcat(df.raw$data)
df <- df.raw[df.raw$lang == "french",]

df.agg.people <- aggregate(
  data ~ party + city + workLanguage + birthDate + maritalStatus + name + surname + cantonName + gender + numberOfChildren, 
  data=df, 
  FUN=paste,
  collapse=' '
)
df.agg.people$id <- paste(df.agg.people$name, df.agg.people$surname)

# df.agg.parties <- aggregate(
#   data ~ party, 
#   data=df, 
#   FUN=paste,
#   collapse=' '
# )
# names(df.agg.parties)[names(df.agg.parties) == "party"] <- "id"

# df.agg.text <- rbind(df.agg.people[,c("id", "data")], df.agg.parties[,c("id", "data")])
df.agg.text <- df.agg.people # FIXME

###

stopifnot(sum(is.na(df.agg.text$data)) == 0)

docs <- df.agg.text$data
n.docs <- length(docs)

nrow(df.raw)
nrow(df)
nrow(df.agg.people)
# nrow(df.agg.parties)
n.docs

vs <- VectorSource(docs)
vs$Names <- df.agg.text$id
corpus <- Corpus(vs)

tokenizer <- function(x)
  unlist(strsplit(as.character(x), "[[:space:]]+|'"))
stemmer <- function(x)
  stemDocument(x, language="french")
ctrl <- list(
  tokenize=tokenizer,
  tolower=T,
  removePunctuation=list(preserve_intra_word_dashes=T),
  removeNumbers=T,
  stopwords=stopwords("french"),
  stemming=stemmer)
dtm <- DocumentTermMatrix(
  corpus,
  control=unlist(c(
    ctrl,
    weighting=function(x) weightTfIdf(x))))

dtm # FIXME Excessive term length
dtm.df <- as.data.frame(as.matrix(dtm))
dtm.df <- dtm.df[,colSums(dtm.df) != 0]

dtm.light <- removeSparseTerms(dtm, 0.2)
dtm.light
dtm.light.df <- as.data.frame(as.matrix(dtm.light))

###

pca <- prcomp(dtm.df, scale=T)
summary(pca) # FIXME Too low explained variance
plot(pca)

plot(pca$x[,c(1,2)], pch=20, main="Semantic similarity between members of the Swiss Parliament")
text(pca$x[,c(1,2)], vs$Names , cex=0.7, pos=4, col="blue")
# FIXME xlim and zooming


