
# File: termux_ai_assistant/code_executor.py
import os
import sys
import subprocess
import tempfile
from pathlib import Path

class CodeExecutor:
    def __init__(self, workspace_dir=None):
        self.workspace_dir = workspace_dir or Path.home() / ".termux_ai_assistant"
        self._ensure_workspace()

    def _ensure_workspace(self):
        """Ensure workspace directory exists."""
        os.makedirs(self.workspace_dir, exist_ok=True)

    def execute_code(self, code, timeout=30):
        """Execute the generated code in a safe environment."""
        try:
            # Create a temporary file for the code
            with tempfile.NamedTemporaryFile(
                mode='w',
                suffix='.py',
                dir=self.workspace_dir,
                delete=False
            ) as temp_file:
                temp_file.write(code)
                temp_file.flush()

            # Execute the code in a subprocess
            result = subprocess.run(
                [sys.executable, temp_file.name],
                capture_output=True,
                text=True,
                timeout=timeout
            )

            # Clean up
            os.unlink(temp_file.name)

            return {
                'stdout': result.stdout,
                'stderr': result.stderr,
                'returncode': result.returncode
            }

        except subprocess.TimeoutExpired:
            return {
                'stdout': '',
                'stderr': 'Execution timed out',
                'returncode': -1
            }
        except Exception as e:
            return {
                'stdout': '',
                'stderr': str(e),
                'returncode': -1
            }
