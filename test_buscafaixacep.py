import unittest
from unittest.mock import patch
import requests
import json
import re
from pathlib import Path
from bs4 import BeautifulSoup
from buscafaixacep import req_faixa_cep, num_max_row, get_cep_list

class TestCepScraper(unittest.TestCase):
    @patch('requests.post')
    def test_req_faixa_cep(self, mock_post):
        mock_post.return_value.text = "<html><body>Test</body></html>"
        uf = 'SP'
        pagini = 1
        pagfim = 50
        result = req_faixa_cep(uf, pagini, pagfim)
        self.assertEqual(result.text, "<html><body>Test</body></html>")
        mock_post.assert_called_with('https://www2.correios.com.br/sistemas/buscacep/resultadoBuscaFaixaCEP.cfm',
                                     data={'UF': 'SP', 'qtd_row': 50, 'pagini': 1, 'pagfim': 50})

    def test_num_max_row(self):
        page = "<html><body>1 a 50 de 1000</body></html>"
        result = num_max_row(None, None, page)
        self.assertEqual(result, 0)

    def test_get_cep_list(self):
        page = "<html><body><div class='ctrlcontent'><table><tr><td>Test 1</td><td>Test 2</td><td>Test 3</td><td>Test 4</td></tr></table></div></body></html>"
        expected_result = ['Empty list, check the URL, or the desired UF and try again']
        result = get_cep_list(page)
        self.assertEqual(result, expected_result)

if __name__ == '__main__':
    unittest.main()