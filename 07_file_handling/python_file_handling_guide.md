# Python File Handling — From Basics to Advanced (Complete Guide)

## 1. Introduction

### What is file handling?
File handling is the process of creating, reading, updating, and deleting files from Python. It is one of the most common tasks in automation, data processing, ETL pipelines, logging, and application development.

### Why it matters in real-world systems
Almost every production system touches files somewhere:

- Applications read configuration files.
- APIs store exports and archives.
- Data pipelines ingest CSV, JSON, logs, images, and parquet-like artifacts.
- Batch jobs process millions of rows from disk.
- Monitoring systems write logs continuously.

A solid file-handling foundation helps you write code that is:
- reliable
- memory-efficient
- cross-platform
- safe in production

### Types of files
| File type | Typical use | Python approach |
|---|---|---|
| Text files | notes, configs, scripts, logs | `open(..., encoding="utf-8")` |
| Binary files | images, PDFs, archives, custom formats | `open(..., "rb")` / `open(..., "wb")` |
| CSV files | tabular data exchange | `csv` module, streaming, chunks |
| JSON files | APIs, config, nested data | `json` module, streaming parsers |
| Log files | application observability | line-by-line reading, rotation |
| Large datasets | ETL, analytics, reporting | generators, chunking, columnar tools |

### File handling flow
```text
+-------------------+
|  File on disk     |
+---------+---------+
          |
          v
+-------------------+
| open()            |
+---------+---------+
          |
          v
+-------------------+
| read / write      |
+---------+---------+
          |
          v
+-------------------+
| flush / close     |
+-------------------+
```

### Simple example
```python
from pathlib import Path

path = Path("example.txt")
path.write_text("Hello, file handling!", encoding="utf-8")

text = path.read_text(encoding="utf-8")
print(text)
```

---

## 2. Basics of File Handling

### Opening files: `open()`, modes, encoding
The built-in `open()` function returns a file object.

```python
f = open("sample.txt", "r", encoding="utf-8")
try:
    data = f.read()
    print(data)
finally:
    f.close()
```

Common modes:

| Mode | Meaning |
|---|---|
| `"r"` | read text file |
| `"w"` | write text file, overwrite if exists |
| `"a"` | append text file |
| `"x"` | create new file, fail if exists |
| `"b"` | binary mode |
| `"t"` | text mode (default) |
| `"+"` | update mode (read and write) |

Examples:
```python
open("data.txt", "r", encoding="utf-8")
open("data.txt", "w", encoding="utf-8")
open("data.txt", "a", encoding="utf-8")
open("image.png", "rb")
open("output.bin", "wb")
```

### Reading files: `read()`, `readline()`, `readlines()`
```python
with open("sample.txt", "r", encoding="utf-8") as f:
    all_text = f.read()
    print(all_text)
```

```python
with open("sample.txt", "r", encoding="utf-8") as f:
    first_line = f.readline()
    print(first_line)
```

```python
with open("sample.txt", "r", encoding="utf-8") as f:
    lines = f.readlines()
    print(lines)
```

#### When to use what
| Method | Best for | Risk |
|---|---|---|
| `read()` | small files | high memory use on large files |
| `readline()` | one line at a time | slower for loops if overused |
| `readlines()` | small files when you need a list | loads everything into memory |

### Writing and appending
```python
with open("output.txt", "w", encoding="utf-8") as f:
    f.write("first line\n")
    f.write("second line\n")
```

```python
with open("output.txt", "a", encoding="utf-8") as f:
    f.write("new line appended\n")
```

### Using `with` context manager
Always prefer `with` because it closes the file automatically.

```python
with open("sample.txt", "r", encoding="utf-8") as f:
    print(f.read())
```

This is equivalent to:
```python
f = open("sample.txt", "r", encoding="utf-8")
try:
    print(f.read())
finally:
    f.close()
```

### Common pitfalls and how to avoid them
| Pitfall | Problem | Safer approach |
|---|---|---|
| Forgetting to close files | resource leak | use `with` |
| Using wrong encoding | Unicode errors | specify `encoding="utf-8"` |
| Reading huge files with `read()` | memory spikes | iterate line by line |
| Writing to text file in binary mode | type errors | match mode to content |
| Assuming `\n` works everywhere | cross-platform issues | let Python handle text mode or use `Path` |

