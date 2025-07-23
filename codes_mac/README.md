# 🧠 NEURON Python Setup (For RISE Students)

This project uses the **NEURON simulator** in Python. You’ll run your code using **Visual Studio Code (VS Code)**.  
👉 You do **NOT** need to install anything outside VS Code except **Python 3.9**.

---

## ✅ What You Need First

1. **Install Python 3.9.7**  
   🔗 https://www.python.org/downloads/release/python-397/

2. **Install Visual Studio Code**  
   🔗 https://code.visualstudio.com/

---

## 🛠️ How to Set Up in VS Code (Step-by-Step)

### 1. 🚪 Open VS Code

- Open **Visual Studio Code**
- Go to **File > Open Folder...**
- Choose the folder that contains these files:
  - `neuron_test_code.py`
  - `requirements.txt`
  - `README.md` (this file!)

---

### 2. 🖥️ Open the Terminal

This is where you’ll type your commands.

- Click the top menu: **Terminal > New Terminal**
- A terminal panel appears at the bottom of VS Code

You should now see something like:

```bash
yourname@computer:~/your-folder$
````

---

### 3. 🧪 Create a Virtual Environment (Only Once)

This creates a safe Python space for your packages.

#### ✅ For Windows:

```bash
python -m venv .venv
.\.venv\Scripts\activate
```

#### ✅ For macOS or Linux:

```bash
python3.9 -m venv .venv
source .venv/bin/activate
```

Once it works, your terminal should look like this:

```bash
(.venv) yourname@computer:~/your-folder$
```

---

### 4. 📦 Install the Required Packages

Make sure you're still in the same folder, then run:

```bash
pip install -r requirements.txt
```

This installs everything the code needs. It might take a few minutes. ⏳
If you see messages like “Successfully installed...”, you’re good!

---

### 5. 🚀 Run the NEURON Test Code

Try this command to test the setup:

```bash
python neuron_test_code.py
```

You should see some NEURON info printed. 🎉
If you get a warning like this:

```
Matplotlib is using agg, which is a non-GUI backend...
```

Just replace the `plt.show()` line with:

```python
plt.savefig("output.png")
```

Then open `output.png` in your folder to see the plot!

---

## 💡 VS Code Tips

* Use **Ctrl + \`** (backtick) to toggle the terminal
* If prompted, click “Select Python Interpreter” and choose `.venv`
* Save files often with **Ctrl + S** or **Cmd + S**

---

## 😅 Something Went Wrong?

No worries! Here's what to send to your teacher or TA:

* Your operating system (Windows, macOS, Linux)
* The command you ran
* The **full error message**
* A screenshot if you can 📸

---

You got this! Step-by-step, no rush. Ask questions. Coding is like learning a new superpower 💥🧠🚀


BU RISE 2025 Staff
July 2025