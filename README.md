<div align="center">

  <p align="center"><img src="https://github.com/Cursed271/Cursed271/blob/main/Logo.png" width="30%"></a></p>
  <h1>DeadKey</h1>
  
  <p>
    DeadKey simulates keylogging attacks to test EDR systems, enabling users to strengthen their defense strategies.
  </p>
  
  <h4>
    <a href="https://github.com/Cursed271/DeadKey/issues/new?labels=bug&template=bug_report.md">Report Bug</a>
  <span> · </span>
    <a href="https://github.com/Cursed271/DeadKey/issues/new?labels=enhancement&template=feature_request.md">Request Feature</a>
  </h4>

</div>

## 📖 Table of Contents

- [Introduction](#-introduction)
- [Features](#-features)
- [Installation and Usage](#%EF%B8%8F-installation-and-usage)
- [Feedback](#-feedback)
- [Contributors](#-contributors)
- [License](#-license)

## 🚀 Introduction

DeadKey is a Python-based keylogging simulation designed for authorized purple team assessments and security testing. It captures all keystrokes on a target system, including letters, numbers, modifiers, function keys, and arrows, then transmits them to a controlled server, where they are timestamped and logged in a structured format for detailed analysis and evaluation of EDR detection capabilities.

<p align="center">
  <h4>DeadKey</h4>
  <img src = "https://github.com/Cursed271/DeadKey/blob/main/DeadKey.png">
</p>

<p align="center">
  <h4>DeadKey Server</h4>
  <img src = "https://github.com/Cursed271/DeadKey/blob/main/DeadKeyServer.png">
</p>

## ✨ Features:

- ⌨️ Keystroke Capture: Captures all keys including letters, numbers, modifiers, function keys, and arrows.

- 🌐 Remote Logging: Sends captured keystrokes to a server for real-time analysis.

- 🕒 Timestamped Logs: Each keystroke can be logged with timestamps for detailed assessment.

- ⚙️ Procedural & Lightweight: Pure Python script, no GUI, minimal footprint.

- 🛡️ Lab-Safe Testing: Designed only for authorized purple team and EDR testing scenarios.

## ⚙️ Installation and Usage:

1. **Pre-requisites**: Ensure you have Python3 installed on your system.
2. **Clone the Repo**: Use "***git clone https://github.com/Cursed271/DeadKey***"
3. **Traverse into the Directory**: Use "***cd DeadKey***"
4. **Install Dependencies**: Use "***pip3 install -r requirements.txt***"
5. **Execute the Server Script**: Use "***python3 DeadKeyServer.py***"
6. **Execute the Keylogger Script on the Target Machine**: Use "***python3 DeadKey.py***"

## 💬 Feedback  

Have suggestions or feature requests? Feel free to reach out via:  

- 🐦 **Twitter**: [@Cursed271](https://x.com/Cursed271)  
- 🐙 **GitHub**: [@Cursed271](https://github.com/Cursed271)  
- 🔗 **LinkedIn**: [Steven Pereira](https://www.linkedin.com/in/Cursed271/)  
- 📧 **Email**: [cursed.pereira@proton.me](mailto:cursed.pereira@proton.me)  
- 🐞 **File an Issue**: [GitHub Issues](https://github.com/Cursed271/DeadKey/issues)  
- 💡 **Request a Feature**: [Feature Requests](https://github.com/Cursed271/DeadKey/issues/new?labels=enhancement&template=feature_request.md) 

Your feedback helps improve DeadKey! Contributions and PRs are always welcome. 🚀

## 🙌 Contributors

- **Steven Pereira (aka Cursed)** - Creator & Maintainer  

## 📜 License

DeadKey is licensed under the **MIT License**. See the [LICENSE](LICENSE) file for details.