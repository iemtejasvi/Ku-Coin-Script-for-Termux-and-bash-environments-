# KuCoin-Script for Termux and Bash Environments

This Python script automates interaction with the KuCoin "xKucoin" account on Telegram, allowing you to tap for coins and collect rewards automatically. The script is optimized for **mobile Termux** and **bash environments**, making it easy to use on mobile devices or lightweight servers.

## Features

- Automatically taps for coins and collects KuCoin rewards via Telegram.
- Manage multiple KuCoin accounts with an interactive interface.
- Retrieves and displays your KuCoin balance after each session.
- Optimized for mobile environments like Termux (no emojis, no extra dependencies).
- Can run in the background for long-term automation.

## Requirements

- **Python 3.x** (Ensure it's installed in your Termux or bash environment).
- **Termux** on Android or **any bash-compatible terminal** on Linux systems.

## Installation and Setup

### 1. Install Git and Python in Termux

Before starting, you need to install **Git** and **Python** in Termux. Follow these commands to install the necessary packages:

#### Update and Upgrade Termux:

```bash
pkg update && pkg upgrade
```

#### Install Git:

```bash
pkg install git
```

#### Install Python:

```bash
pkg install python
```

### 2. Clone the Repository

Once Git is installed, clone the KuCoin script repository:

```bash
git clone https://github.com/iemtejasvi/Ku-Coin-Script-for-Termux-and-bash-environments-.git
cd Ku-Coin-Script-for-Termux-and-bash-environments-
```

### 3. Install Required Python Packages

There are two ways to install the required Python packages:

#### a. Using `requirements.txt` (If Available):

If the `requirements.txt` file exists in the repository, you can install the dependencies with this command:

```bash
pip install -r requirements.txt
```

#### b. Manually Installing Dependencies (If `requirements.txt` Fails):

If the `requirements.txt` file is missing or the installation fails, you can manually install the required libraries:

- **Colorama**: For colored terminal output.
- **Requests**: For handling HTTP requests.

Run these commands to install the required libraries manually:

```bash
pip install colorama
pip install requests
```

Once these dependencies are installed, you can proceed with running the script.

### 4. Retrieve Your Telegram Data

To use the script, you need to retrieve your Telegram user data from the official "xKucoin" account. Follow these steps:

#### How to Retrieve Telegram Data:

1. Install the Telegram app on your **PC** (do **not** use the browser version).
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

## Running the Script on Mobile Termux

This script is specifically designed to work on **Termux**, making it perfect for mobile automation. You can keep the script running in the background on your Android device using Termux's `wake lock` feature to prevent the device from sleeping during execution.

### 1. Keep the Script Running in the Background:

If you want to ensure the script keeps running even when you close Termux or lock the screen, you can run it inside **tmux**:

#### Install tmux:

```bash
pkg install tmux
```

#### Start a tmux session and run the script:

```bash
tmux new -s kucoin
python ku.py
```

This will allow the script to run in a separate session.

To **detach** from the tmux session without stopping the script, press:

```
Ctrl + B, then D
```

### 2. Reattach the tmux Session Later:

If you want to reattach to the session to check on the script, use:

```bash
tmux attach -t kucoin
```

This ensures the script runs in the background without interruptions even if the terminal is closed.

## Conclusion

The KuCoin-Script for Termux and bash environments is a lightweight, mobile-friendly solution for automating KuCoin rewards via Telegram. It can be run easily on Android devices or Linux systems, offering a flexible solution for long-term automation.

