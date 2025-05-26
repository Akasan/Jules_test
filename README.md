# Project Description

This project contains Python scripts for various utilities.

## `main.py`

### Description

The `main.py` script is a command-line utility that reads a specified file and prints its content to the standard output.

### Usage

You can run the script using the Python interpreter:

```bash
python main.py <filepath>
```

Alternatively, after making the script executable (e.g., `chmod +x main.py`), you can run it directly:

```bash
./main.py <filepath>
```

Replace `<filepath>` with the actual path to the file you want to read.

### Example

To read a file named `myfile.txt` located in the same directory as the script, you would run:

```bash
python main.py myfile.txt
```

Or, if executable:

```bash
./main.py myfile.txt
```

If the file is not found, the script will print an error message: `Error: File not found: <filepath>`.
If no filepath is provided, `argparse` will show a usage message and exit.
