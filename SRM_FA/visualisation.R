library(ggplot2)

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

