# CIDR to IP Converter

Welcome to the **CIDR to IP Converter** script! This tool allows you to easily convert CIDR notation into a list of IP addresses and save them to a file. Whether you're working with a single CIDR block or multiple, this script has you covered.

---

## 📝 Table of Contents
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
  - [Single CIDR](#single-cidr)
  - [Multiple CIDRs](#multiple-cidrs)
  - [Saving Options](#saving-options)
- [Example Outputs](#example-outputs)
- [License](#license)

---

## ✨ Features

- **Single CIDR Input:** Convert a single CIDR block to a list of IP addresses.
- **Multiple CIDR Input:** Handle multiple CIDR blocks via manual entry or file input.
- **File Saving:** Save all generated IP addresses into a single file or separate files.
- **Progress Feedback:** Provides progress updates during execution.
- **Error Handling:** Graceful handling of invalid CIDR formats and missing files.
- **Colorful UI:** Improved user interface with color-coded output for better readability.

---

## 📥 Installation

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/Ayanrajpoot/cidr2ip.git
   cd cidr2ip


Ensure Python is Installed:
      • This script requires Python 3.6 or higher.
       Check your Python version with:
      ```bash
         python --version

## 🚀 Usage

### Single CIDR

1. **Run the Script:**
   ```bash
   python cidr_converter.py
   ```

2. **Select the Single CIDR Option:**
   - When prompted, select the option `1` to input a single CIDR block.
   - Enter your CIDR notation (e.g., `192.168.1.0/24`).

3. **Save the Output:**
   - Enter the filename where you want to save the list of IP addresses.

4. **Result:**
   - The script will save the IP addresses for the provided CIDR into the specified file and display a confirmation message.

### Multiple CIDRs

1. **Run the Script:**
   ```bash
   python cidr_converter.py
   ```

2. **Select the Multiple CIDRs Option:**
   - Choose option `2` to input multiple CIDRs.

3. **Input Method:**
   - **Manual:** Enter multiple CIDR blocks separated by commas.
   - **File:** Provide a text file containing CIDRs, one per line.

4. **Choose Saving Option:**
   - **Same File:** Save all IP addresses from multiple CIDRs into one file.
   - **Different Files:** Save IP addresses for each CIDR in separate files.

5. **Result:**
   - The script will process each CIDR, save the IPs accordingly, and provide progress updates.
