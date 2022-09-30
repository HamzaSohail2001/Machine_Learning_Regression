import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('Data_Study.csv')
# print(data)
# plt.scatter(data.studytime, data.grade)
# plt.show()


def cost_function(m, b, p):
    error = 0
    for i in range(len(p)):
        x = data.iloc[i].studytime
        y = data.iloc[i].grade
        error += (y - (m * x + b)) ** 2
    error = error / len(p)


def gradient_decent(m,b,p,l):

    m_dx = 0
    b_dx = 0
    lenght = len(p)
    for i in range(lenght):
        x = data.iloc[i].studytime
        y = data.iloc[i].grade
        y_predicted = m * x + b
        m_dx = -(2/lenght) * x * (y-y_predicted)
        b_dx = -(2 /lenght) * (y - y_predicted)
    m_total = m - m_dx * l
    b_total = b - b_dx * l
    return m_total, b_total


m=0
b=0
l=0.0001
iterations =1000
for i in range(iterations):
    m,b = gradient_decent(m,b,data,l)

print(m)
print(b)
plt.scatter(data.studytime, data.grade)
plt.plot(list(range(1,13)),[m*x+b for x in range(1,13)],color="red")
plt.show()
