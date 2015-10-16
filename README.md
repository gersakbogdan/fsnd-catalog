## Udacity FSND -  P3 Item Catalog
Udacity Full Stack Web Developer Nanodegree P3 Item Catalog Project

### Recipes catalog features:
* Login with Facebook, Twitter or Google+
* Create/Read/Update/Delete recipe categories
* Create/Read/Upadate/Delete recipes
* Add/Delete categories images
* Add/Delete recipes images
* Export categories or recipes to JSON or XML format

### Requirements
* [Python](https://www.python.org/)
* [Virtualenv](https://virtualenv.pypa.io/en/latest/#)
* [Flask](http://flask.pocoo.org)
* [Flask-WTF](https://flask-wtf.readthedocs.org/en/latest/)
* [Flask-Login](https://flask-login.readthedocs.org/en/latest/)
* [Flask-SQLAlchemy](https://pythonhosted.org/Flask-SQLAlchemy/)
* [Rauth](https://rauth.readthedocs.org/en/latest/)
* [Pillow](https://python-pillow.github.io/)
* [SQLAlchemy](http://www.sqlalchemy.org/)
* [SQLAlchemy Migrate](https://sqlalchemy-migrate.readthedocs.org/en/latest/)
* [xmltodict](https://github.com/martinblech/xmltodict)

### Setup
* Install [VirtualBox](https://www.virtualbox.org/) and [Vagrant](https://www.vagrantup.com/)
* Launch & Connect to the VagrantVM
    * ```$ vagrant up```
    * ```$ vagrant ssh```
    * ```$ cd /vagrant/catalog``` # navigate to project root folder
* Config Virtualenv from the root folder
    * ```$ virtualenv flask```
* Install dependencies
    * ```$ ./install.py```
* Create database
    * ```$ ./db-create.py```
* Add test data
    * ```$ ./db-populate.py```
* Open & Change config.py
    * Update ```OAUTH_CREDENTIALS``` with Facebook, Twitter and Google+ oauth details
    * Append your e-mail address to ```ADMIN``` list (you need admin rights to add/edit categories)
* Run
    * ```$ ./run.py```
* View/Use
    * Open in your favourite browser: ```http://localhost:8000```

### Screenshots
![ScreenShot Index](/screenshots/1_index.png)
[View more screenshots](/screenshots/)

### Resources
* **Udacity courses**
    * [Full Stack Foundations](https://www.udacity.com/course/full-stack-foundations--ud088)
    * [Authentication & Authorization: OAuth](https://www.udacity.com/course/authentication-authorization-oauth--ud330)
* Flask
    * [The Flask Mega-Tutorial](http://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-i-hello-world)
    * [OAuth Authentication with Flask](http://blog.miguelgrinberg.com/post/oauth-authentication-with-flask)
* OAuth Integration
    * [Facebook](https://developers.facebook.com/docs/facebook-login/manually-build-a-login-flow)
    * [Twitter](https://dev.twitter.com/oauth)
    * [Google+](https://developers.google.com/+/web/api/rest/oauth)
