
import numpy as np
import matplotlib.pyplot as plt
np.random.seed(42)
data=np.random.randint(50,200,size=30)
days=np.arange(1,31)

#Function for display a histogram

def show_histogram():
  plt.hist(data,bins=10,color="blue",edgecolor="black",alpha=0.7)
  plt.xlabel('Profile Views')
  plt.ylabel('Frequency')
  plt.title('Histogram of Profile Views')
  plt.grid(True)
  plt.show()

#Function to display a bar chart

def show_bar_chart():
  plt.bar(days,data,color="green",alpha=0.7)
  plt.xlabel('Days')
  plt.ylabel('Profile views')
  plt.title('Bar chart of profile views')
  plt.grid(axis='y')
  plt.show()

#Function to display a pie chart

def show_pie_chart():
  views_split=np.array([sum(data[:10]),sum(data[10:20]),sum(data[20:])])
  labels=['First 10 days','Middle 10 days','Last 10 days']
  plt.pie(views_split,labels=labels,autopct='%1.1f%%',colors=['red','blue','green'])
  plt.title('Pie chart of profile views (Divided into 3 parts)')
  plt.show()

#Function to display a line graph

def show_line_graph():
  plt.plot(days,data,marker='o',linestyle='-',color='purple',label='Profile views')
  plt.xlabel('Days')
  plt.ylabel('Profile views')
  plt.title('Line graph of profile views')
  plt.legend()
  plt.grid(True)
  plt.show() 

#Function to display a scatter plot

def show_scatter_plot():
  plt.scatter(days,data,color='orange',marker='x',alpha=0.7)
  plt.xlabel('Days')
  plt.ylabel('Profile views')
  plt.title('Scatter plot of profile views')
  plt.grid(True)
  plt.show()

  #Function to display a box plot

def show_box_plot():
  plt.boxplot(data,vert=True,patch_artist=True)
  plt.ylabel('Profile views')
  plt.title('Box plot of profile views')
  plt.grid(True)
  plt.show()

  #Function to display a area chart
def show_area_chart():
  plt.fill_between(days,data,color='cyan',alpha=0.4)
  plt.xlabel('Days')
  plt.ylabel('Profile views')
  plt.title('Area chart of profile views')
  plt.grid(True)
  plt.show()

  #Menu for selecting graph type
def main():
   while True:
    print("\nSelect a graph to display:")
    print("1. Histogram")
    print("2. Bar Chart")
    print("3. Pie Chart")
    print("4. Line Graph")
    print("5. Scatter Plot")
    print("6. Box Plot")
    print("7. Area Chart")
    print("8. Exit")

    choice=input("Enter your choice (1-8):")
    if choice=='1':
      show_histogram()
    elif choice=='2':
      show_bar_chart()
    elif choice=='3':
      show_pie_chart()
    elif choice=='4':
      show_line_graph()
    elif choice=='5':
      show_scatter_plot()
    elif choice=='6':
      show_box_plot()
    elif choice=='7':
      show_area_chart()
    elif choice=='8':
      break
if  __name__=='__main__':
  main()
