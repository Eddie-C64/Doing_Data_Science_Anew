setwd('/Users/lalo/CodingComplication/DataScienceProjects/Doing_Data_Science_Anew/Regression Fun/')

x_1 <- rnorm(1000, 5, 7)
hist(x_1, col='grey')
true_error <- rnorm(1000, 0, 2)
true_beta_0 <- 1.1
true_beta_1 <- -8.2
y <- true_beta_0 + true_beta_1*x_1 + true_error

hist(y)
plot(x_1, y, pch=20,col="red")

x_2 <- rnorm(10000, 5, 7)
hist(x_1, col='grey')
true_error <- rbinom(10000, 0, 2)
true_beta_0 <- 1.1
true_beta_1 <- -8.2
true_beta_2 <- 5.0
y1 <- true_beta_0 + true_beta_1*x_1 + true_beta_2*x_2 + true_error

hist(1)
plot(x_1, y, pch=20,col="red")