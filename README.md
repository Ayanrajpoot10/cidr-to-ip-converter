# CIDR to IP Converter

Welcome to the **CIDR to IP Converter** script! This tool allows you to easily convert CIDR notation into a list of IP addresses and save them to a file. Whether you're working with a single CIDR block or multiple, this script has you covered.

---

## 📝 Table of Contents
- [Features](#-features)
- [Installation](#-installation)
- [Usage](#-usage)
  - [Single CIDR](#-single-cidr)
  - [Multiple CIDRs](#-multiple-cidrs)
  - [Saving Options](#-saving-options)
- [Example Outputs](#-example-outputs)
- [License](#-license)

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



## 🚀 Usage

### Single CIDR

1. **Run the Script:**
   ```bash
   python cidr2ip.py
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
   python cidr2ip.py
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

## 💻 Example Outputs

### Single CIDR Example
```bash
$ python cidr2ip.py

▒█▀▀█ ▀█▀ ▒█▀▀▄ ▒█▀▀█ 　 █▀█ 　 ▀█▀ ▒█▀▀█ 
▒█░░░ ▒█░ ▒█░▒█ ▒█▄▄▀ 　 ░▄▀ 　 ▒█░ ▒█▄▄█ 
▒█▄▄█ ▄█▄ ▒█▄▄▀ ▒█░▒█ 　 █▄▄ 　 ▄█▄ ▒█░░░
                               By- Ayan Rajpoot    

Welcome to the CIDR to IP Converter
1. Input a single CIDR
2. Input multiple CIDRs
Choose an option (1 or 2): 1
Enter a CIDR (e.g., 192.168.1.0/24): 192.168.1.0/24
Enter the filename to save IP addresses (e.g., ip_addresses.txt): output.txt
IP addresses for 192.168.1.0/24 saved to output.txt
Total number of IP addresses saved: 256
```

### Multiple CIDRs Example
```bash
$ python cidr2ip.py

▒█▀▀█ ▀█▀ ▒█▀▀▄ ▒█▀▀█ 　 █▀█ 　 ▀█▀ ▒█▀▀█ 
▒█░░░ ▒█░ ▒█░▒█ ▒█▄▄▀ 　 ░▄▀ 　 ▒█░ ▒█▄▄█ 
▒█▄▄█ ▄█▄ ▒█▄▄▀ ▒█░▒█ 　 █▄▄ 　 ▄█▄ ▒█░░░
                               By- Ayan Rajpoot          

Welcome to the CIDR to IP Converter
1. Input a single CIDR
2. Input multiple CIDRs
Choose an option (1 or 2): 2
Do you want to input CIDRs manually or provide a file? (manual/file): manual
Enter CIDR(s) separated by a comma (e.g., 192.168.1.0/24,10.0.0.0/8): 192.168.1.0/24,10.0.0.0/8
Do you want to save the results to the same file or different files? (same/different): same
Enter the filename to save all IP addresses (e.g., ip_addresses.txt): output.txt
Processed 192.168.1.0/24. IP addresses appended to output.txt.
Processed 10.0.0.0/8. IP addresses appended to output.txt.
All IP addresses saved to output.txt
Total number of IP addresses saved: 16777216
```

---

## 📜 License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

## 📬 Contact

For any issues or suggestions, feel free to create an issue or pull request, or contact the author:

- **GitHub:** [Ayanrajpoot10](https://github.com/Ayanrajpoot10)
- **Email:** Ayanrajpoot2004@gmail.com

---

Thank you for using the CIDR to IP Converter! Happy coding! 🎉
```
