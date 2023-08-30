"""
@Title: 运行一些测试代码
@Author(s): Stephen CUI
@LastEditor(s): Stephen CUI
@CreatedTime: 2023-08-30 17:03:46
@Description: 
"""

from knn import Sample, LabeledSample, TrainData
data = raw_data = [
    {"sepal_length": 5.1, "sepal_width": 3.5, "petal_length": 1.4,
        "petal_width": 0.2, "label": "Iris-setosa"},
    {"sepal_length": 5.0, "sepal_width": 3.5, "petal_length": 1.4,
        "petal_width": 0.2, "label": "Iris-setosa"},
    {"sepal_length": 4.9, "sepal_width": 3.5, "petal_length": 1.4,
        "petal_width": 0.2, "label": "Iris-setosa"},
    {"sepal_length": 5.5, "sepal_width": 3.6, "petal_length": 1.4,
        "petal_width": 0.2, "label": "Iris-setosa"},
    {"sepal_length": 7.9, "sepal_width": 3.2, "petal_length": 4.7,
        "petal_width": 1.4, "label": "Iris-versicolor"},
    {"sepal_length": 7.9, "sepal_width": 3.2, "petal_length": 4.7,
        "petal_width": 1.4, "label": "Iris-versicolor"},
    {"sepal_length": 7.9, "sepal_width": 3.1, "petal_length": 4.7,
        "petal_width": 1.4, "label": "Iris-versicolor"},
    {"sepal_length": 7.8, "sepal_width": 3.2, "petal_length": 4.7,
        "petal_width": 1.4, "label": "Iris-versicolor"},
    {"sepal_length": 7.9, "sepal_width": 3.3, "petal_length": 4.7,
        "petal_width": 1.4, "label": "Iris-versicolor"},
]


td = TrainData()
td.load(data)
print(td.training)