### Example: safe read
```python
from pathlib import Path

path = Path("sample.txt")

if path.exists():
    with path.open("r", encoding="utf-8") as f:
        for line in f:
            print(line.rstrip("\n"))
else:
    print("File does not exist.")
```

---

## 3. Working with Paths

### `os` module basics
The `os` module gives low-level path and filesystem helpers.

```python
import os

print(os.getcwd())
print(os.listdir("."))
print(os.path.exists("sample.txt"))
print(os.path.join("data", "input.csv"))
```

### `pathlib` best practices
Modern Python code should usually prefer `pathlib.Path`.

```python
from pathlib import Path

path = Path("data") / "input.csv"
print(path)
print(path.exists())
print(path.name)
print(path.suffix)
print(path.parent)
```

### Cross-platform path handling
Avoid hardcoding separators like `/` or `\`.

Wrong:
```python
path = "data\\input.csv"
```

Better:
```python
from pathlib import Path

path = Path("data") / "input.csv"
```

### Real-world example
```python
from pathlib import Path

base_dir = Path("/tmp") if Path("/tmp").exists() else Path(".")
logs_dir = base_dir / "logs"
logs_dir.mkdir(parents=True, exist_ok=True)

log_file = logs_dir / "app.log"
log_file.write_text("application started\n", encoding="utf-8")
print(log_file.resolve())
```

### Useful `Path` methods
| Method | Example | Meaning |
|---|---|---|
| `exists()` | `path.exists()` | file or folder exists |
| `is_file()` | `path.is_file()` | is a regular file |
| `is_dir()` | `path.is_dir()` | is a directory |
| `mkdir()` | `path.mkdir()` | create directory |
| `glob()` | `path.glob("*.csv")` | find matching files |
| `resolve()` | `path.resolve()` | absolute path |

---

## 4. Reading & Writing Text Files

### Line-by-line processing
This is the standard pattern for large text files.

```python
from pathlib import Path

path = Path("input.txt")

with path.open("r", encoding="utf-8") as f:
    for line in f:
        print(line.rstrip())
```

### Efficient iteration
Iterating over the file object is memory-friendly.

```python
with open("large_log.txt", "r", encoding="utf-8") as f:
    for line in f:
        if "ERROR" in line:
            print(line.rstrip())
```

### Handling encodings
Text files are bytes plus an encoding. UTF-8 is the default safe choice for modern systems.

```python
# UTF-8
with open("data_utf8.txt", "r", encoding="utf-8") as f:
    print(f.read())
```

Some legacy files may use ISO-8859-1.

```python
with open("legacy.txt", "r", encoding="iso-8859-1") as f:
    print(f.read())
```

### Encoding errors
You can control decode failures.

```python
with open("legacy.txt", "r", encoding="utf-8", errors="replace") as f:
    text = f.read()
    print(text)
```

Common `errors` options:
- `"strict"`: default, raises an exception
- `"replace"`: substitutes invalid bytes
- `"ignore"`: skips invalid bytes

### Error handling strategies
```python
from pathlib import Path

path = Path("input.txt")

try:
    with path.open("r", encoding="utf-8") as f:
        for line in f:
            print(line.rstrip())
except FileNotFoundError:
    print(f"{path} was not found")
except UnicodeDecodeError as exc:
    print(f"Encoding problem: {exc}")
except OSError as exc:
    print(f"Filesystem error: {exc}")
```

### Writing text safely
```python
from pathlib import Path

path = Path("report.txt")

lines = [
    "Daily report",
    "================",
    "All systems healthy.",
]

with path.open("w", encoding="utf-8", newline="\n") as f:
    for line in lines:
        f.write(line + "\n")
```

### Practical log filtering example
```python
from pathlib import Path

source = Path("app.log")
target = Path("errors_only.log")

with source.open("r", encoding="utf-8") as src, target.open("w", encoding="utf-8") as dst:
    for line in src:
        if "ERROR" in line or "CRITICAL" in line:
            dst.write(line)
```

---

## 5. Binary File Handling

### Reading/writing binary data
Binary files must be handled with `"rb"` and `"wb"`.

```python
from pathlib import Path

source = Path("image.png")
data = source.read_bytes()

