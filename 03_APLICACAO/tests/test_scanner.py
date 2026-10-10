#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Testes unitários para o motor do DriverScan Workspace Audit CLI.
"""

import unittest
import sys
from pathlib import Path

SRC_DIR = Path(__file__).resolve().parent.parent / "src"
sys.path.insert(0, str(SRC_DIR))

from scanner import DriverScanEngine

class TestDriverScanEngine(unittest.TestCase):
    def setUp(self):
        self.engine = DriverScanEngine(":memory:")

    def test_classificacao_de_risco(self):
        self.assertEqual(self.engine.classificar_risco(is_public=True, is_external=True), "CRITICO")
        self.assertEqual(self.engine.classificar_risco(is_public=False, is_external=True), "ALTO")
        self.assertEqual(self.engine.classificar_risco(is_public=False, is_external=False), "BAIXO")

    def test_registro_e_estatisticas(self):
        self.engine.registrar_arquivo("1", "doc.pdf", "app/pdf", "user@corp.com", is_public=True, is_external=True)
        self.engine.registrar_arquivo("2", "notes.txt", "text/plain", "user@corp.com", is_public=False, is_external=False)
        stats = self.engine.obter_estatisticas()
        self.assertEqual(stats["CRITICO"], 1)
        self.assertEqual(stats["BAIXO"], 1)

if __name__ == "__main__":
    unittest.main()
