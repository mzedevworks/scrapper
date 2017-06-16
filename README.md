scrapper
========

#What it does
---------------
- This project will scrape a given wikipedia url to get the table of contents

#Setting Up
- First you will need to install pip assuming you are using Linux.

- For other versions check from the pip documentation [link to pip installation   !](https://pip.pypa.io/en/stable/)

   $sudo apt-get update

   $sudo apt-get -y install python-pip

- After that you will need to install the virtual environment you might also need to install the virtual
environment wrapper but its not a requirement so will leave the details

   $sudo pip install --upgrade virtualenv

##Starting the application

- Clone the project onto your local machine.

- Change directory into your newly created project.

    cd scrapper

- To make the process easier use the script in the root of the project called start.sh.

    ./start.sh

- If it doesnt work due to permissions change it to an executable file

    $sudo chmod +x start.sh

- It will ask you if you want to run tests or not

- Press 1 to do the tests and 2 to continue