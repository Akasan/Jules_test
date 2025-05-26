#!/usr/bin/env python3
import argparse
import sys # Import sys to access command-line arguments for the error message

def main():
    parser = argparse.ArgumentParser(description="Reads a file and prints its content.")
    parser.add_argument("filepath", help="The path to the file to read.")
    
    # Parse arguments early to make filepath available in except block if needed
    # However, if filepath is missing, argparse exits, so this is fine.
    args = parser.parse_args()

    try:
        with open(args.filepath, 'r') as f:
            content = f.read()
            print(content)
    except FileNotFoundError:
        # Access the filepath directly from the parsed arguments.
        # If parse_args() failed (e.g. no argument given), it would have exited before this point.
        print(f"Error: File not found: {args.filepath}")
    except Exception as e:
        # Catch any other potential errors during file operations
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