copy_path = Path("image_copy.png")
copy_path.write_bytes(data)
```

### Working with images, PDFs, custom binary formats
Binary mode is appropriate when you do not want Python to decode bytes as text.

```python
with open("document.pdf", "rb") as f:
    header = f.read(8)
    print(header)
```

### Example: byte copy
```python
from pathlib import Path

src = Path("source.bin")
dst = Path("target.bin")

with src.open("rb") as fsrc, dst.open("wb") as fdst:
    while chunk := fsrc.read(1024 * 1024):
        fdst.write(chunk)
```

### Using `struct` for packed data
`struct` is useful for fixed-format binary records.

```python
import struct

# Format: int, float, 4-byte string
packed = struct.pack("if4s", 7, 3.14, b"ABCD")
print(packed)

unpacked = struct.unpack("if4s", packed)
print(unpacked)
```

### Example: binary record parser
```python
import struct
from pathlib import Path

record_format = "I f"
record_size = struct.calcsize(record_format)

path = Path("records.bin")

with path.open("rb") as f:
    while chunk := f.read(record_size):
        if len(chunk) != record_size:
            break
        record_id, value = struct.unpack(record_format, chunk)
        print(record_id, value)
```

### Binary file handling checklist
| Check | Why it matters |
|---|---|
| Use `"rb"` / `"wb"` | prevents text decoding issues |
| Read in chunks | avoids memory spikes |
| Know the format | binary data is not self-describing |
| Use `struct` carefully | pack/unpack must match exactly |

---

## 6. CSV File Handling (Beginner → Advanced)

### Using Python `csv` module
The standard library `csv` module is reliable for CSV work.

```python
import csv

with open("people.csv", "r", encoding="utf-8", newline="") as f:
    reader = csv.reader(f)
    for row in reader:
        print(row)
```

### `DictReader` and `DictWriter`
```python
import csv

with open("people.csv", "r", encoding="utf-8", newline="") as f:
    reader = csv.DictReader(f)
    for row in reader:
        print(row["name"], row["city"])
```

```python
import csv

rows = [
    {"name": "Asha", "city": "Chennai"},
    {"name": "Ravi", "city": "Bengaluru"},
]

with open("output.csv", "w", encoding="utf-8", newline="") as f:
    writer = csv.DictWriter(f, fieldnames=["name", "city"])
    writer.writeheader()
    writer.writerows(rows)
```

### Dialects, quoting, delimiters
CSV files are not always comma-separated.

```python
import csv

with open("data.tsv", "r", encoding="utf-8", newline="") as f:
    reader = csv.reader(f, delimiter="\t")
    for row in reader:
        print(row)
```

Quoting example:
```python
import csv

with open("quoted.csv", "w", encoding="utf-8", newline="") as f:
    writer = csv.writer(f, quoting=csv.QUOTE_MINIMAL)
    writer.writerow(["name", "note"])
    writer.writerow(["Asha", 'He said "hello"'])
```

### Streaming large CSVs
Do not load the whole file unless necessary.

```python
import csv
from pathlib import Path

path = Path("large.csv")

with path.open("r", encoding="utf-8", newline="") as f:
    reader = csv.DictReader(f)
    for row in reader:
        if row["status"] == "active":
            print(row["id"])
```

### Writing clean CSV output
```python
import csv
from pathlib import Path

input_path = Path("input.csv")
output_path = Path("cleaned.csv")

with input_path.open("r", encoding="utf-8", newline="") as src, \
     output_path.open("w", encoding="utf-8", newline="") as dst:
    reader = csv.DictReader(src)
    writer = csv.DictWriter(dst, fieldnames=["id", "name", "status"])
    writer.writeheader()

    for row in reader:
        writer.writerow({
            "id": row["id"].strip(),
            "name": row["name"].strip(),
            "status": row["status"].strip().lower(),
        })
```

### CSV comparison table
| Tool | Best for | Strengths | Weaknesses |
|---|---|---|---|
| `csv` module | standard CSV I/O | built-in, lightweight, streaming-friendly | limited data validation and analytics features |
| `pandas` | analysis, transformations | rich API, easy tabular work | memory-heavy on very large files |
| `pyarrow` | columnar analytics, Parquet | fast, efficient, strong Arrow ecosystem | extra dependency, steeper learning curve |
| `polars` | fast dataframe processing | very fast, expressive, can be lazy | not built into Python, learning curve |

### Example: pandas CSV read
```python
import pandas as pd

