#!/bin/bash

MODULE_NAME="odoo-custom-sale-report"
ZIP_NAME="${MODULE_NAME}.zip"

# Eliminar zips anteriores
[ -f "$ZIP_NAME" ] && rm "$ZIP_NAME"

# Crear archivo .zip ignorando .git y archivos temporales
zip -r "$ZIP_NAME" "$MODULE_NAME" \
    -x "*.pyc" "__pycache__/*" ".git/*" "*/.DS_Store" "*.zip" "*.swp" "*.bak" "*.env" ".idea/*" ".vscode/*"

echo "📦 Módulo empaquetado como $ZIP_NAME"
