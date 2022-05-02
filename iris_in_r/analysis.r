library(hrbrthemes)
library(tidyverse)
library(ggridges)
library(ggthemes)
library(cowplot)
library(viridis)
library(GGally)

# Set the working directory
setwd("D:/ML Projects/iris_in_r/")

iris_data <- read.csv(file = "Iris.csv")
# print(head(iris_data, 5))

print(summary(iris_data))  # Summary of the data


tema <- theme(plot.background = element_rect(fill = "#FFDAB9"),
             plot.title = element_text(size = 25, hjust = .5),
             axis.title.x = element_text(size = 22, color = "black"),
             axis.text.x = element_text(size = 20),
             axis.text.y = element_text(size = 20))

options(repr.plot.width = 14, repr.plot.height = 10)

sepallength <- ggplot(data = iris_data, mapping = aes(x = SepalLengthCm)) +
    geom_histogram(bins = 30, fill = "red",
    color = "black", size = 1.3, alpha = .8) +
    theme_wsj() +
    xlab("Sepal Length") +
    ggtitle("Sepal Length Histogram") +
    tema

sepalwidth <- ggplot(data = iris_data, mapping = aes(x = SepalWidthCm)) +
    geom_histogram(bins = 30, fill = "blue",
    color = "black", size = 1.3, alpha = .8) +
    theme_wsj() +
    xlab("Sepal Width") +
    ggtitle("Sepal Width Histogram") +
    tema

petallength <- ggplot(data = iris_data, mapping = aes(x = PetalLengthCm)) +
    geom_histogram(bins = 30, fill = "cyan",
    color = "black", size = 1.3, alpha = .8) +
    theme_wsj() +
    xlab("Petal Length") +
    ggtitle("Petal Length Histogram") +
    tema

petalwidth <- ggplot(data = iris_data, mapping = aes(x = PetalWidthCm)) +
    geom_histogram(bins = 30, fill = "green",
    color = "black", size = 1.3, alpha = .8) +
    theme_wsj() +
    xlab("Petal Width") +
    ggtitle("Petal Width Histogram") +
    tema

# Graph
plot_grid(sepallength, sepalwidth, petallength, petalwidth, nrow = 2, ncol = 2)