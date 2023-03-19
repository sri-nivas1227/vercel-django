# Welcome to KalaKumbh
KalaKumbh is an app for aspiring singers to help them earn money, recognition, and validation by conducting competitions, community, and mentors(without recognition being a major barrier in the process). It levels them up in the money-recognition cycle.
In short, an accelerator for singers.

### Steps to follow to run the app locally

- Clone the project using `git clone https://github.com/sri-nivas1227/kalakumbh-website.git`
- change your directory -  `cd kalakumbh-website`
- create a virtual environment - `python -m venv env` or `py -m venv env`
- activate your virtaul environment - `./env/scripts/activate`
- Install all the python dependencies for the project `pip install -r requirements.txt`
- then open settings.py present in _kalakumbh_soon/settings.py_
- change the `NPM_BIN_PATH` value to your local npm path
    - you can find it by running `where npm` in command prompt
- Run these commands in order
    `python manage.py tailwind install`
    `python manage.py tailwind start`
- open a new terinal and run
    `python manage.py runserver`
    open 127.0.0.1:8000 in the broweser to use the app