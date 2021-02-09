df <- read.csv("./labeledTrainData.tsv",sep="\t",quote="")
data <- df.small[1:1000,c("sentiment","review")]
mylogit <- glm(sentiment ~ review, data = data, family = binomial(link="logit"))

