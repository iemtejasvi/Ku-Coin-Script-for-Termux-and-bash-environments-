# KuCoin-Script for Termux and Bash Environments

This Python script automates interaction with the KuCoin "xKucoin" account on Telegram, allowing you to tap for coins and collect rewards automatically. The script is optimized for **mobile Termux** and **bash environments**, making it easy to use on mobile devices or lightweight servers.

## Features

- Automatically taps for coins and collects KuCoin rewards via Telegram.
- Manage multiple KuCoin accounts with an interactive interface.
- Retrieves and displays your KuCoin balance after each session.
- Optimized for mobile environments like Termux (no emojis, no extra dependencies).
- Can run in the background for long-term automation.

## Requirements

- **Python 3.x** (Make sure it's installed in your Termux or bash environment).
- **Termux (on Android)** or **any bash-compatible terminal** on Linux systems.

## Installation and Setup

### 1. Install Python in Termux

Ensure you have Python installed in your Termux or bash environment. To install Python in **Termux**, use the following commands:

```bash
pkg update && pkg upgrade
pkg install python
```

### 2. Clone the Repository

Next, clone the script repository from GitHub:

```bash
git clone https://github.com/iemtejasvi/Ku-Coin-Script-for-Termux-and-bash-environments-.git
cd Ku-Coin-Script-for-Termux-and-bash-environments-
```

### 3. Install Required Python Packages

The required Python libraries are listed in the `requirements.txt` file. Install them using pip:

```bash
pip install -r requirements.txt
```

This will install all the necessary packages such as `colorama`, `requests`, and others.

### 4. Retrieve Your Telegram Data

To use the script, you need to retrieve your Telegram user data from the official "xKucoin" account. Follow these steps:

#### How to Retrieve Telegram Data:

1. Install the Telegram app on your PC (do **not** use the browser version).
2. Open Telegram and navigate to **Settings** > **Advanced** > **Experimental Settings**, then enable **Webview Inspecting**.
3. Search for "xKucoin" in Telegram and confirm it has a blue check mark.
4. Open the official account and click on **Play Game**.
5. Press `Ctrl + Shift + J` to open the developer console.
6. In the console, type `allow pasting`, then paste the following:

    ```javascript
    copy(Telegram.WebApp.initData)
    ```

    You should see "undefined," indicating that the data has been copied.
7. Paste this data into a text file or directly into the script when prompted.

For a detailed guide, refer to this [video tutorial](https://youtu.be/K66LMX513n4?si=aR5o_VMaVnget6t_).

### 5. Running the Script

Once you have retrieved your Telegram data, you can run the script using:

```bash
python ku.py
```

The script will guide you through adding your KuCoin accounts and managing them.

## Account Management

The script provides an easy-to-use interface for managing multiple KuCoin accounts:

- **Add a new account**: Paste your encoded Telegram data.
- **View all accounts**: Displays all added accounts.
- **Delete an account**: Removes a selected account.
- **Clear all accounts**: Deletes all accounts (use with caution).

## Running on Mobile Termux

This script is specifically designed to work on **Termux**, making it perfect for mobile automation. You can keep the script running in the background on your Android device using Termux's `wake lock` feature to prevent the device from sleeping during execution.

1. **Keep the script running in the background**:

   If you want to ensure the script keeps running even when you close Termux or the screen locks, you can run it inside `tmux`:

   ```bash
   apt install tmux
   tmux new -s kucoin
   python ku.py
   ```

   To exit tmux while keeping it running in the background, press `Ctrl + B`, then `D`.

2. **Reattach the session later**:

   ```bash
   tmux attach -t kucoin
   ```

This ensures the script runs in the background without interruptions.

## Conclusion

The KuCoin-Script for Termux and bash environments is a lightweight, mobile-friendly solution for automating KuCoin rewards via Telegram. It can be run easily on Android devices or Linux systems, offering a flexible solution for long-term automation.

For more information or updates, visit the repository: [KuCoin-Script for Termux and Bash Environments](https://github.com/iemtejasvi/Ku-Coin-Script-for-Termux-and-bash-environments-.git).
