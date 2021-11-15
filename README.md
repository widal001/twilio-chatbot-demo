# Twilio Chatbot Demo

<details open="open">
<summary>Table of Contents</summary>

<!-- TOC -->

- [Twilio Chatbot Demo](#twilio-chatbot-demo)
  - [About this Project](#about-this-project)
    - [Made With](#made-with)
    - [Relevant Documents](#relevant-documents)
  - [Getting Started](#getting-started)
    - [Prerequisites](#prerequisites)
    - [Installation](#installation)
  - [Usage](#usage)
    - [{Use Case 1}](#use-case-1)
  - [Vision and Roadmap](#vision-and-roadmap)
  - [Contributing](#contributing)
  - [License](#license)
  - [Maintainers](#maintainers)
  - [Acknowledgements](#acknowledgements)

<!-- /TOC -->

</details>

## About this Project

Twilio Chatbot Demo serves as an example project for implementing an SMS chatbot using the Twilio API to send and receive messages and FastAPI as the web server to manage requests.

### Made With

- Project Dependencies
  - [fastapi](https://github.com/tiangolo/fastapi) - Modern, fast, web framework for building APIs with Python 3.6+ based on standard Python type hints.
  - [twilio](https://github.com/twilio/twilio-python) - A Python module for communicating with the Twilio API and generating TwiML.
  - [uvicorn](https://github.com/encode/uvicorn) - ASGI web server framework for Python.
  - [dynaconf](https://github.com/rochacbruno/dynaconf) - Configuration management framework for Python.
- Development Dependencies
  - [poetry](https://python-poetry.org/) - Dependency management library that makes creating and installing packages more streamlined.
  - [tox](https://tox.readthedocs.io/en/latest/) - Automates and standardizes the creation of testing environments.
  - [pytest](https://docs.pytest.org/en/6.2.x/) - Simplifies the design and execution of both unit and integration testing.
  - [black](https://black.readthedocs.io/en/stable/) - Autoformats code for consistent styling.
  - [flake8](https://flake8.pycqa.org/en/latest/) - Checks that code complies with PEP8 style guidelines.
  - [pylint](https://www.pylint.org/) - Checks that code follows idiomatic best practices for Python.
  - [pre-commit](https://pre-commit.com/) - Runs code quality checks before code is committed.

### Relevant Documents

- [Architecture Decision Records](docs/adrs)
- [Project Scoping Document](docs/project-scope.md)
- [Data Dictionary](docs/data-dictionary.md)

## Getting Started

### Prerequisites

- Python installed on your local machine, a version between 3.7 and 3.9
- Poetry installed on your local machine

In order to check that you have both Python and Poetry installed, run the following in your command line, and the output should look something like this:

> **NOTE**: in all of the code blocks below, lines preceded with $ indicate commands you should enter in your command line (excluding the $ itself), while lines preceded with > indicate the expected output from the previous command.

```
$ python --version && poetry --version
> Python 3.9.0
> Poetry version 1.1.6
```

**TROUBLESHOOTING:** If you receive an error message, or the version of python you have installed is not between 3.7 and 3.9, consider using a tool like [pyenv](https://github.com/pyenv/pyenv) (on Mac/Linux) or [pyenv-win](https://github.com/pyenv-win/pyenv-win) (on Windows) to manage multiple python installations.

If you have python installed but not poetry, follow these installation instructions:

- [Global install on Mac/Linux](https://python-poetry.org/docs/#osx--linux--bashonwindows-install-instructions)
- [Global install on Windows](https://python-poetry.org/docs/#windows-powershell-install-instructions)
- Local install inside a virtual environment using `pip` **NOTE:** This is not recommended because of potential package conflicts:
  - Create a virtual environment: `python -m venv env`
  - Acvitate the virtual environment. **NOTE:** This virtual environment must be active any time you are working with this project:
    - Mac/Linux: `source env/bin/activate`
    - Windows: `env\Scripts\activate`
  - Install poetry: `pip install poetry`

### Installation

1. [Clone the repository](https://docs.github.com/en/github/creating-cloning-and-archiving-repositories/cloning-a-repository-from-github/cloning-a-repository) on your local machine: `git clone https://github.com/widal001/twilio-chatbot-demo.git`
1. Change directory into the cloned project: `cd twilio-chatbot-demo`
1. Install the package: `poetry install`
1. Install `pre-commit` to autoformat your code: `poetry run pre-commit install`
1. Execute all tests: `poetry run tox`
1. All tests should pass with an output that ends in something like this:
   ```
    py39: commands succeeded
    lint: commands succeeded
    checkdeps: commands succeeded
    pytest: commands succeeded
    coverage: commands succeeded
    congratulations :)
   ```

## Usage

### {Use Case 1}

{1-2 sentence summary of this use case}

1. {Step 1 to complete use case}
1. {Step 2 to complete use case}
1. ... <!-- number of steps and use cases may vary -->

## Vision and Roadmap

The vision for this project is to provide a simple example for building out an SMS chatbot using FastAPI and Twilio. This project aims to fulfill this vision by:

- Modeling best practices for both the FastAPI and Twilio libraries
- Structuring the project for scalability and transferability to multiple use cases
- Documenting key project and architectural decisions

For a more detailed breakdown of the feature roadmap and other development priorities please reference the following links:

- [Feature Roadmap](https://github.com/widal001/twilio-chatbot-demo/projects/1)
- [Architecture Decisions](https://github.com/widal001/twilio-chatbot-demo/projects/2)
- [Bug Fixes](https://github.com/widal001/twilio-chatbot-demo/projects/3)
- [All Issues](https://github.com/widal001/twilio-chatbot-demo/issues)

## Contributing

Contributions are always welcome! We encourage contributions in the form of discussion on issues in this repo and pull requests for improvements to documentation and code.

See [CONTRIBUTING.md](CONTRIBUTING.md) for ways to get started.

## License

Distributed under the MIT License. See [LICENSE](LICENSE) for more information.

## Maintainers

- [@widal001](https://github.com/widal001)

## Acknowledgements

- [Python Packaging Authority Sample Project](https://github.com/pypa/sampleproject)
- [Best README Template](https://github.com/othneildrew/Best-README-Template)
