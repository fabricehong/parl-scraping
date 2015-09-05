rm(list=ls())

library(httr)

# Querying the parlament web services
# WATCH OUT! You have to identify as a… browser 
# ¯\_(ツ)_/¯

# XML retrieval

for (i in 1:10000) {		# upper bound is deliberately very high
	url <- paste0("http://ws.parlament.ch/councillors/", i, "?format=xml", collapse="")
	if (GET(url)$status_code == 200) {			# Some IDs aren't used, we escape them
		destfile <- paste0("bio_xml/", i, ".xml", collapse="")
		cat(content(GET(url, user_agent("Mozilla/4.0")), "text", encoding = "UTF-8"), file=destfile)
	}
}

# JSON retrieval

for (i in 1:10000) {		# upper bound is deliberately very high
	url <- paste0("http://ws.parlament.ch/councillors/", i, "?format=json", collapse="")
	if (GET(url)$status_code == 200) {			# Some IDs aren't used, we escape them
		destfile <- paste0("bio_json/", i, ".json", collapse="")
		cat(content(GET(url, user_agent("Mozilla/4.0")), "text", encoding = "UTF-8"), file=destfile)
	}
}

