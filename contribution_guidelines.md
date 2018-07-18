# Candi Contribution Guidelines

## Setting up the development environment

Getting set up to contribute to Candi can be accomplished in just a few simple steps.

1. Verify that you have Python and Pipenv installed.
    - Python is the programming language Candi is written in. It can be downloaded from the [official website](https://www.python.org/).
    - Pipenv is a Python module that Candi uses to manage its depencies. Once you Python installed, Pipenv can be installed by executing the command `pip install pipenv` in the console.
2. Clone the Candi repository
    - You'll have to install [Git](https://git-scm.com/) for this.
    - Navigate to the desired directory and execute the command `git clone https://github.com/sgh304/candi.git` in the console.
3. Install dependencies with Pipenv
    - Navigate to the project directory (/candi/) and execure the command `pipenv install`.
    - This will create a new virtual environment for Candi and install all of the project's required dependencies.
    - Because the dependencies will be installed to the virtual environment, you'll want to run all code with the `pipenv run python -m ______` command.
    - Note that this configuration does not include setup for working with the Candi database or web application. I don't really expect anyone else to be working on those aspects of the project, but, if you have ideas for improvements in those areas, please go for it and just let me know if anything is unclear.

## Understanding the project structure

Hopefully Candi's project structure is pretty simple. There are currently five modules in src:
1. src.candidate
    - Code for Candi's generalized candidate model.
2. src.state
    - Code for state-specific implementations. The module is futher split into submodules for each state using their postal abbreviations. Each submodule should contain a get_abbreviation_candidates function, which fetches candidate information from the state's Secretary of State website and returns it as a list of src.candidate.Candidate objects. These submodules should export the state's get_abbreviation_candidates function, along with any other objects needed for testing, in their __init__.py files. The state module itself should export each state's get_abbreviation_candidates function for use in the database creation script. (If this is unclear, look at the current structure of the module)
3. src.test
    - Code for testing. The module is further split into src.test.candidate and src.test.state for clear testing of each component. Pytest is relied on to discover tests using its standard test discovery rules.
4. src.db
    - Code for managing the Candi database. This is basically just a script (src.db.create_new_db) that I run on the server on an interval to refresh the database with new information.
5. src.web
    - Code for managing the Candi webapp. Flask provides the API backend that lets users query the Candi server's database.

## Standards for contributions

The project is currently in its early stages. That said, given Candi's goal of providing standardized candidate information, there are some simple standards for code contribution:

1. Follow the project structure outlined above. 
    - If you're working on implementing a state, please create a new folder in the /candi/src/state/ directory, etc.
2. Use pipenv for dependency management.
    - If you introduce a new dependency, make sure to install it to the project environment with `pipenv install _____`. Please refer to the [official Pipenv documentation](https://docs.pipenv.org/) for help.
3. Provide test cases for new functionality.
    - The project uses pytest for testing, meaning tests can be run from the project directory with the `pipenv run pytest` command. The existing tests in the /candi/src/test/ directory can guide your own test development.