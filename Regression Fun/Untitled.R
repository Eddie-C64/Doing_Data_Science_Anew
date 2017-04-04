setwd('/Users/lalo/CodingComplication/DataScienceProjects/Doing_Data_Science_Anew/Regression Fun/')

require(rjson)
require(plyr)

dataPath <- "http://getglue-data.s3.amazonaws.com/getglue_sample.tar.gz"

temp_file = download.file(dataPath, 'getglue_sample.tar.gz')

theCon <- untar('tempePack.tar.gz')

n.rows <- 10
theLines <- readLines(theCon, n=n.rows)
str(theLines)

theLines[1]

theRead <- lapply(theLines[-1], fromJSON)

theData <- ldply(theRead, as.data.frame)

View(theData)
