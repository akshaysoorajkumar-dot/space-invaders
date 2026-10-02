# 🚀 SPACE INVADERS IN PYTHON 🚀

A retro arcade Space Invaders clone built entirely from scratch using Python and Pygame! Take control of a starship, defend the planet, and blast down the invading alien armada before they touch down and destroy Earth!! 💥

---

### 🎓 Student Submission Details
* **Student Name:** Akshay Soorajkumar  
* **Project Name:** Space Invaders  
* **Target Language:** Python 3  
* **Graphics Library:** Pygame  

---

## 💻 Installation & Setup (Do this first!)

Before jumping into battle, make sure you have **Python** installed on your machine. If you don't have it yet, grab it from the official python.org website.

### Step 1: Install Pygame
This game uses a library called Pygame to handle all the cool graphics and windows. Open your Terminal or Command Prompt and run this command:
```bash
pip install pygame
```

### Step 2: Download the Project Folder
Download all the files from this repository into a folder on your computer. 

⚠️ **Important:** Keep all image asset folders, sound directories, and the main code files together in the exact same folder. If you move things around, Python won't be able to find the textures and it will crash!

### Step 3: Run the Game!
Open your terminal inside that folder and type this to start the game:
```bash
python main.py
```

---

## 🕹️ Game Controls

Don't panic! The defensive systems are super simple:
* **`A` / Left Arrow Key** — Move your starship left 👈
* **`D` / Right Arrow Key** — Move your starship right 👉
* **Spacebar** — Activate laser weapons and SHOOT THE ALIENS!!! 💥

---

## ✨ Features (Why my game is cool)

* **Dynamic Alien Grids:** The invaders move sideways in a synchronized pattern and drop down closer to Earth every time they hit a wall!
* **Health & Life Tracker:** You start with **3 lives**. Getting hit by enemy lasers costs a life—don't lose them all omg!
* **Real-time Score Engine:** A built-in scoreboard that updates and dynamically awards you points the second you blast an alien out of the sky.
* **Immersive Retro Assets:** Full arcade physics, responsive movement, and classic 8-bit sound effects!

---

## 😭 Troubleshooting / Help me it's broken

* **`Error: No module named pygame`**  
  * *Fix:* Your computer missed Step 1! Run `pip install pygame` in your terminal right now.
* **Game window flashes open and instantly crashes**  
  * *Fix:* The code is looking for an image or sound file that isn't where it belongs. Make sure your asset folders are sitting right next to your `main.py` file!
