# **Neoway Challenge**
---
# Introduction

This project is a solution to the [Neoway Data Pirates challenge](https://github.com/NeowayLabs/jobs/blob/master/datapirates/challengePirates.md). It consists in fetching an HTML from [Correios](https://www2.correios.com.br/sistemas/buscacep/buscaFaixaCep.cfm) and parsing to extract the postal codes ranges from a pre determined region. And store the results on a [JSONL](https://jsonlines.org/) file.

---
# Getting Started

These instructions will help you to get the project up and running on your local machine.

---
# Prerequisites

- A computer with an internet connection
- [git](https://git-scm.com/downloads)
- [Python 3.10.6](https://www.python.org/downloads/release/python-3106/), or any campatible version
- [beautifulsoup4 ](https://libraries.io/pypi/beautifulsoup4)
- [requests](https://pypi.org/project/requests/2.5.1/)


---
# Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/adinamfranco/neoway-busca-faixa-cep
    ```
2. Open the cloned repository in your text editor.
3. Checkout to the dev branch:
    ```bash
    git checkout dev
    ```
4. Install the `requirements.txt` if needed:
    ```bash
    pip install -r requirements.txt
    ```
---
# Usage

1. To run this projetc, simply run the command on your terminal:
    ```bash
    python3 buscafaixacep.py
    ```
2. Note that the program will create a folder on your directory called 'faixa_cep'. the resuls will be stored there.
3. If you want to add more, or changing the default UFs, open the file `buscafaixacep.py`, and edit the variable called `uf_list` locaed at line 10. Then run the code again. E.g.

    From:
    ```python
    uf_list = ['MG','ES']
    ```

    To:
    ```python
    uf_list = ['RJ','SP']
    ```
---
# Testing
A unit test was writen to test the main functions of the code: `req_faixa_cep()`, `num_max_row()` and `get_cep_list()`.

 To run the test:

   ```bash
    python3 test_buscafaixacep.py
```
---
# Built With

List of tools and references used in this project

- [Ubuntu](https://ubuntu.com/)
- [Visual Studio Code](https://code.visualstudio.com/)
- [HTML](https://html.com/)
- [Python](https://www.python.org/)
- [JSONL](https://jsonlines.org/)
- [Correios](https://www2.correios.com.br/sistemas/buscacep/buscaFaixaCep.cfm)

---
# Author

Adinam Franco - [Github](https://github.com/adinamfranco) - [Linkedin](https://www.linkedin.com/in/adinamfranco/)

---

# License

This project is licensed under the MIT License.

---
