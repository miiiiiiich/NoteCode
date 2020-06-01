# Title     : TODO
# Objective : TODO
# Created by: Michisato
# Created on: 2020/05/30
library(tidyverse)
competence <- 0:96
confidence <- NULL
for (i in competence) {
  confidence <- c(confidence,
                  if_else(i <= 10, true = i * 8.4, false = 1 / 28 * (i - 51)^2 + 20))
}
g <- ggplot(data = NULL, aes(x = competence, y = confidence)) +
  geom_line(color = "red", size = 2, alphl = 0.4) +
  geom_hline(yintercept = 0, size = 1) +
  geom_vline(xintercept = 0, size = 1) +
  ggtitle("Dunning-Kruger Effect") +
  theme(plot.title = element_text(hjust = 0.5, size = 30)) +
  annotate("text", x = 10, y = 88, label = "Begginer", size = 5) +
  annotate("text", x = 96, y = 80, label = "Expert", size = 5)
g
