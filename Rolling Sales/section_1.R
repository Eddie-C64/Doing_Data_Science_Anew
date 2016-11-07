# Author: Eduardo Carrasco Jr.
cat("/014")
nyt_file1 = read.csv(file.choose())
nyt_file1

# Summary
head(nyt_file1)
summary(nyt_file1)

# Categorize the age groups
nyt_file1$agecat <-cut(nyt_file1$Age,c(-Inf,0,18,24,34,44,54,64,Inf))

# Set the brackets
install.packages("doBy")
library("doBy")
siterange <- function(x){c(length(x), min(x), mean(x), max(x))} summaryBy(Age~agecat, data =nyt_file1, FUN=siterange)

# so only signed in users have ages and genders
summaryBy(Gender+Signed_In+Impressions+Clicks~agecat,
          data =nyt_file1)
# plot
install.packages("ggplot2")
library(ggplot2)
ggplot(nyt_file1, aes(x=Impressions, fill=agecat))+geom_histogram(binwidth=1)
ggplot(nyt_file1, aes(x=agecat, y=Impressions, fill=agecat))+geom_boxplot()

nyt_file1$hasimps <-cut(nyt_file1$Impressions,c(-Inf,0,Inf))

summaryBy(Clicks~hasimps, data =nyt_file1, FUN=siterange) ggplot(subset(nyt_file1, Impressions>0), aes(x=Clicks/Impressions,
                                                                                               colour=agecat)) + geom_density()

# create categories
nyt_file1$scode[nyt_file1$Impressions==0] <- "NoImps"
nyt_file1$scode[nyt_file1$Impressions >0] <- "Imps"
nyt_file1$scode[nyt_file1$Clicks >0] <- "Clicks"
# Convert the column to a factor
nyt_file1$scode <- factor(nyt_file1$scode)
head(nyt_file1)
#look at levels
clen <- function(x){c(length(x))} etable<-summaryBy(Impressions~scode+Gender+agecat,data = nyt_file1, FUN=clen)