df = pd.read_csv("people.csv")
print(df.head())
```

### Example: pyarrow CSV read
```python
import pyarrow.csv as pv

table = pv.read_csv("people.csv")
print(table.schema)
```

### Example: polars CSV read
```python
import polars as pl

df = pl.read_csv("people.csv")
print(df.head())
```

---

## 7. JSON File Handling

### `json` module basics
```python
import json

data = {"name": "Asha", "age": 28, "city": "Chennai"}

text = json.dumps(data)
print(text)

parsed = json.loads(text)
print(parsed["name"])
```

### Reading and writing JSON files
```python
import json
from pathlib import Path

path = Path("config.json")
data = {"env": "prod", "debug": False}

with path.open("w", encoding="utf-8") as f:
    json.dump(data, f, indent=2, ensure_ascii=False)
```

```python
import json
from pathlib import Path

path = Path("config.json")

with path.open("r", encoding="utf-8") as f:
    data = json.load(f)

print(data)
```

### Pretty printing
```python
import json

data = {"a": 1, "b": {"c": 2}}
print(json.dumps(data, indent=4, sort_keys=True, ensure_ascii=False))
```

### Streaming JSON (`ijson`)
For very large JSON arrays, streaming is safer than `json.load()`.

```python
# pip install ijson
import ijson
from pathlib import Path

path = Path("large.json")

with path.open("rb") as f:
    for item in ijson.items(f, "item"):
        print(item)
```

### Handling large JSON safely
If the file is too large for memory:
- avoid `json.load()` on the whole file
- process line-delimited JSON if possible
- use streaming parsers
- validate schema incrementally

### Example: JSON Lines (`.jsonl`)
Each line is one JSON object.

```python
import json
from pathlib import Path

path = Path("events.jsonl")

with path.open("r", encoding="utf-8") as f:
    for line in f:
        event = json.loads(line)
        print(event["event_type"])
```

### JSON formats table
| Format | Good for | Notes |
|---|---|---|
| Standard JSON | config, APIs | entire structure loaded as one object |
| JSON Lines | logs, events, streams | one object per line |
| Nested JSON | hierarchical data | may require flattening for analytics |

---

## 8. Handling Large Files (Millions of Rows)

### Memory-efficient patterns
The main rule is simple: process data as a stream.

Bad:
```python
with open("big.txt", "r", encoding="utf-8") as f:
    data = f.read()   # may consume too much memory
```

Better:
```python
with open("big.txt", "r", encoding="utf-8") as f:
    for line in f:
        process = line.strip()
```

### Chunked reading
```python
from pathlib import Path

def read_in_chunks(path: Path, chunk_size: int = 1024 * 1024):
    with path.open("rb") as f:
        while chunk := f.read(chunk_size):
            yield chunk

for chunk in read_in_chunks(Path("large.bin")):
    print(len(chunk))
```

### Buffered I/O
Python already buffers file I/O, but explicit chunking helps for huge data.

```python
from pathlib import Path

path = Path("large.log")

with path.open("r", encoding="utf-8") as f:
    for line in f:
        if "WARN" in line:
            print(line.rstrip())
```

### Using generators
Generators keep memory use low.

```python
def valid_rows(path):
    with open(path, "r", encoding="utf-8") as f:
        for line in f:
            if line.strip():
                yield line.rstrip("\n")

for row in valid_rows("input.txt"):
    print(row)
```

### Lazy evaluation
```python
numbers = (x * x for x in range(10))
print(next(numbers))
print(next(numbers))
```

### When to use `mmap`
`mmap` is useful for fast, random-access reading of large files.

```python
import mmap
from pathlib import Path

path = Path("large.txt")

with path.open("r+b") as f:
    mm = mmap.mmap(f.fileno(), 0)
    try:
        print(mm[:100])
    finally:
        mm.close()
```

### When to use PySpark, Dask, Polars, DuckDB
| Tool | Use when | Best fit |
|---|---|---|
| PySpark | data is distributed, very large, cluster available | enterprise ETL, lakehouse pipelines |
| Dask | pandas-like parallel processing | medium to large local/distributed workloads |
| Polars | fast single-node analytics | large CSV/Parquet on one machine |
| DuckDB | SQL on local files | fast ad hoc analytics on CSV/Parquet |

### Chunked processing flow
```text
+-------------------+
| Large input file  |
+---------+---------+
          |
          v
