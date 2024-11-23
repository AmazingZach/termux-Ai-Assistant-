# File: termux_ai_assistant/terminal_ui.py
import asyncio
import os
from prompt_toolkit import PromptSession
from prompt_toolkit.shortcuts import yes_no_dialog
from rich.console import Console
from rich.syntax import Syntax
from .ai_client import AIClient
from .code_executor import CodeExecutor
from .utils import load_config

class TerminalUI:
    def __init__(self):
        self.console = Console()
        self.session = PromptSession()
        self.config = load_config()
        self.ai_client = AIClient(self.config['credentials_path'])
        self.code_executor = CodeExecutor()

    async def run(self):
        """Main UI loop."""
        self.console.print("[bold blue]Termux AI Assistant[/bold blue]")
        self.console.print("Type 'exit' to quit, 'help' for commands\n")

        while True:
            try:
                # Get user input
                prompt = await self.session.prompt_async("TAI> ")
                
                if prompt.lower() in ['exit', 'quit']:
                    break
                elif prompt.lower() == 'help':
                    self._show_help()
                    continue

                # Generate code
                self.console.print("\n[yellow]Generating code...[/yellow]")
                code = await self.ai_client.generate_code(prompt)

                # Display generated code
                self.console.print("\n[green]Generated Code:[/green]")
                syntax = Syntax(code, "python", theme="monokai")
                self.console.print(syntax)

                # Ask for execution confirmation
                if yes_no_dialog(title="Execute Code?", text="Do you want to execute this code?").run():
                    # Execute code
                    self.console.print("\n[yellow]Executing code...[/yellow]")
                    result = self.code_executor.execute_code(code)

                    # Display results
                    if result['returncode'] == 0:
                        self.console.print("\n[green]Output:[/green]")
                        self.console.print(result['stdout'])
                    else:
                        self.console.print("\n[red]Error:[/red]")
                        self.console.print(result['stderr'])

            except KeyboardInterrupt:
                continue
            except Exception as e:
                self.console.print(f"\n[red]Error: {str(e)}[/red]")

    def _show_help(self):
        """Display help information."""
        help_text = """
        Commands:
        - help: Show this help message
        - exit/quit: Exit the application
        
        Usage:
        Simply type your code generation request in natural language.
        The AI will generate the code, and you can choose to execute it.
        """
        self.console.print(help_text)

def main():
    """Entry point for the application."""
    ui = TerminalUI()
    asyncio.run(ui.run())

if __name__ == "__main__":
    main()