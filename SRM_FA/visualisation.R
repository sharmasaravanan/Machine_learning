library(ggplot2)
install.packages(ggplot2)

n <-c(1,1,1,2,2,3,3,3,4,4,4,4)
p <- hist(n,breaks = 10)
print(p)

data(VADeaths)
VADeaths

par(mfrow = c(2,3))
library("RColorBrewer")
hist(VADeaths,breaks = 10,main = "Death rate",col = brewer.pal(8,"Greys"))
hist(VADeaths,breaks = 7,main = "Death rate")
hist(VADeaths,breaks = 3,main = "Death rate",col=brewer.pal(3,"Set3"))
hist(VADeaths,breaks = 7,main = "Death rate")
hist(VADeaths,breaks = 10,main = "Death rate")
hist(VADeaths,breaks = 7,main = "Death rate")
hist(VADeaths,breaks = 17,main = "Death rate")
hist(VADeaths,breaks = 5,main = "Death rate")


barplot(VADeaths, plot = TRUE, beside = TRUE)

mp <- barplot(VADeaths)
tot <- colMeans(VADeaths)
text(mp, tot+3, format(tot),col  = "blue")


barplot(VADeaths, beside = TRUE,
        col = c("lightblue", "mistyrose", "lightcyan",
                           "lavender", "cornsilk"),
                           legend = rownames(VADeaths), ylim = c(0, 80))
title(main = "Death Rates in Virginia", font.main = 4)



pie.sales <- c(0.12, 0.3, 0.26, 0.16, 0.04, 0.12)
names(pie.sales) <- c("Blueberry", "Cherry",
                      "Apple", "Boston Cream", "Other", "Vanilla Cream")

pie(pie.sales) # default colours

pie(pie.sales, col = c("purple", "violetred1", "green3",
                               "cornsilk", "cyan", "white"))
pie(pie.sales, col = gray(seq(0.4, 1.0, length = 6)))

pie(pie.sales, density = 10, angle = 15 + 10 * 1:6)

pie(pie.sales, clockwise = TRUE, main = "pie(*, clockwise = TRUE)")

segments(0, 0, 0, 1, col = "red", lwd = 2)
text(0, 1, "init.angle = 90", col = "red")
                               
                               
data(iris)
plot(iris,col = brewer.pal(3,"Set1"),pch=16)

boxplot(iris$Sepal.Length,col = "blue")


# Creating a histogram
p <- ggplot(data  = iris, aes( x = Sepal.Length)) + geom_histogram( )
print(p)

p <- ggplot(data = iris , aes(x=Sepal.Length)) + 
  geom_histogram(color="black", fill="white", bins = 10) 
print(p)

# creating density
p <- ggplot(iris, aes(x=Sepal.Length, color=Species)) + geom_density( )
print(p)

p <- ggplot(mpg, aes(x= class)) + geom_bar() + 
  labs(title = "Number of Cars in each type", x = "Type of car", y = "Number of cars")
print(p)
 
# print(p + geom_text(stat='count', aes(label=..count..), vjust=-0.25))