+-------------------+
| Read chunk/row    |
+---------+---------+
          |
          v
+-------------------+
| Transform        |
+---------+---------+
          |
          v
+-------------------+
| Write output     |
+-------------------+
```

### Example: chunked CSV processing
```python
import csv
from pathlib import Path

def process_large_csv(input_path: Path, output_path: Path, chunk_size: int = 100_000):
    with input_path.open("r", encoding="utf-8", newline="") as src, \
         output_path.open("w", encoding="utf-8", newline="") as dst:
        reader = csv.DictReader(src)
        fieldnames = reader.fieldnames or []
        writer = csv.DictWriter(dst, fieldnames=fieldnames)
        writer.writeheader()

        buffer = []
        for row in reader:
            row["status"] = row["status"].strip().lower()
            buffer.append(row)

            if len(buffer) >= chunk_size:
                writer.writerows(buffer)
                buffer.clear()

        if buffer:
            writer.writerows(buffer)

process_large_csv(Path("input.csv"), Path("output.csv"))
```

---

## 9. Performance Optimization Techniques

### I/O buffering
File objects are buffered by default. Chunking and streaming are often enough.

```python
with open("big.txt", "r", encoding="utf-8", buffering=1024 * 1024) as f:
    for line in f:
        pass
```

### Avoid `.read()` on large files
```python
# Avoid this for huge files
text = open("big.txt", "r", encoding="utf-8").read()
```

Prefer:
```python
with open("big.txt", "r", encoding="utf-8") as f:
    for line in f:
        ...
```

### Using `mmap` for fast reads
```python
import mmap

with open("big.txt", "r+b") as f:
    mm = mmap.mmap(f.fileno(), 0)
    try:
        print(mm.find(b"ERROR"))
    finally:
        mm.close()
```

### Multiprocessing for parallel file processing
Good for CPU-heavy transformations or many independent files.

```python
from concurrent.futures import ProcessPoolExecutor
from pathlib import Path

def count_lines(path_str: str) -> tuple[str, int]:
    path = Path(path_str)
    with path.open("r", encoding="utf-8") as f:
        return path.name, sum(1 for _ in f)

files = ["a.txt", "b.txt", "c.txt"]

with ProcessPoolExecutor() as executor:
    for name, count in executor.map(count_lines, files):
        print(name, count)
```

### Async file handling with `aiofiles`
Async file I/O can help when your program also does network I/O, but regular disk I/O is often simpler and fast enough.

```python
# pip install aiofiles
import asyncio
import aiofiles

async def read_file(path: str):
    async with aiofiles.open(path, "r", encoding="utf-8") as f:
        async for line in f:
            print(line.rstrip())

asyncio.run(read_file("sample.txt"))
```

### Benchmarks table
Actual performance depends on disk, OS cache, file size, and workload. Use this as a rule-of-thumb.

| Method | Small files | Large files | Random access | Parallel use |
|---|---|---|---|---|
| `read()` | fast | poor | no | no |
| line iteration | good | very good | no | moderate |
| chunked reads | good | very good | no | moderate |
| `mmap` | good | very good | yes | moderate |
| `aiofiles` | good | good | no | useful with async apps |
| multiprocessing | overhead for tiny files | useful for CPU-heavy workloads | no | yes |

### Microbenchmark example
```python
import time
from pathlib import Path

path = Path("big.txt")

start = time.perf_counter()
with path.open("r", encoding="utf-8") as f:
    for _ in f:
        pass
elapsed = time.perf_counter() - start

print(f"Line iteration took {elapsed:.4f} seconds")
```

---

## 10. Error Handling & Logging

### Try/except patterns
```python
from pathlib import Path

path = Path("input.csv")

try:
    with path.open("r", encoding="utf-8") as f:
        print(f.readline())
except FileNotFoundError:
    print("File missing")
except PermissionError:
    print("No permission to read file")
except OSError as exc:
    print(f"Filesystem problem: {exc}")
```

### Custom exceptions
```python
class InvalidDataFileError(Exception):
    pass

def load_file(path):
    if not path.endswith(".csv"):
        raise InvalidDataFileError("Only .csv files are allowed")
