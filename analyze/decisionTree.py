import pandas
from sklearn import tree
from sklearn.tree import DecisionTreeClassifier
import pydotplus
import matplotlib.pyplot as plt
import matplotlib.image as pltimg
from sklearn.tree import export_graphviz

file_name = '../resource/CSV_output.csv'
data_frame = pandas.read_csv(file_name)

map_pattern = {'Low': 0, 'Medium': 1, 'High': 2}
list_ele = list(data_frame.columns.values)
for index in range(len(list_ele) - 2):
    data_frame[list_ele[index]] = data_frame[list_ele[index]].map(map_pattern)

map_pattern = {'American': 1, 'European': 2, 'Japanese': 3}
data_frame['Origin of car'] = data_frame['Origin of car'].map(map_pattern)
map_pattern = {'No': 0, 'Yes': 1}
data_frame['Acceleration'] = data_frame['Acceleration'].map(map_pattern)

# The feature columns & target column
features = ['MPG','Cylinders','Engine displacement','Horsepower','Vehicle weight','Origin of car'];
df_features = data_frame[features]
df_target= data_frame['Acceleration']

#Create a Decision Tree
dtree = DecisionTreeClassifier();
dtree = dtree.fit(df_features, df_target)
data = tree.export_graphviz(dtree, out_file=None, 
    feature_names=features)

# Save it as an image
graph = pydotplus.graph_from_dot_data(data)
graph.write_png('../resource/decision_tree.png')

# Show the image
img=pltimg.imread('../resource/decision_tree.png')
imgplot = plt.imshow(img)
plt.show()