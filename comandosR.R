library(readr)
crawlerData <- read_csv("valoresCaptados.csv")

ggplot(data = crawlerData, aes( y = ramPercent)) +
  geom_bar()

ggplot(data = crawlerData, aes(x = dataHora, y = cpuPercent)) +
  geom_line()

ggplot(data = crawlerData, aes(x = dataHora, y = ramPercent)) +
  geom_line()

plot(crawlerData$ramPercent~crawlerData$cpuPercent)
abline(4.08181, 0.02668)

#model <- lm(crawlerData$ramPercent~crawlerData$cpuPercent)
#model


ggplot(mapping = aes(crawlerData$cpuPercent, crawlerData$ramPercent)) +
  geom_point() +
  geom_smooth(method = "lm")

predict(lm(crawlerData$ramPercent~crawlerData$cpuPercent))

summary(lm(crawlerData$ramPercent~crawlerData$cpuPercent))

#BAR PLOT TEMPxRAM
ggplot(crawlerData, aes(x = ramPercent, y = cpuPercent)) +
  geom_bar(stat = "identity")

#GRAFICO DE PIZZA
ggplot(crawlerData, aes(x = factor(1), fill = factor(ramPercent))) +
  geom_bar() +
  coord_polar(theta = "y")

#GRAFICO DE REGRESSAO LINEAR
ggplot(crawlerData, aes(x = cpuPercent, y = ramPercent)) +
  geom_point() +
  geom_smooth(method = "lm", se = FALSE) +
  labs(x = "Temperatura", y = "Uso de RAM")

#MATRIZ DE CORRELAÇÃO
testeCDN <- read.csv("testeCDN.csv")

install.packages("corrplot")

library(corrplot)

m<-cor(testeCDN[3:12])
corrplot(m, method = "color",
         + type="upper",
         + addCoef.col = "black", insig = "blank", diag=FALSE)