```

### Logging best practices for file operations
Use the `logging` module instead of `print()` in production code.

```python
import logging
from pathlib import Path

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s %(levelname)s %(message)s"
)

logger = logging.getLogger(__name__)

path = Path("input.txt")

try:
    with path.open("r", encoding="utf-8") as f:
        logger.info("Opened file %s", path)
        data = f.read()
        logger.info("Read %d characters", len(data))
except Exception:
    logger.exception("Failed to process file %s", path)
```

### Structured logging example
```python
import logging

logger = logging.getLogger("file_processor")
logger.info("processing_started", extra={"file": "input.csv"})
```

---

## 11. Real-World Data Engineering Examples

### Processing 20M+ row CSV using chunks
This pattern reduces memory pressure.

```python
import csv
from pathlib import Path

def transform_row(row: dict) -> dict:
    return {
        "user_id": row["user_id"].strip(),
        "country": row["country"].strip().upper(),
        "amount": row["amount"].strip(),
    }

def process_csv_in_chunks(input_path: Path, output_path: Path, chunk_size: int = 100_000):
    with input_path.open("r", encoding="utf-8", newline="") as src, \
         output_path.open("w", encoding="utf-8", newline="") as dst:
        reader = csv.DictReader(src)
        fieldnames = ["user_id", "country", "amount"]
        writer = csv.DictWriter(dst, fieldnames=fieldnames)
        writer.writeheader()

        buffer = []
        for row in reader:
            buffer.append(transform_row(row))
            if len(buffer) >= chunk_size:
                writer.writerows(buffer)
                buffer.clear()

        if buffer:
            writer.writerows(buffer)

process_csv_in_chunks(Path("transactions.csv"), Path("transactions_clean.csv"))
```

### Converting large CSV → Parquet
Using `pyarrow`:

```python
# pip install pyarrow
import pyarrow as pa
import pyarrow.csv as pv
import pyarrow.parquet as pq

table = pv.read_csv("input.csv")
pq.write_table(table, "output.parquet")
```

For very large files, process in batches instead of loading everything at once.

```python
import pyarrow.csv as pv
import pyarrow.parquet as pq

reader = pv.open_csv("input.csv")
writer = None

for batch in reader:
    if writer is None:
        writer = pq.ParquetWriter("output.parquet", batch.schema)
    writer.write_table(pa.Table.from_batches([batch]))

if writer:
    writer.close()
```

### Streaming logs and writing rotated files
```python
from pathlib import Path

source = Path("app.log")
error_file = Path("app_errors.log")
warn_file = Path("app_warnings.log")

with source.open("r", encoding="utf-8") as src, \
     error_file.open("w", encoding="utf-8") as err, \
     warn_file.open("w", encoding="utf-8") as warn:
    for line in src:
        if "ERROR" in line:
            err.write(line)
        elif "WARN" in line:
            warn.write(line)
```

### ETL-style transformation example
```python
import csv
from pathlib import Path

def normalize_name(value: str) -> str:
    return " ".join(value.strip().title().split())

def etl(input_path: Path, output_path: Path):
    with input_path.open("r", encoding="utf-8", newline="") as src, \
         output_path.open("w", encoding="utf-8", newline="") as dst:
        reader = csv.DictReader(src)
        writer = csv.DictWriter(dst, fieldnames=["id", "name", "email"])
        writer.writeheader()

        for row in reader:
            writer.writerow({
                "id": row["id"].strip(),
                "name": normalize_name(row["name"]),
                "email": row["email"].strip().lower(),
            })

etl(Path("raw_users.csv"), Path("clean_users.csv"))
```

---

## 12. Security & Safety

### Safe file deletion
Only delete files after checking the path.

```python
from pathlib import Path

path = Path("old_output.tmp")

if path.exists() and path.is_file():
    path.unlink()
```

### Avoiding path traversal attacks
Never trust raw user input for file paths.

Unsafe:
```python
from pathlib import Path

base = Path("/safe/base")
user_input = "../../etc/passwd"
target = base / user_input
```

Safer:
```python
from pathlib import Path

base = Path("/safe/base").resolve()
user_input = "reports/output.csv"

target = (base / user_input).resolve()
if base in target.parents or target == base:
    print("Safe path")
