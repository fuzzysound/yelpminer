# Yelpminer
Yelpminer is a tool that helps build complex query for Elasticsearch with Web UI. The name is Yelpminer because this app is just for yelp dataset.

## Requirements
- python >= 3.7.0
- Django >= 3.0.0
- django-rest-framework >= 3.11.0
- Elasticsearch >= 7.6.0
- Bower >= 1.8.8
- Anaconda is recommended for virtual environment. See: [Virtual environments](https://docs.conda.io/projects/conda/en/latest/user-guide/concepts/environments.html#virtual-environments)

## Getting Started
After cloning and activating venv, install required packages using pip and bower.
```
pip install -r requirements.txt
bower install
```

Yelp dataset has to be ready in the directory to which [rest/es_filepaths.py](rest/es_filepaths.py) directs.
You can download Yelp dataset [here](https://www.kaggle.com/yelp-dataset/yelp-dataset).
Since the dataset is huge, it might be better to sample data if you don't have enough storage.
If the dataset is ready and Elasticsearch is running, bulk the data.
```
python manage.py bulk_files
```

After finished, run django server.
```
python manage.py runserver
```

Access to <http://localhost:8000>, and you will see the page below.

Just check the item you want to put in query, and fill the inputs. Remember that inputs are enabled only when their corresponding checkboxes are checked.
Then click the "Build Request" button and the request address will show up below. Click the "View on Browser" button to view response data on DRF browsable API.
Note that if you uncheck the checkbox of any item, its input value won't be passed whether or not there is any value.
