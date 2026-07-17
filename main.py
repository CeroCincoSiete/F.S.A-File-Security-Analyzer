import os
from rich.console import Console
from rich.panel import Panel
from rich.table import Table
from scanner import analyze_file, get_file_hash
import sys

console = Console()

def run():
    console.print(Panel("[bold cyan]🛡️  File Security Analyzer v1.0[/bold cyan]", subtitle="Modo Análisis Profundo"))
    
    path = input("Introduce la ruta del archivo a analizar: ").strip('"')
    
    if not os.path.exists(path):
        console.print("[bold red]Error: El archivo no existe.[/bold red]")
        return

    tipo, ext_real = analyze_file(path)
    file_hash = get_file_hash(path)

    table = Table(title="Informe de Seguridad")
    table.add_column("Concepto", style="yellow")
    table.add_column("Detalle", style="white")
    
    table.add_row("Firma Detectada", tipo)
    table.add_row("Extensión Original", ext_real)
    table.add_row("Hash SHA-256", file_hash[:20] + "...")
    
    # Lógica de seguridad: Alerta de discrepancia
    if "EXE" in tipo and ext_real != "exe":
        console.print("[bold red]⚠️  ¡ALERTA DE SEGURIDAD![/bold red] ¡Archivo ejecutable oculto bajo otra extensión!")
    
    console.print(table)
    console.print("\n[dim]Nota: Esta herramienta identifica el tipo de archivo. No ejecutes archivos sospechosos.[/dim]")

if __name__ == "__main__":
    run()