else:
    raise ValueError("Path traversal detected")
```

### Validating file extensions
```python
from pathlib import Path

allowed = {".csv", ".json", ".txt"}

path = Path("input.csv")
if path.suffix.lower() not in allowed:
    raise ValueError("Unsupported file type")
```

### Permissions and access control
```python
from pathlib import Path
import os

path = Path("secret.txt")

# Read-only check is platform dependent, but you can inspect permissions.
print(os.stat(path))
```

### Safety rules
| Rule | Why |
|---|---|
| Validate file names and paths | prevents unintended access |
| Restrict allowed extensions | avoids dangerous uploads |
| Use least privilege | limits damage if compromised |
| Avoid executing file contents blindly | prevents code injection |
| Log access appropriately | supports audits |

---

## 13. Best Practices Summary

### Do’s and Don’ts table
| Do | Don’t |
|---|---|
| Use `with open(...)` | leave files unclosed |
| Prefer `pathlib.Path` | hardcode path separators |
| Stream large files | call `.read()` on multi-GB files |
| Set explicit encodings | rely on platform defaults |
| Use `csv.DictReader` for named columns | parse CSV manually with `split(",")` |
| Validate user-controlled paths | trust external input blindly |
| Log failures with context | swallow exceptions silently |

### Checklist for production-ready file handling
- [ ] Correct file mode used (`r`, `w`, `a`, `rb`, `wb`)
- [ ] Encoding explicitly set for text files
- [ ] `with` used for automatic closing
- [ ] Large files processed in streaming/chunks
- [ ] Exceptions handled with meaningful messages
- [ ] Logging added for observability
- [ ] Paths validated and normalized
- [ ] Output format verified
- [ ] Temporary files cleaned up safely
- [ ] Performance tested with realistic data size

### Production-ready template
```python
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def process_file(input_path: Path, output_path: Path) -> None:
    try:
        with input_path.open("r", encoding="utf-8") as src, \
             output_path.open("w", encoding="utf-8") as dst:
            for line in src:
                dst.write(line.upper())
        logger.info("Processed %s -> %s", input_path, output_path)
    except FileNotFoundError:
        logger.error("Missing file: %s", input_path)
        raise
    except Exception:
        logger.exception("Unexpected failure")
        raise

process_file(Path("input.txt"), Path("output.txt"))
```

---

## 14. Final Cheat Sheet

### One-page summary
| Task | Best pattern |
|---|---|
| Read small text file | `Path.read_text(encoding="utf-8")` |
| Read large text file | `for line in f:` |
| Write text file | `with open(..., "w", encoding="utf-8")` |
| Append text | `open(..., "a", encoding="utf-8")` |
| Read binary file | `open(..., "rb")` |
| Copy binary file | chunked `read()` / `write()` |
| Parse CSV | `csv.DictReader` |
| Write CSV | `csv.DictWriter` |
| Parse JSON | `json.load()` / `json.loads()` |
| Large JSON | streaming parser such as `ijson` |
| Faster random access | `mmap` |
| Parallel file jobs | `ProcessPoolExecutor` |
| Async file I/O | `aiofiles` |
| Cross-platform paths | `pathlib.Path` |

### Common commands
```python
from pathlib import Path

p = Path("data") / "input.csv"
print(p.exists())
print(p.suffix)
print(p.parent)

text = p.read_text(encoding="utf-8")
p.write_text("hello\n", encoding="utf-8")

with p.open("r", encoding="utf-8") as f:
    for line in f:
        print(line.rstrip())
```

### Final mental model
```text
Text files  -> decode bytes to str using encoding
Binary files-> keep raw bytes
CSV files   -> stream rows
JSON files  -> parse structure
Large files -> never assume memory is enough
Paths       -> use pathlib
Safety      -> validate everything from outside
```

### Closing example
```python
from pathlib import Path
import csv
import json

base = Path("data")
csv_path = base / "input.csv"
json_path = base / "output.json"

rows = []

with csv_path.open("r", encoding="utf-8", newline="") as f:
    reader = csv.DictReader(f)
    for row in reader:
        rows.append(row)

with json_path.open("w", encoding="utf-8") as f:
    json.dump(rows, f, indent=2, ensure_ascii=False)
```

---

### End of guide
This document is suitable to save as `python_file_handling_guide.md`.
