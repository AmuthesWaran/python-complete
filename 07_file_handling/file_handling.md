# Python File Handling — From Basics to Advanced (Complete Guide)

> **Audience:** Beginners to working professionals and data engineers  
> **Goal:** Build a solid foundation in Python file I/O and scale it to production-grade, large-dataset workflows  
> **Python Version:** 3.8+

---

## Table of Contents

1. [Introduction](#1-introduction)
2. [Basics of File Handling](#2-basics-of-file-handling)
3. [Working with Paths](#3-working-with-paths)
4. [Reading & Writing Text Files](#4-reading--writing-text-files)
5. [Binary File Handling](#5-binary-file-handling)
6. [CSV File Handling](#6-csv-file-handling)
7. [JSON File Handling](#7-json-file-handling)
8. [Handling Large Files (Millions of Rows)](#8-handling-large-files-millions-of-rows)
9. [Performance Optimization Techniques](#9-performance-optimization-techniques)
10. [Error Handling & Logging](#10-error-handling--logging)
11. [Real-World Data Engineering Examples](#11-real-world-data-engineering-examples)
12. [Security & Safety](#12-security--safety)
13. [Best Practices Summary](#13-best-practices-summary)
14. [Final Cheat Sheet](#14-final-cheat-sheet)

---

## 1. Introduction

### What Is File Handling?

File handling is the process of **creating, reading, writing, updating, and deleting files** stored on a filesystem using a programming language. In Python, the built-in `open()` function is your primary gateway to file I/O operations.

```
┌─────────────────────────────────────────────┐
│              Python Program                 │
│                                             │
│   open() → read() / write() → close()      │
└───────────────────┬─────────────────────────┘
                    │
          ┌─────────▼──────────┐
          │   Operating System │
          │   (File System API)│
          └─────────┬──────────┘
                    │
          ┌─────────▼──────────┐
          │   Storage (Disk /  │
          │   SSD / Network FS)│
          └────────────────────┘
```

### Why It Matters in Real-World Systems

File handling is fundamental to virtually every software system:

- **Data Engineering:** ETL pipelines read CSVs, JSON, Parquet, Avro files
- **Log Management:** Servers write millions of log lines per day
- **Configuration:** Apps read YAML/INI/JSON config files at startup
- **ML/AI Pipelines:** Training datasets are often flat files (CSV, TFRecord)
- **Reporting:** Generating PDFs, Excel sheets, or flat-file exports
- **Microservices:** Reading/writing shared files or temporary data

### Types of Files

| File Type | Extension(s) | Description | Typical Use Case |
|-----------|-------------|-------------|-----------------|
| **Text** | `.txt`, `.log`, `.md` | Human-readable characters | Logs, notes, configs |
| **Structured Text** | `.csv`, `.tsv` | Delimited tabular data | Data interchange, analytics |
| **JSON** | `.json`, `.jsonl` | Key-value structured text | APIs, configs, NoSQL exports |
| **Binary** | `.bin`, `.dat`, `.pkl` | Raw bytes, not human-readable | Images, serialized objects |
| **Image** | `.png`, `.jpg`, `.gif` | Binary image formats | Computer vision, media |
| **Compressed** | `.gz`, `.zip`, `.bz2` | Compressed data | Storage optimization |
| **Columnar** | `.parquet`, `.orc` | Column-oriented binary | Big data analytics |
| **Log Files** | `.log`, `.log.gz` | Timestamped event records | Monitoring, debugging |

---

## 2. Basics of File Handling

### Opening Files with `open()`

The built-in `open()` function is the foundation of all file I/O in Python.

**Syntax:**
```python
file_object = open(file_path, mode='r', encoding='utf-8', buffering=-1, errors='strict')
```

### File Modes

| Mode | Symbol | Description |
|------|--------|-------------|
| Read | `'r'` | Read only (default). File must exist. |
| Write | `'w'` | Write only. Creates file; truncates if exists. |
| Append | `'a'` | Write only. Creates file; appends if exists. |
| Exclusive Create | `'x'` | Write only. Fails if file already exists. |
| Read+Write | `'r+'` | Read and write. File must exist. |
| Binary Read | `'rb'` | Read binary data. |
| Binary Write | `'wb'` | Write binary data. |
| Binary Append | `'ab'` | Append binary data. |
| Text Mode | `'t'` | Default; used with r/w/a (e.g., `'rt'`, `'wt'`). |

```python
# Basic open and close (manual — not recommended for production)
f = open("data.txt", "r", encoding="utf-8")
content = f.read()
f.close()  # ← You MUST close, or the file stays locked

# Better: read lines
f = open("data.txt", "r", encoding="utf-8")
for line in f:
    print(line.strip())
f.close()
```

### Reading Methods

```python
with open("data.txt", "r", encoding="utf-8") as f:

    # 1. read() — entire file as a single string
    content = f.read()

with open("data.txt", "r", encoding="utf-8") as f:

    # 2. readline() — one line at a time (moves cursor forward)
    first_line  = f.readline()
    second_line = f.readline()

with open("data.txt", "r", encoding="utf-8") as f:

    # 3. readlines() — all lines as a list
    lines = f.readlines()   # ['line1\n', 'line2\n', ...]
    lines = [l.strip() for l in lines]  # strip newlines
```

**When to use which:**

| Method | Memory | Best For |
|--------|--------|----------|
| `read()` | Loads entire file | Small files (<50 MB) |
| `readline()` | One line | Custom line-by-line logic |
| `readlines()` | All lines as list | Small files needing random access |
| `for line in f:` | One line | Large files — memory-efficient |

### Writing and Appending

```python
# Write (overwrites if file exists)
with open("output.txt", "w", encoding="utf-8") as f:
    f.write("Hello, World!\n")
    f.write("Second line.\n")

# Append (adds to existing file)
with open("output.txt", "a", encoding="utf-8") as f:
    f.write("Appended line.\n")

# Write multiple lines at once
lines = ["Alice\n", "Bob\n", "Charlie\n"]
with open("names.txt", "w", encoding="utf-8") as f:
    f.writelines(lines)  # Note: writelines does NOT add newlines automatically
```

### Using `with` — The Context Manager (Always Preferred)

The `with` statement ensures the file is automatically closed — even if an exception occurs.

```python
# ✅ Correct: file is always closed after the with block
with open("data.txt", "r", encoding="utf-8") as f:
    content = f.read()
# f is now closed here, even if an error occurred inside the block

# ✅ Multiple files in one with block (Python 3.x)
with open("input.txt", "r") as fin, open("output.txt", "w") as fout:
    for line in fin:
        fout.write(line.upper())
```

### Common Pitfalls and How to Avoid Them

```python
# ❌ PITFALL 1: Forgetting to close the file
f = open("data.txt", "r")
data = f.read()
# f.close() forgotten — file handle leaks! Use 'with' instead.

# ❌ PITFALL 2: Reading large file with .read()
content = open("10GB_file.csv").read()  # Crashes with MemoryError

# ✅ FIX: Iterate line by line
with open("10GB_file.csv", "r") as f:
    for line in f:
        process(line)

# ❌ PITFALL 3: Wrong encoding
with open("arabic_data.txt", "r") as f:  # Default encoding varies by OS!
    text = f.read()  # Might throw UnicodeDecodeError

# ✅ FIX: Always specify encoding
with open("arabic_data.txt", "r", encoding="utf-8") as f:
    text = f.read()

# ❌ PITFALL 4: Writing binary to text mode
with open("image.png", "w") as f:
    f.write(image_bytes)  # TypeError

# ✅ FIX: Use binary mode
with open("image.png", "wb") as f:
    f.write(image_bytes)

# ❌ PITFALL 5: Using 'w' mode when you meant 'a'
with open("log.txt", "w") as f:
    f.write("new entry")  # Erases all previous log data!

# ✅ FIX: Use 'a' mode for logs
with open("log.txt", "a") as f:
    f.write("new entry\n")
```

---

## 3. Working with Paths

### `os` Module Basics

```python
import os

# Current working directory
cwd = os.getcwd()
print(cwd)  # /home/user/project

# Join paths (OS-agnostic)
path = os.path.join("data", "raw", "file.csv")
# On Unix:    data/raw/file.csv
# On Windows: data\raw\file.csv

# Check existence
os.path.exists("data/file.csv")   # True or False
os.path.isfile("data/file.csv")   # Is it a file?
os.path.isdir("data/")            # Is it a directory?

# Get parts
os.path.basename("/data/raw/file.csv")   # 'file.csv'
os.path.dirname("/data/raw/file.csv")    # '/data/raw'
os.path.splitext("file.csv")            # ('file', '.csv')

# List directory contents
files = os.listdir("data/")

# Walk a directory tree recursively
for dirpath, dirnames, filenames in os.walk("data/"):
    for fname in filenames:
        full_path = os.path.join(dirpath, fname)
        print(full_path)

# Create directories
os.makedirs("output/reports/2024", exist_ok=True)  # exist_ok avoids error if exists

# Rename and delete
os.rename("old_name.txt", "new_name.txt")
os.remove("unwanted.txt")
```

### `pathlib` Best Practices (Recommended for Python 3.4+)

`pathlib` is the modern, object-oriented alternative to `os.path`. It is cleaner and more expressive.

```python
from pathlib import Path

# Create a path object
p = Path("data/raw/transactions.csv")

# Properties
print(p.name)       # 'transactions.csv'
print(p.stem)       # 'transactions'
print(p.suffix)     # '.csv'
print(p.parent)     # PosixPath('data/raw')
print(p.parts)      # ('data', 'raw', 'transactions.csv')

# Join paths with /
base = Path("data")
raw  = base / "raw" / "file.csv"   # Pythonic path joining!

# Check
raw.exists()
raw.is_file()
raw.is_dir()

# Read and write directly (no open() needed for simple cases)
text = raw.read_text(encoding="utf-8")
raw.write_text("Hello!", encoding="utf-8")

binary = raw.read_bytes()
raw.write_bytes(b"\x00\x01\x02")

# Iterate directory
for csv_file in Path("data/").glob("*.csv"):
    print(csv_file)

# Recursive glob
for log_file in Path("logs/").rglob("*.log"):
    print(log_file)

# Create directories
Path("output/reports").mkdir(parents=True, exist_ok=True)

# Resolve absolute path (resolves symlinks too)
abs_path = Path("../config.yaml").resolve()
```

### Cross-Platform Path Handling

```python
from pathlib import Path, PurePosixPath, PureWindowsPath
import os

# Always use pathlib or os.path.join — NEVER hardcode separators
# ❌ Bad
path = "data\\raw\\file.csv"      # Windows-only
path = "data/raw/file.csv"        # Unix-only string

# ✅ Good
path = Path("data") / "raw" / "file.csv"   # Works everywhere

# Get home directory
home = Path.home()          # /home/user or C:\Users\user

# Get temp directory
import tempfile
tmpdir = Path(tempfile.gettempdir())

# Environment-based paths
data_dir = Path(os.environ.get("DATA_DIR", "data/"))
```

---

## 4. Reading & Writing Text Files

### Line-by-Line Processing

```python
# Most memory-efficient for large text files
def count_lines(filepath: str) -> int:
    count = 0
    with open(filepath, "r", encoding="utf-8") as f:
        for _ in f:
            count += 1
    return count

# Process and filter lines
def extract_errors(log_path: str, output_path: str) -> None:
    with open(log_path, "r", encoding="utf-8") as fin, \
         open(output_path, "w", encoding="utf-8") as fout:
        for line in fin:
            if "ERROR" in line:
                fout.write(line)
```

### Efficient Iteration

```python
# Using enumerate for line numbers
with open("data.txt", "r", encoding="utf-8") as f:
    for line_num, line in enumerate(f, start=1):
        print(f"Line {line_num}: {line.rstrip()}")

# islice to read first N lines
from itertools import islice

with open("huge_file.txt", "r", encoding="utf-8") as f:
    first_100 = list(islice(f, 100))

# Generator-based line reader (lazy)
def read_lines(filepath: str, encoding: str = "utf-8"):
    with open(filepath, "r", encoding=encoding) as f:
        for line in f:
            yield line.rstrip("\n")

for line in read_lines("data.txt"):
    print(line)
```

### Handling Encodings

```python
# Common encodings
# UTF-8:       Universal, supports all languages. Default for modern systems.
# UTF-16:      Fixed 2-byte, common in Windows legacy files.
# ISO-8859-1:  Latin-1, Western European legacy files.
# CP1252:      Windows Western European encoding.
# ASCII:       7-bit, no special characters.

# Detect encoding (requires chardet)
# pip install chardet
import chardet

def detect_encoding(filepath: str) -> str:
    with open(filepath, "rb") as f:
        raw = f.read(100_000)  # Read first 100KB for detection
    result = chardet.detect(raw)
    return result["encoding"] or "utf-8"

enc = detect_encoding("unknown_file.txt")
with open("unknown_file.txt", "r", encoding=enc) as f:
    content = f.read()

# Handling encoding errors gracefully
with open("messy.txt", "r", encoding="utf-8", errors="replace") as f:
    # 'replace': replace bad chars with ?
    content = f.read()

with open("messy.txt", "r", encoding="utf-8", errors="ignore") as f:
    # 'ignore': silently skip undecodable bytes
    content = f.read()

with open("messy.txt", "r", encoding="utf-8", errors="backslashreplace") as f:
    # 'backslashreplace': replace with \xNN escape
    content = f.read()
```

### Error Handling Strategies

```python
def safe_read(filepath: str, encoding: str = "utf-8") -> str | None:
    """Read a file safely, returning None on error."""
    try:
        with open(filepath, "r", encoding=encoding) as f:
            return f.read()
    except FileNotFoundError:
        print(f"File not found: {filepath}")
    except PermissionError:
        print(f"Permission denied: {filepath}")
    except UnicodeDecodeError as e:
        print(f"Encoding error in {filepath}: {e}")
    return None
```

---

## 5. Binary File Handling

### Reading and Writing Binary Data

```python
# Write binary
data = bytes([0x89, 0x50, 0x4E, 0x47])  # PNG magic bytes
with open("header.bin", "wb") as f:
    f.write(data)

# Read binary
with open("header.bin", "rb") as f:
    raw = f.read()
    print(raw.hex())   # '89504e47'

# Copy a binary file
def copy_file(src: str, dst: str, chunk_size: int = 65536) -> None:
    with open(src, "rb") as fin, open(dst, "wb") as fout:
        while chunk := fin.read(chunk_size):
            fout.write(chunk)
```

### Working with Images

```python
# Using built-in binary I/O to inspect images
def get_image_format(filepath: str) -> str:
    magic = {
        b"\x89PNG":    "PNG",
        b"\xff\xd8\xff": "JPEG",
        b"GIF8":       "GIF",
        b"RIFF":       "WEBP",
        b"%PDF":       "PDF",
    }
    with open(filepath, "rb") as f:
        header = f.read(4)
    for sig, fmt in magic.items():
        if header.startswith(sig):
            return fmt
    return "Unknown"

# Working with images using Pillow
# pip install Pillow
from PIL import Image

with Image.open("photo.jpg") as img:
    print(img.format, img.size, img.mode)  # JPEG (1920, 1080) RGB
    thumb = img.resize((200, 200))
    thumb.save("thumb.jpg", quality=85)
```

### Using `struct` for Packed Binary Data

`struct` lets you pack/unpack primitive C types into/from bytes — useful for custom binary protocols, file headers, or reading binary formats.

```python
import struct

# Pack: Python values → bytes
# Format: '<' = little-endian, 'I' = unsigned int (4 bytes), 'f' = float (4 bytes)
packed = struct.pack("<If", 42, 3.14)
print(len(packed))   # 8 bytes
print(packed.hex())  # 2a0000004...(hex)

# Unpack: bytes → Python values
value_int, value_float = struct.unpack("<If", packed)
print(value_int, value_float)  # 42, 3.140000104904175

# Format characters
# 'b': signed char (1B)   'B': unsigned char (1B)
# 'h': short (2B)         'H': unsigned short (2B)
# 'i': int (4B)           'I': unsigned int (4B)
# 'q': long long (8B)     'Q': unsigned long long (8B)
# 'f': float (4B)         'd': double (8B)
# 's': char[] (string)

# Real-world: Reading a custom binary file header
HEADER_FORMAT = "<4sIIH"   # magic(4B) + version(4B) + rows(4B) + cols(2B)
HEADER_SIZE = struct.calcsize(HEADER_FORMAT)  # 14 bytes

def read_custom_header(filepath: str) -> dict:
    with open(filepath, "rb") as f:
        raw = f.read(HEADER_SIZE)
    magic, version, rows, cols = struct.unpack(HEADER_FORMAT, raw)
    return {
        "magic":   magic.decode("ascii"),
        "version": version,
        "rows":    rows,
        "cols":    cols,
    }

def write_custom_header(filepath: str, rows: int, cols: int) -> None:
    header = struct.pack(HEADER_FORMAT, b"MYFT", 1, rows, cols)
    with open(filepath, "wb") as f:
        f.write(header)
```

---

## 6. CSV File Handling (Beginner → Advanced)

### Using Python's `csv` Module

```python
import csv

# --- Reading CSV ---
with open("employees.csv", "r", encoding="utf-8", newline="") as f:
    reader = csv.reader(f)
    header = next(reader)          # Read header row
    print("Columns:", header)
    for row in reader:
        print(row)                 # List of strings

# DictReader: rows as dicts (column name → value)
with open("employees.csv", "r", encoding="utf-8", newline="") as f:
    reader = csv.DictReader(f)
    for row in reader:
        print(row["name"], row["salary"])

# --- Writing CSV ---
data = [
    {"name": "Alice", "age": 30, "city": "Chennai"},
    {"name": "Bob",   "age": 25, "city": "Mumbai"},
]

with open("output.csv", "w", encoding="utf-8", newline="") as f:
    writer = csv.DictWriter(f, fieldnames=["name", "age", "city"])
    writer.writeheader()
    writer.writerows(data)

# Always use newline='' to prevent extra blank lines on Windows
```

### Dialects, Quoting, and Delimiters

```python
import csv

# Custom delimiter (tab-separated values)
with open("data.tsv", "r", encoding="utf-8", newline="") as f:
    reader = csv.reader(f, delimiter="\t")
    for row in reader:
        print(row)

# Semicolon-separated (common in European locales)
with open("data_eu.csv", "r", encoding="utf-8", newline="") as f:
    reader = csv.reader(f, delimiter=";")
    for row in reader:
        print(row)

# Quoting options
# csv.QUOTE_ALL:       Quote all fields
# csv.QUOTE_MINIMAL:   Quote only fields with special chars (default)
# csv.QUOTE_NONNUMERIC: Quote all non-numeric fields
# csv.QUOTE_NONE:      Never quote (use escapechar for special chars)

with open("output.csv", "w", newline="") as f:
    writer = csv.writer(f, quoting=csv.QUOTE_ALL)
    writer.writerow(["name", "notes"])
    writer.writerow(["Alice", 'She said, "Hello"'])

# Register a custom dialect
csv.register_dialect(
    "pipe_delimited",
    delimiter="|",
    quoting=csv.QUOTE_MINIMAL,
    lineterminator="\n",
)

with open("data.pipe", "w", newline="") as f:
    writer = csv.writer(f, dialect="pipe_delimited")
    writer.writerow(["id", "value"])
    writer.writerow([1, "foo"])
```

### Streaming Large CSVs

```python
import csv
from typing import Iterator

def stream_csv(filepath: str, chunk_size: int = 1000) -> Iterator[list[dict]]:
    """Yield chunks of rows from a large CSV file."""
    with open(filepath, "r", encoding="utf-8", newline="") as f:
        reader = csv.DictReader(f)
        chunk = []
        for row in reader:
            chunk.append(row)
            if len(chunk) >= chunk_size:
                yield chunk
                chunk = []
        if chunk:
            yield chunk  # Yield remaining rows

# Usage
for batch in stream_csv("huge_file.csv", chunk_size=10_000):
    process_batch(batch)  # Process 10,000 rows at a time
```

### Writing Clean CSV Output

```python
import csv
import io

def write_clean_csv(data: list[dict], filepath: str) -> None:
    """Write a clean, portable CSV file."""
    if not data:
        return
    fieldnames = list(data[0].keys())
    with open(filepath, "w", encoding="utf-8-sig", newline="") as f:
        # utf-8-sig adds BOM — ensures Excel opens UTF-8 correctly
        writer = csv.DictWriter(
            f,
            fieldnames=fieldnames,
            quoting=csv.QUOTE_NONNUMERIC,
            extrasaction="ignore",
        )
        writer.writeheader()
        writer.writerows(data)
    print(f"Wrote {len(data)} rows to {filepath}")
```

### Comparison: CSV Libraries

| Feature | `csv` (stdlib) | `pandas` | `pyarrow` | `polars` |
|---------|---------------|----------|-----------|----------|
| **Dependencies** | None | Heavy | Medium | Light |
| **Speed (large files)** | Slow | Medium | Fast | Fastest |
| **Memory efficiency** | High (streaming) | Low | High (chunked) | Very High |
| **Lazy evaluation** | Manual | No | No | Yes |
| **DataFrame output** | No | Yes | Yes | Yes |
| **Schema inference** | No | Yes | Yes | Yes |
| **Best for** | Small files, no deps | Analysis, medium files | Parquet convert, Arrow | Big data, analytics |
| **pip install** | — | `pandas` | `pyarrow` | `polars` |

```python
# pandas
import pandas as pd
df = pd.read_csv("data.csv", chunksize=100_000)

# pyarrow
import pyarrow.csv as pv
table = pv.read_csv("data.csv")

# polars (lazy, zero-copy)
import polars as pl
df = pl.scan_csv("data.csv").filter(pl.col("amount") > 100).collect()
```

---

## 7. JSON File Handling

### `json` Module Basics

```python
import json

# --- Reading JSON ---
with open("config.json", "r", encoding="utf-8") as f:
    data = json.load(f)     # dict or list

# From string
json_str = '{"name": "Alice", "age": 30}'
data = json.loads(json_str)

# --- Writing JSON ---
data = {"name": "Alice", "scores": [95, 88, 72]}

with open("output.json", "w", encoding="utf-8") as f:
    json.dump(data, f)

# From object to string
json_str = json.dumps(data)
```

### Pretty Printing

```python
import json

data = {"users": [{"id": 1, "name": "Alice"}, {"id": 2, "name": "Bob"}]}

# Pretty print to file
with open("pretty.json", "w", encoding="utf-8") as f:
    json.dump(data, f, indent=4, sort_keys=True, ensure_ascii=False)

# Pretty print to console
print(json.dumps(data, indent=2))

# Handle non-serializable types
from datetime import datetime, date
import decimal

def json_default(obj):
    if isinstance(obj, (datetime, date)):
        return obj.isoformat()
    if isinstance(obj, decimal.Decimal):
        return float(obj)
    raise TypeError(f"Type {type(obj)} not JSON serializable")

data = {"ts": datetime.now(), "price": decimal.Decimal("19.99")}
with open("output.json", "w") as f:
    json.dump(data, f, default=json_default, indent=2)
```

### JSONL (JSON Lines) — One JSON Object Per Line

```python
import json

# Writing JSONL
records = [{"id": 1, "val": "a"}, {"id": 2, "val": "b"}]
with open("data.jsonl", "w", encoding="utf-8") as f:
    for record in records:
        f.write(json.dumps(record) + "\n")

# Reading JSONL (streaming — great for large files)
def read_jsonl(filepath: str):
    with open(filepath, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if line:
                yield json.loads(line)

for record in read_jsonl("data.jsonl"):
    print(record)
```

### Streaming Large JSON with `ijson`

```python
# pip install ijson
import ijson

# A huge JSON file like: {"records": [{...}, {...}, ...]}
# ijson parses it incrementally without loading it all into memory

def stream_json_array(filepath: str, key: str = "records.item"):
    """Stream items from a large JSON array."""
    with open(filepath, "rb") as f:
        for record in ijson.items(f, key):
            yield record

# Usage
for record in stream_json_array("large_export.json"):
    process(record)

# ijson with multiple passes
def get_record_count(filepath: str) -> int:
    count = 0
    with open(filepath, "rb") as f:
        for _ in ijson.items(f, "records.item"):
            count += 1
    return count
```

---

## 8. Handling Large Files (Millions of Rows)

### Memory-Efficient Patterns

```
┌───────────────────────────────────────────────────┐
│            File (10GB CSV on disk)                │
└───────────────────────┬───────────────────────────┘
                        │
              ┌─────────▼──────────┐
              │  Read Buffer (64KB)│  ← OS reads in chunks
              └─────────┬──────────┘
                        │
              ┌─────────▼──────────┐
              │  Python Iterator   │  ← yields one line at a time
              └─────────┬──────────┘
                        │
              ┌─────────▼──────────┐
              │  Process / Filter  │  ← only ~1 line in memory
              └─────────┬──────────┘
                        │
              ┌─────────▼──────────┐
              │  Write Output      │  ← flush to disk periodically
              └────────────────────┘
```

### Chunked Reading

```python
import pandas as pd

# Read in 100K row chunks — never loads whole file
def process_large_csv(filepath: str, chunk_size: int = 100_000) -> None:
    total = 0
    for chunk in pd.read_csv(filepath, chunksize=chunk_size):
        # Each chunk is a DataFrame of chunk_size rows
        filtered = chunk[chunk["amount"] > 0]
        total += len(filtered)
        filtered.to_csv("output.csv", mode="a", header=(total == len(filtered)), index=False)
    print(f"Total rows processed: {total}")
```

### Buffered I/O

```python
import io

# Default buffering is usually fine, but you can tune it
# buffering=0: unbuffered (binary mode only)
# buffering=1: line-buffered (text mode only)
# buffering=N: use N-byte buffer

# 4MB write buffer for better throughput
with open("large_output.txt", "w", encoding="utf-8", buffering=4*1024*1024) as f:
    for i in range(10_000_000):
        f.write(f"row {i}\n")

# Wrap with BufferedWriter explicitly
with open("output.bin", "wb") as raw:
    with io.BufferedWriter(raw, buffer_size=8*1024*1024) as f:
        for chunk in data_generator():
            f.write(chunk)
```

### Using Generators for Lazy Evaluation

```python
from typing import Generator

def generate_rows(filepath: str) -> Generator[dict, None, None]:
    """Lazily yield rows from a CSV file."""
    import csv
    with open(filepath, "r", encoding="utf-8", newline="") as f:
        reader = csv.DictReader(f)
        for row in reader:
            yield row

def filter_rows(rows, predicate):
    """Lazy filter — does not materialize rows."""
    return (row for row in rows if predicate(row))

def transform_rows(rows, transform_fn):
    """Lazy transform."""
    return (transform_fn(row) for row in rows)

# Pipeline is lazy — only one row is in memory at a time
rows      = generate_rows("transactions.csv")
filtered  = filter_rows(rows, lambda r: float(r["amount"]) > 100)
converted = transform_rows(filtered, lambda r: {**r, "amount": float(r["amount"])})

# Only materializes when consumed
for record in converted:
    write_to_db(record)
```

### Memory-Mapped Files (`mmap`)

`mmap` maps a file directly into memory — the OS handles paging. Ideal for random access into large binary or text files.

```python
import mmap

# Read-only mmap
with open("large_file.bin", "rb") as f:
    with mmap.mmap(f.fileno(), length=0, access=mmap.ACCESS_READ) as mm:
        # Slice like bytes
        header = mm[:16]
        print(header.hex())

        # Seek to a specific offset
        mm.seek(1024 * 1024)   # Jump to 1MB offset
        data = mm.read(256)

        # Search inside a huge file without reading it all
        idx = mm.find(b"ERROR")
        if idx != -1:
            print(f"Found 'ERROR' at byte {idx}")

# Read/write mmap
with open("data.bin", "r+b") as f:
    with mmap.mmap(f.fileno(), length=0) as mm:
        mm[0:4] = b"NEWH"   # Overwrite bytes in place
```

### When to Use What

| Volume | Tool | Reason |
|--------|------|--------|
| < 100 MB | `csv`, `json`, `open()` | Simple, no dependencies |
| 100 MB – 5 GB | `pandas` (chunked), `polars` | Mature DataFrame APIs |
| 5 GB – 50 GB | `polars`, `dask`, `duckdb` | Parallelism, lazy eval |
| > 50 GB / distributed | `PySpark`, `Ray` | Cluster-scale distributed I/O |
| Random access on huge file | `mmap` | No full load needed |
| Columnar analytics | `pyarrow` + Parquet | Column pruning, predicate pushdown |

```python
# DuckDB: SQL on files without loading into memory
import duckdb

conn = duckdb.connect()
result = conn.execute("""
    SELECT region, SUM(amount) as total
    FROM read_csv_auto('transactions_20M.csv')
    WHERE date >= '2024-01-01'
    GROUP BY region
    ORDER BY total DESC
""").fetchdf()
print(result)
```

---

## 9. Performance Optimization Techniques

### I/O Buffering

```python
# Default buffer: typically 8KB (determined by io.DEFAULT_BUFFER_SIZE)
import io
print(io.DEFAULT_BUFFER_SIZE)  # 8192

# Larger buffer = fewer syscalls = faster for sequential reads/writes
BUFFER_SIZE = 1 * 1024 * 1024  # 1 MB

with open("huge.txt", "r", encoding="utf-8", buffering=BUFFER_SIZE) as f:
    for line in f:
        pass
```

### Using `mmap` for Fast Reads

```python
import mmap
import time

filepath = "large_log.txt"

# Method 1: Normal line-by-line
start = time.perf_counter()
count = 0
with open(filepath, "rb") as f:
    for line in f:
        if b"ERROR" in line:
            count += 1
t1 = time.perf_counter() - start

# Method 2: mmap + find (much faster for search operations)
start = time.perf_counter()
count2 = 0
with open(filepath, "rb") as f:
    with mmap.mmap(f.fileno(), 0, access=mmap.ACCESS_READ) as mm:
        pos = 0
        while (idx := mm.find(b"ERROR", pos)) != -1:
            count2 += 1
            pos = idx + 1
t2 = time.perf_counter() - start

print(f"Normal: {t1:.2f}s | mmap: {t2:.2f}s")
```

### Multiprocessing for Parallel File Processing

```python
import multiprocessing as mp
from pathlib import Path

def process_file(filepath: Path) -> dict:
    """Process one file — runs in a worker process."""
    count = 0
    with open(filepath, "r", encoding="utf-8") as f:
        for line in f:
            if "ERROR" in line:
                count += 1
    return {"file": filepath.name, "error_count": count}

def parallel_process(directory: str, workers: int = 4) -> list[dict]:
    files = list(Path(directory).rglob("*.log"))
    with mp.Pool(workers) as pool:
        results = pool.map(process_file, files)
    return results

if __name__ == "__main__":
    results = parallel_process("logs/", workers=mp.cpu_count())
    for r in results:
        print(r)
```

### Async File Handling with `aiofiles`

```python
# pip install aiofiles
import asyncio
import aiofiles

async def read_file_async(filepath: str) -> str:
    async with aiofiles.open(filepath, "r", encoding="utf-8") as f:
        return await f.read()

async def write_file_async(filepath: str, content: str) -> None:
    async with aiofiles.open(filepath, "w", encoding="utf-8") as f:
        await f.write(content)

async def process_files_async(files: list[str]) -> list[str]:
    """Read multiple files concurrently."""
    tasks = [read_file_async(fp) for fp in files]
    return await asyncio.gather(*tasks)

# Run
async def main():
    contents = await process_files_async(["a.txt", "b.txt", "c.txt"])
    for content in contents:
        print(len(content))

asyncio.run(main())
```

### Benchmarks: Methods for Reading a 1GB CSV

| Method | Time (approx.) | Memory Usage | Notes |
|--------|---------------|--------------|-------|
| `f.read()` | 3.5s | ~1.5× file size | Loads all into RAM |
| `for line in f` | 4.0s | ~1 line | Best for sequential processing |
| `mmap` + search | 1.2s | Paged by OS | Best for search/random access |
| `pandas.read_csv` | 5.0s | ~3× file size | Convenient but RAM-heavy |
| `pandas` chunked | 6.0s | Low | Slower but memory-safe |
| `polars.scan_csv` | 1.5s | Low | Lazy, multi-threaded |
| `duckdb` SQL | 1.0s | Low | Best for aggregation queries |
| `pyarrow` CSV | 2.0s | Low-Medium | Great for Parquet conversion |

> Times are illustrative on a typical modern laptop (SSD, 16GB RAM). Actual results vary.

---

## 10. Error Handling & Logging

### Try/Except Patterns

```python
import errno

def read_file_robust(filepath: str) -> str | None:
    try:
        with open(filepath, "r", encoding="utf-8") as f:
            return f.read()

    except FileNotFoundError:
        print(f"[ERROR] File does not exist: {filepath}")

    except PermissionError:
        print(f"[ERROR] No permission to read: {filepath}")

    except IsADirectoryError:
        print(f"[ERROR] Expected file, got directory: {filepath}")

    except UnicodeDecodeError as e:
        print(f"[ERROR] Encoding problem in {filepath}: {e}")

    except OSError as e:
        # Catch-all for OS-level errors (disk full, network fs errors, etc.)
        if e.errno == errno.ENOSPC:
            print("[ERROR] Disk is full!")
        else:
            print(f"[ERROR] OS error reading {filepath}: {e}")

    return None
```

### Custom Exceptions

```python
class FileHandlingError(Exception):
    """Base class for file handling errors."""
    pass

class FileTooLargeError(FileHandlingError):
    """Raised when a file exceeds the allowed size limit."""
    def __init__(self, filepath: str, size: int, limit: int):
        self.filepath = filepath
        self.size = size
        self.limit = limit
        super().__init__(
            f"File '{filepath}' is {size / 1e6:.1f} MB, limit is {limit / 1e6:.1f} MB"
        )

class UnsupportedFileTypeError(FileHandlingError):
    """Raised when a file type is not supported."""
    pass

MAX_SIZE = 500 * 1024 * 1024  # 500 MB

def validate_and_open(filepath: str):
    from pathlib import Path
    p = Path(filepath)

    if not p.exists():
        raise FileNotFoundError(f"Not found: {filepath}")

    if p.suffix not in {".csv", ".json", ".txt"}:
        raise UnsupportedFileTypeError(f"Unsupported type: {p.suffix}")

    size = p.stat().st_size
    if size > MAX_SIZE:
        raise FileTooLargeError(filepath, size, MAX_SIZE)

    return open(filepath, "r", encoding="utf-8")
```

### Logging Best Practices for File Operations

```python
import logging
import logging.handlers
from pathlib import Path

def setup_logger(name: str, log_file: str, level=logging.INFO) -> logging.Logger:
    """Set up a rotating file logger."""
    logger = logging.getLogger(name)
    logger.setLevel(level)

    # Rotating file handler: max 10MB per file, keep 5 backups
    handler = logging.handlers.RotatingFileHandler(
        log_file,
        maxBytes=10 * 1024 * 1024,
        backupCount=5,
        encoding="utf-8",
    )
    formatter = logging.Formatter(
        "%(asctime)s | %(levelname)-8s | %(name)s | %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
    )
    handler.setFormatter(formatter)
    logger.addHandler(handler)

    # Also log to console
    console = logging.StreamHandler()
    console.setFormatter(formatter)
    logger.addHandler(console)

    return logger

logger = setup_logger("file_processor", "logs/app.log")

def process_with_logging(filepath: str) -> None:
    logger.info(f"Starting processing: {filepath}")
    try:
        size = Path(filepath).stat().st_size
        logger.info(f"File size: {size / 1e6:.2f} MB")
        with open(filepath, "r", encoding="utf-8") as f:
            for i, line in enumerate(f, 1):
                pass  # process line
        logger.info(f"Finished. Processed {i:,} lines.")
    except Exception as e:
        logger.exception(f"Failed processing {filepath}: {e}")
        raise
```

---

## 11. Real-World Data Engineering Examples

### Example 1: Processing 20M+ Row CSV Using Chunks

```python
import csv
import logging
from pathlib import Path

logger = logging.getLogger(__name__)

def process_large_transactions(
    input_path: str,
    output_path: str,
    chunk_size: int = 50_000,
) -> dict:
    """
    Process a 20M row transactions CSV:
    - Filter: amount > 0
    - Transform: add tax column (18% GST)
    - Output: clean CSV
    """
    stats = {"total": 0, "filtered_out": 0, "written": 0}
    first_chunk = True

    with open(input_path, "r", encoding="utf-8", newline="") as fin, \
         open(output_path, "w", encoding="utf-8", newline="") as fout:

        reader = csv.DictReader(fin)
        fieldnames = (reader.fieldnames or []) + ["tax_amount"]
        writer = csv.DictWriter(fout, fieldnames=fieldnames)
        writer.writeheader()

        chunk = []
        for row in reader:
            stats["total"] += 1
            amount = float(row.get("amount", 0))

            if amount <= 0:
                stats["filtered_out"] += 1
                continue

            row["tax_amount"] = round(amount * 0.18, 2)
            chunk.append(row)

            if len(chunk) >= chunk_size:
                writer.writerows(chunk)
                stats["written"] += len(chunk)
                logger.info(f"Written {stats['written']:,} rows so far...")
                chunk = []

        if chunk:
            writer.writerows(chunk)
            stats["written"] += len(chunk)

    logger.info(f"Done. Stats: {stats}")
    return stats

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    result = process_large_transactions(
        "transactions_20M.csv",
        "transactions_clean.csv",
        chunk_size=100_000,
    )
    print(result)
```

### Example 2: Converting Large CSV → Parquet

```python
# pip install pyarrow pandas
import pyarrow as pa
import pyarrow.parquet as pq
import pyarrow.csv as pv
import logging

logger = logging.getLogger(__name__)

def csv_to_parquet(
    csv_path: str,
    parquet_path: str,
    chunk_size: int = 500_000,
    compression: str = "snappy",
) -> None:
    """
    Convert a large CSV file to Parquet format with Snappy compression.
    Parquet is columnar: much faster for analytics, ~3-10x smaller.
    """
    read_opts  = pv.ReadOptions(block_size=64 * 1024 * 1024)   # 64MB blocks
    parse_opts = pv.ParseOptions(delimiter=",")
    conv_opts  = pv.ConvertOptions(auto_dict_encode=True)       # categorical for low-cardinality cols

    writer = None
    total_rows = 0

    with pv.open_csv(csv_path, read_options=read_opts,
                     parse_options=parse_opts,
                     convert_options=conv_opts) as reader:
        for batch in reader:
            table = pa.Table.from_batches([batch])
            if writer is None:
                writer = pq.ParquetWriter(
                    parquet_path,
                    schema=table.schema,
                    compression=compression,
                )
            writer.write_table(table)
            total_rows += len(table)
            logger.info(f"Converted {total_rows:,} rows...")

    if writer:
        writer.close()

    logger.info(f"Saved Parquet: {parquet_path} | Rows: {total_rows:,}")

csv_to_parquet("sales_data.csv", "sales_data.parquet")
```

### Example 3: Streaming Logs with Rotating File Handler

```python
import logging
import logging.handlers
import time
import random

def create_rotating_logger(
    log_dir: str = "logs",
    max_bytes: int = 50 * 1024 * 1024,   # 50 MB per file
    backup_count: int = 10,
) -> logging.Logger:
    """Create a logger that writes to rotating files."""
    from pathlib import Path
    Path(log_dir).mkdir(parents=True, exist_ok=True)

    logger = logging.getLogger("app")
    logger.setLevel(logging.DEBUG)

    handler = logging.handlers.RotatingFileHandler(
        f"{log_dir}/app.log",
        maxBytes=max_bytes,
        backupCount=backup_count,
        encoding="utf-8",
    )
    handler.setFormatter(logging.Formatter(
        "%(asctime)s %(levelname)s %(module)s:%(lineno)d — %(message)s"
    ))
    logger.addHandler(handler)
    return logger

logger = create_rotating_logger()

# Simulate log-heavy application
events = ["INFO", "DEBUG", "WARNING", "ERROR"]
for i in range(100):
    level = random.choice(events)
    msg = f"Event {i}: transaction_id={random.randint(1000, 9999)}"
    getattr(logger, level.lower())(msg)
    time.sleep(0.01)
```

### Example 4: ETL-Style Transformation

```python
import csv
import json
import logging
from datetime import datetime
from pathlib import Path

logger = logging.getLogger(__name__)

def etl_pipeline(
    source_csv: str,
    lookup_json: str,
    output_csv: str,
) -> dict:
    """
    ETL pipeline:
    E — Extract from CSV
    T — Transform: enrich with JSON lookup, parse dates, standardize fields
    L — Load to clean output CSV
    """
    # Load lookup table (small enough to fit in memory)
    with open(lookup_json, "r", encoding="utf-8") as f:
        region_map: dict = json.load(f)

    stats = {"extracted": 0, "transformed": 0, "errors": 0}
    output_rows = []

    with open(source_csv, "r", encoding="utf-8", newline="") as f:
        reader = csv.DictReader(f)

        for row in reader:
            stats["extracted"] += 1
            try:
                # Transform
                transformed = {
                    "transaction_id": row["txn_id"].strip(),
                    "amount":         round(float(row["amount"]), 2),
                    "date":           datetime.strptime(row["date"], "%d/%m/%Y").strftime("%Y-%m-%d"),
                    "region":         region_map.get(row["region_code"], "UNKNOWN"),
                    "currency":       row.get("currency", "INR").upper(),
                    "processed_at":   datetime.utcnow().isoformat(),
                }
                output_rows.append(transformed)
                stats["transformed"] += 1

            except (ValueError, KeyError) as e:
                logger.warning(f"Row {stats['extracted']}: transform error — {e}")
                stats["errors"] += 1

    # Load
    if output_rows:
        with open(output_csv, "w", encoding="utf-8", newline="") as f:
            writer = csv.DictWriter(f, fieldnames=output_rows[0].keys())
            writer.writeheader()
            writer.writerows(output_rows)

    logger.info(f"ETL complete: {stats}")
    return stats
```

---

## 12. Security & Safety

### Safe File Deletion

```python
import os
import shutil
from pathlib import Path

# Safe delete (moves to trash on supported platforms)
# pip install send2trash
from send2trash import send2trash
send2trash("old_report.csv")   # Recoverable!

# Secure delete (overwrite before delete — for sensitive data)
def secure_delete(filepath: str, passes: int = 3) -> None:
    """Overwrite file contents before deleting."""
    p = Path(filepath)
    if not p.is_file():
        raise FileNotFoundError(filepath)
    size = p.stat().st_size
    with open(filepath, "r+b") as f:
        for _ in range(passes):
            f.seek(0)
            f.write(os.urandom(size))
            f.flush()
            os.fsync(f.fileno())
    os.remove(filepath)

# Delete a directory tree safely
shutil.rmtree("old_data/", ignore_errors=True)
```

### Avoiding Path Traversal Attacks

```python
from pathlib import Path

SAFE_BASE_DIR = Path("/data/uploads").resolve()

def safe_open(user_provided_filename: str):
    """Prevent path traversal: ensure file stays within allowed directory."""
    # Resolve to absolute path (handles ../, symlinks, etc.)
    requested = (SAFE_BASE_DIR / user_provided_filename).resolve()

    # Verify the resolved path is still inside our safe directory
    if not str(requested).startswith(str(SAFE_BASE_DIR)):
        raise PermissionError(
            f"Access denied: '{user_provided_filename}' escapes the allowed directory."
        )

    return open(requested, "r", encoding="utf-8")

# Examples
# safe_open("report.csv")           → OK
# safe_open("../../../etc/passwd")  → raises PermissionError
# safe_open("/etc/passwd")          → raises PermissionError
```

### Validating File Extensions

```python
from pathlib import Path

ALLOWED_EXTENSIONS = {".csv", ".json", ".txt", ".parquet"}
MAX_FILE_SIZE = 500 * 1024 * 1024  # 500 MB

def validate_upload(filepath: str) -> Path:
    """Validate file before processing."""
    p = Path(filepath)

    # 1. Check extension (case-insensitive)
    if p.suffix.lower() not in ALLOWED_EXTENSIONS:
        raise ValueError(
            f"Unsupported file type: '{p.suffix}'. "
            f"Allowed: {ALLOWED_EXTENSIONS}"
        )

    # 2. Check file exists and is actually a file (not a dir or symlink)
    if not p.is_file():
        raise FileNotFoundError(f"File not found: {filepath}")

    # 3. Check file size
    size = p.stat().st_size
    if size == 0:
        raise ValueError("File is empty.")
    if size > MAX_FILE_SIZE:
        raise ValueError(
            f"File too large: {size / 1e6:.1f} MB > {MAX_FILE_SIZE / 1e6:.0f} MB limit"
        )

    # 4. Check magic bytes (not just extension)
    with open(p, "rb") as f:
        magic = f.read(4)
    if p.suffix == ".parquet" and magic[:4] != b"PAR1":
        raise ValueError("File claims to be Parquet but magic bytes are wrong.")

    return p
```

### Permissions and Access Control

```python
import os
import stat
from pathlib import Path

# Check file permissions
def check_permissions(filepath: str) -> dict:
    p = Path(filepath)
    s = p.stat()
    mode = s.st_mode

    return {
        "owner_read":    bool(mode & stat.S_IRUSR),
        "owner_write":   bool(mode & stat.S_IWUSR),
        "owner_execute": bool(mode & stat.S_IXUSR),
        "group_read":    bool(mode & stat.S_IRGRP),
        "others_read":   bool(mode & stat.S_IROTH),
        "is_readable":   os.access(filepath, os.R_OK),
        "is_writable":   os.access(filepath, os.W_OK),
    }

# Set restrictive permissions on sensitive files (Unix/Linux/macOS)
def secure_file_permissions(filepath: str) -> None:
    """Set file to owner-read-only (600)."""
    os.chmod(filepath, stat.S_IRUSR | stat.S_IWUSR)  # rw-------

# Create a temp file safely
import tempfile

with tempfile.NamedTemporaryFile(
    mode="w",
    suffix=".csv",
    prefix="proc_",
    dir="/tmp",
    delete=True,       # Auto-delete on close
    encoding="utf-8",
) as tmp:
    tmp.write("id,value\n1,100\n")
    tmp_path = tmp.name
    print(f"Temp file: {tmp_path}")
# File is deleted here automatically
```

---

## 13. Best Practices Summary

### Do's and Don'ts

| ✅ Do | ❌ Don't |
|-------|---------|
| Always use `with` context manager | Manually call `open()` without `close()` |
| Specify `encoding="utf-8"` explicitly | Rely on OS-default encoding |
| Use `newline=""` for CSV files | Let the OS handle newlines in CSV (causes bugs) |
| Use `pathlib.Path` for path handling | Hardcode `/` or `\\` separators |
| Stream large files line by line | Load multi-GB files with `.read()` |
| Use `mode='x'` to fail-safe create | Use `'w'` when you don't want to overwrite |
| Validate file type and size before processing | Trust user-supplied filenames blindly |
| Resolve and validate paths against a base dir | Accept `../` in user-provided paths |
| Log errors with `logger.exception()` | Silently swallow exceptions |
| Use chunked reading for CSV > 100MB | Read entire large CSV into DataFrame at once |
| Use Parquet for analytical data at scale | Use CSV for multi-GB analytical datasets |
| Use `errors='replace'` for encoding issues | Let `UnicodeDecodeError` crash the pipeline |
| Set file permissions on sensitive output | Leave config/key files world-readable |
| Use temp files for intermediate results | Write directly to final path before validation |

### Checklist for Production-Ready File Handling

```
File Processing Production Checklist
======================================
[ ] Use 'with' context manager for all file operations
[ ] Explicitly set encoding (utf-8 or as required)
[ ] Set newline='' for all CSV reads/writes
[ ] Validate file existence before opening
[ ] Validate file extension against allowlist
[ ] Check file size before loading into memory
[ ] Prevent path traversal (resolve & check against base dir)
[ ] Handle all relevant exceptions (FileNotFoundError, PermissionError, UnicodeDecodeError)
[ ] Log start, progress, and completion of file operations
[ ] Use rotating log handlers in production
[ ] Stream / chunk large files (never .read() on > 50MB)
[ ] Use atomic writes (write to temp → rename) for critical files
[ ] Set restrictive file permissions on sensitive outputs
[ ] Clean up temp files (use tempfile.NamedTemporaryFile with delete=True)
[ ] Test with empty files, corrupted files, and encoding edge cases
```

#### Atomic Write Pattern (Critical for Production)

```python
import os
import tempfile
from pathlib import Path

def atomic_write(filepath: str, content: str, encoding: str = "utf-8") -> None:
    """
    Write to a temp file, then rename — guarantees no partial writes.
    If the process crashes mid-write, the original file is untouched.
    """
    target = Path(filepath)
    tmp_path = None
    try:
        # Write to temp file in same directory (ensures same filesystem)
        with tempfile.NamedTemporaryFile(
            mode="w",
            encoding=encoding,
            dir=target.parent,
            delete=False,
            suffix=".tmp",
        ) as tmp:
            tmp.write(content)
            tmp_path = tmp.name

        # Atomic rename (os.replace is atomic on POSIX)
        os.replace(tmp_path, filepath)
    except Exception:
        if tmp_path and Path(tmp_path).exists():
            os.remove(tmp_path)
        raise
```

---

## 14. Final Cheat Sheet

```
╔══════════════════════════════════════════════════════════════════════╗
║         PYTHON FILE HANDLING — ONE-PAGE CHEAT SHEET                ║
╠══════════════════════════════════════════════════════════════════════╣
║  OPEN MODES                                                          ║
║  'r'  read text (default)    'rb' read binary                       ║
║  'w'  write (truncate)       'wb' write binary                      ║
║  'a'  append                 'ab' append binary                     ║
║  'x'  create (fail if exists)'r+' read+write                        ║
╠══════════════════════════════════════════════════════════════════════╣
║  ALWAYS USE                                                          ║
║  with open(path, 'r', encoding='utf-8') as f:                      ║
║      ...                                                             ║
╠══════════════════════════════════════════════════════════════════════╣
║  READING                                                             ║
║  f.read()          → entire file as string (small files only)       ║
║  f.readline()      → one line                                        ║
║  f.readlines()     → list of all lines                              ║
║  for line in f:    → memory-efficient line iterator (preferred)     ║
╠══════════════════════════════════════════════════════════════════════╣
║  WRITING                                                             ║
║  f.write(str)      → write string                                   ║
║  f.writelines(lst) → write list (no auto-newline)                  ║
╠══════════════════════════════════════════════════════════════════════╣
║  PATHS (use pathlib!)                                                ║
║  Path("a") / "b" / "c.csv"  → cross-platform join                 ║
║  p.exists() p.is_file() p.is_dir()                                  ║
║  p.stem p.suffix p.name p.parent                                    ║
║  p.read_text() p.write_text() p.read_bytes()                        ║
║  p.glob("*.csv") p.rglob("*.log")                                   ║
║  Path.home() Path(tempfile.gettempdir())                            ║
╠══════════════════════════════════════════════════════════════════════╣
║  CSV                                                                 ║
║  csv.reader(f)                → list rows                           ║
║  csv.DictReader(f)            → dict rows                           ║
║  csv.writer(f)                → write rows                          ║
║  csv.DictWriter(f, fieldnames)→ write dict rows                     ║
║  Always: newline='' in open()                                        ║
╠══════════════════════════════════════════════════════════════════════╣
║  JSON                                                                ║
║  json.load(f)    json.loads(s)    → parse                           ║
║  json.dump(d,f)  json.dumps(d)    → serialize                       ║
║  json.dump(..., indent=4, ensure_ascii=False)  → pretty             ║
║  JSONL: one json.dumps(record)+'\n' per line                        ║
║  Large JSON: use ijson.items(f, 'key.item')                         ║
╠══════════════════════════════════════════════════════════════════════╣
║  LARGE FILE PATTERNS                                                 ║
║  • Stream line-by-line with 'for line in f'                         ║
║  • Use generators (yield) to stay lazy                              ║
║  • pandas.read_csv(path, chunksize=100_000)                        ║
║  • polars.scan_csv(path).filter(...).collect()                      ║
║  • duckdb.execute("SELECT ... FROM read_csv_auto('f.csv')")         ║
║  • mmap for random-access search on large files                     ║
╠══════════════════════════════════════════════════════════════════════╣
║  BINARY                                                              ║
║  open(path, 'rb'/'wb')                                              ║
║  struct.pack('<If', int_val, float_val)  → bytes                    ║
║  struct.unpack('<If', raw_bytes)          → values                  ║
║  mmap.mmap(f.fileno(), 0)                → memory-mapped access     ║
╠══════════════════════════════════════════════════════════════════════╣
║  ERROR HANDLING                                                      ║
║  FileNotFoundError  PermissionError  IsADirectoryError              ║
║  UnicodeDecodeError  OSError                                         ║
║  errors='replace' | 'ignore' | 'backslashreplace'                  ║
╠══════════════════════════════════════════════════════════════════════╣
║  LOGGING                                                             ║
║  RotatingFileHandler(path, maxBytes=10MB, backupCount=5)            ║
║  logger.info / .warning / .error / .exception(msg)                 ║
╠══════════════════════════════════════════════════════════════════════╣
║  SECURITY                                                            ║
║  • Resolve paths: (BASE / user_input).resolve()                     ║
║  • Check: resolved.startswith(str(BASE))                            ║
║  • Validate extension against allowlist                             ║
║  • Check magic bytes, not just extension                            ║
║  • Atomic write: temp file → os.replace(tmp, target)               ║
║  • Restrict permissions: os.chmod(path, stat.S_IRUSR|stat.S_IWUSR) ║
╠══════════════════════════════════════════════════════════════════════╣
║  PERFORMANCE                                                         ║
║  Small  (<100MB)  : csv, open(), json                               ║
║  Medium (100MB–5G): pandas chunked, polars                          ║
║  Large  (5G–50G)  : polars, dask, duckdb                           ║
║  Huge   (>50G)    : PySpark, Ray                                    ║
║  Search in big file: mmap + find()                                  ║
║  Parallel: multiprocessing.Pool.map()                               ║
║  Async I/O: aiofiles + asyncio.gather()                             ║
╚══════════════════════════════════════════════════════════════════════╝
```

---

*Guide version: 1.0 | Python 3.8+ | Last updated: 2025*

> **Next Steps:**
> - Practice: Build a local log parser that reads `.log` files and outputs an error summary CSV.
> - Explore: Try converting a 1GB CSV to Parquet with PyArrow and compare query speed with DuckDB.
> - Advanced: Set up an async file processor using `aiofiles` and benchmark it against synchronous I/O.