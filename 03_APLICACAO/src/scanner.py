#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
DriverScan Workspace Audit CLI - Motor de Auditoria e Governança de Permissões
Python 3 stdlib puro - Zero dependências externas
"""

import sys
import sqlite3
import json
from pathlib import Path
from typing import Dict, List, Any

class DriverScanEngine:
    def __init__(self, db_path: str = ":memory:"):
        self.conn = sqlite3.connect(db_path)
        self._init_db()

    def _init_db(self):
        with self.conn:
            self.conn.execute("""
                CREATE TABLE IF NOT EXISTS audit_files (
                    id TEXT PRIMARY KEY,
                    name TEXT,
                    mime_type TEXT,
                    owner_email TEXT,
                    is_shared_externally BOOLEAN,
                    is_public_link BOOLEAN,
                    risk_level TEXT
                )
            """)

    def classificar_risco(self, is_public: bool, is_external: bool) -> str:
        if is_public:
            return "CRITICO"
        if is_external:
            return "ALTO"
        return "BAIXO"

    def registrar_arquivo(self, file_id: str, name: str, mime: str, owner: str, is_public: bool, is_external: bool):
        risco = self.classificar_risco(is_public, is_external)
        with self.conn:
            self.conn.execute("""
                INSERT OR REPLACE INTO audit_files 
                (id, name, mime_type, owner_email, is_shared_externally, is_public_link, risk_level)
                VALUES (?, ?, ?, ?, ?, ?, ?)
            """, (file_id, name, mime, owner, is_external, is_public, risco))

    def obter_estatisticas(self) -> Dict[str, int]:
        cur = self.conn.cursor()
        cur.execute("SELECT risk_level, COUNT(*) FROM audit_files GROUP BY risk_level")
        stats = {"CRITICO": 0, "ALTO": 0, "BAIXO": 0}
        for risco, qtd in cur.fetchall():
            stats[risco] = qtd
        return stats

def executar_demonstracao():
    print("=" * 65)
    print("🔍 TECHDIM DRIVERSCAN - AUDITORIA SIMULADA DE WORKSPACE")
    print("=" * 65)
    
    scanner = DriverScanEngine()
    
    # Simula 5 arquivos com perfis de risco distintos
    amostras = [
        ("file_01", "Planilha_Salarial_Diretoria.xlsx", "application/vnd.ms-excel", "rh@empresa.com", True, True),
        ("file_02", "Credenciais_AWS_Producao.txt", "text/plain", "devops@empresa.com", True, True),
        ("file_03", "Contrato_Cliente_Confidencial.pdf", "application/pdf", "juridico@empresa.com", False, True),
        ("file_04", "Manual_Integracao_API.md", "text/markdown", "eng@empresa.com", False, False),
        ("file_05", "Apresentacao_Vendas_Institucional.pptx", "application/vnd.ms-powerpoint", "mkt@empresa.com", False, False),
    ]
    
    for item in amostras:
        scanner.registrar_arquivo(*item)
        
    stats = scanner.obter_estatisticas()
    print(f"🚨 Arquivos com Risco CRÍTICO (Links Públicos Abertos) : {stats['CRITICO']}")
    print(f"⚠️  Arquivos com Risco ALTO (Compartilhamento Externo)   : {stats['ALTO']}")
    print(f"✅ Arquivos com Risco BAIXO (Acesso Interno Controlado) : {stats['BAIXO']}")
    print("-" * 65)
    print("✓ Auditoria concluída. Relatório de conformidade indexado no SQLite.")

if __name__ == "__main__":
    executar_demonstracao()
