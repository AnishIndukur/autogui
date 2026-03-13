# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is a simple Python utility that prevents computers from going to sleep or showing as inactive by moving the mouse cursor periodically. The project consists of a minimal mouse jiggler.

## Package Management

This project uses **uv** for package management. Always use the `--native-tls` flag when installing dependencies:

```bash
# Install dependencies
uv pip install --native-tls -r requirements.txt

# Create virtual environment
uv venv

# Activate virtual environment
source .venv/bin/activate  # Unix/macOS
```

## Running the Application

```bash
python3 tiny_jiggler.py
```

Press `Ctrl+C` to stop.

## Architecture

**Core Components:**

- `tiny_jiggler.py` - Simple terminal script that jiggles the mouse every 60 seconds with random 8-direction movement (including diagonals)

- `main.py` - Placeholder entry point (currently just prints a hello message)

**Key Dependencies:**
- `pyautogui` - Handles all mouse control operations

## macOS Specific Notes

On macOS, the terminal application requires accessibility permissions to control the mouse. Users must grant these permissions in System Preferences > Security & Privacy > Accessibility before the script will function.

## Configuration

The jiggler behavior is controlled by constants at the top of `tiny_jiggler.py`:
- `INTERVAL_SECONDS`: Time between mouse movements (default: 60 seconds)
- `PIXEL_MOVE`: Number of pixels to move the cursor (default: 1 pixel)
