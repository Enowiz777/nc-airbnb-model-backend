nc-airbnb-model-backend

Download python newest version make sure it is < 3.0 as of 09/02/2022.
Install poetry - Poetry is going to allow us to create a virtual environment. 

*What is poetry?*

- Django is a package that we need to download. 
- Poetry allows us to download and manage packages.

*What is virtual environment?*
- Virtual environment like a bubble.
- Virtual environments allow you to download same package with different versions. so that different versions could be used on seperate projects.
- Example: Use Django virtual environment latest version. 

*How do you create a virtual environment?*
- poetry init. 
-- Interactive guide to create a package. 
-- Just enter on everything. 
-- say yes. 
Output: 
- pyproject.toml gets created: contains description of the virtual environment and the version of python and settings. 

*How do you get inside the bubble?*
1. Enter into a poetry shell. 
```
poetry shell
```
2. Test your VE by running Django Admin command
```
django-admin
```
3. Run 'Exit' to exit the VE.

*How do you start Django project within the folder that you already created?*
```
django-admin startproject config .
```

*Pacakge to install .gitignore*
Download Gitignore and run the command pallete to create gitignore. 

