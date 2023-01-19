# Ecommerce Application V1.0.0

This is an Online ecommerce demo project created using Django Web Framework.


## Features

* Create User account
* Create Categories for the products
* Upload the product based on the categories
* Can able to check the products added in each category
* Product variation can be also done with the help of Color and Size
* Search tab for searching the product using keywords
* Store paging is implemented to restrict the number of products to be viewed
* Product filterations are implemented based on the categories 


## Prerequisites

Be sure you have the following installed on your development machine:

+ Python >= 3.7
+ Git >= 2.31.0
+ Git Bash
+ Virtualenv (virtualenvwrapper is recommended)

## Requirements

+ asgiref==3.2.10
+ Django==3.1
+ Pillow==9.4.0
+ pytz==2022.7.1
+ sqlparse==0.4.3


## Project Installation

To setup a local development environment:

Create a virtual environment in which to install Python pip packages. With [virtualenv](https://pypi.python.org/pypi/virtualenv),
```bash
virtualenv venv            # create a virtualenv
source venv/bin/activate   # activate the Python virtualenv 
```

or with [virtualenvwrapper](http://virtualenvwrapper.readthedocs.org/en/latest/),
```bash
mkvirtualenv -p python3 {{project_name}}   # create and activate environment
workon {{project_name}}   # reactivate existing environment
```

or with [Git Bash](recommended),
```bash
python -m venv {{environment_name}} # On Windows Or
python3 -m venv {{environment_name}} # On Mac/ Linus

source {{environment_name}}/Scripts/activate   # activate the Python virtualenv
```

Clone GitHub Project,
```bash
git@github.com:VigneshCatariSureshBabu/EcommerceApplication.git
```

Install development dependencies,
```bash
pip install -r requirements.txt
```

Migrate Database,
```bash
python manage.py migrate
```

Run the web application locally,
```bash
python manage.py runserver # 127.0.0.1:8000
```

Create Superuser,
```bash
python manage.py createsuperuser

or

winpty python manage.py createsuperuser
```

To collect all the static file into the project,
```bash
python manage.py collectstatic
```

## Steps to use the application

* Run the web application
* Go to the http://127.0.0.1:8000/admin and login using the Super User details
* Upload category with some image for example, Jacket image for Jacket as category
* Upload the products based on the category
* Add Color and size of each products uploaded under the variation
* Then start using the application using http://127.0.0.1:8000/
* Check the demo functionality of the application

## Images

* Home Page
![homepage](https://user-images.githubusercontent.com/93681795/213537743-b2a26c67-d4f6-4d84-a3b8-bb97a4fd1f32.JPG)
* Store Page
![StorePage](https://user-images.githubusercontent.com/93681795/213537826-6fc97e72-7998-4565-9bc4-83e1a93ebb8c.JPG)
* Cart Page
![CartPage](https://user-images.githubusercontent.com/93681795/213537893-312782c3-7bb6-4a28-a024-02e214d71329.JPG)
* Checkout Page
![CheckOutPage](https://user-images.githubusercontent.com/93681795/213537943-236ec4a7-7c18-4720-b820-cfff3992945f.JPG)
* List og Categories
![ListOfCategory](https://user-images.githubusercontent.com/93681795/213538104-b8b050bd-65b3-413b-ade6-ebba474df2f3.JPG)
* Category Selection
![CategorySelection](https://user-images.githubusercontent.com/93681795/213538013-32cf093a-d112-447f-a26e-268e85e7ffe3.JPG)
* Product details
![ProductDetailPage](https://user-images.githubusercontent.com/93681795/213539249-6c34609f-8109-45c2-9b84-4797488f0af6.JPG)

Django's admin panel
* Customized user account
![AccountAdmin](https://user-images.githubusercontent.com/93681795/213538342-13a88e0f-0cb4-451a-b3bb-bf0e9148ed5f.JPG)
* Category admin page
![image](https://user-images.githubusercontent.com/93681795/213538744-04f55dd7-1cec-4629-a8df-fc262378b1e1.png)
* Product admin page
![productAdmin](https://user-images.githubusercontent.com/93681795/213538834-a99f604d-c44b-44b1-84d1-dbe17a7c0807.JPG)
* Cart admin page
![CartAdmin](https://user-images.githubusercontent.com/93681795/213538912-9557d9ae-49bf-4087-9cbb-9299d6b292fd.JPG)
* Cart items admin page
![CartItemsAdmin](https://user-images.githubusercontent.com/93681795/213538972-b257ead4-5004-4738-a252-b508f86a06f5.JPG)
* Variation admin page
![VariationAdmin](https://user-images.githubusercontent.com/93681795/213539100-1a0f7479-accb-43cf-8b35-c29941a7c9e8.JPG)
* Products with variation admin page
![ProductsWithVariationAdmin](https://user-images.githubusercontent.com/93681795/213539150-0f2569a5-7401-473f-b04e-250eaff2aff3.JPG)
