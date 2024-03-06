# install.packages("dplyr")
library(dplyr)
mydata <- read.csv("https://raw.githubusercontent.com/deepanshu88/data/master/sampledata.csv")

print(sample_n(mydata, 3))

# random sample of data
print(sample_frac(mydata,0.1))

# Remove Duplicate Rows
x1 <- distinct(mydata)
print(x1)

# Remove Duplicate Rows based column
x2 <- distinct(mydata, Index, .keep_all= TRUE)
print(x2)

# Selecting Columns
mydata2 <- select(mydata, Index, State:Y2008)
print(mydata2)

# dropping columns
x3 <-  select(mydata, -c(Index,State))
print(x3)

# selecting columns
x4 <- select(mydata, starts_with("Y"))
print(x4)

mydata2 <- select(mydata, contains("I"))
print(mydata2)

# ordering columns
mydata3 <- select(mydata, State, everything())
print(mydata3)

# renaming the column
mydata4 <- rename(mydata, Index_New=Index)
print(mydata4)

# Filter Rows
mydata5 <- filter(mydata, Index == "A")
print(mydata5)

# Multiple filter condition
mydata6 <- filter(mydata, Index %in% c("A", "C"))
print(mydata6)

# conditional filtering
mydata7 <- filter(mydata, Index %in% c("A", "C") & Y2002 >= 1300000 )
mydata8 <- filter(mydata, Index %in% c("A", "C") | Y2002 >= 1300000)
mydata9 <- filter(mydata, !Index %in% c("A", "C"))
print(mydata7)
print(mydata8)
print(mydata9)

# contains columns
mydata10 <- filter(mydata, grepl("Ar", State))
print(mydata10)

# Summarize selected variables
print(summarise(mydata, Y2015_mean <- mean(Y2015), Y2015_med=median(Y2015)))
print(summarise_at(mydata, vars(Y2005, Y2006), funs(n(), mean, median)))

# multiple condition
dt <- mydata %>% select(Index, State) %>% sample_n(10)
print(dt)

# group by
group <- mydata %>% group_by('Index')
print(group)




