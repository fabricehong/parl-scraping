rm(list=ls())

# working directory is "parl_scraping"

library(jsonlite)
wd <- getwd()
setwd("../biography_retrieval/bio_json/")

lf <- list.files()

df <- data.frame()

# Ici les quelques rubriques qui nous intéressent
# Il devra y en avoir plus, mais ça n'est pas évident, il y a 
# par exemple des gens qui ont quitté un conseil et y sont revenus, 
# ou ont changé de conseil. Il faudra prendre ça en compte avec
# autre chose qu'un data frame

coln <- c("id", "cantonName", "council", "firstName", "lastName", "party", "active", "birthDate", "gender", "language", "maritalStatus", "militaryGrade", "partyId", "salutationLetter", "workLanguage")

for (i in 1:length(lf)) {
	a <- fromJSON(lf[i])
	temp <- as.vector(a[coln])
	names(temp) <- coln	
	temp[sapply(temp, is.null)] <- NA
	temp <- as.data.frame(temp)
	df <- rbind(df, temp)
}

setwd(wd)

write.csv(df, "alldelegates.csv")