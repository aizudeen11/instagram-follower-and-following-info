# 📊 Instagram Followers vs Following Analysis

This project helps you analyze your Instagram followers and following lists by comparing exported HTML files. It identifies:

- Users you follow who **don’t follow you back**
- Users who **follow you but you don’t follow back**
- Users with **mutual connections**

---

## 🚀 Features
- Parse Instagram HTML data using **BeautifulSoup**
- Compare followers and following lists
- Generate categorized outputs:
  - `follower_list`
  - `following_list`
  - `follower_or_following`
  - `follower_and_following` (mutuals)
  - `following_only`
  - `follower_only`
- Export results into a structured **CSV file**

---

## 🛠️ Tech Stack
- Python
- BeautifulSoup (`bs4`)
- Pandas

---

## 📂 Input Files
You need to download your Instagram data in HTML format:

👉 https://help.instagram.com/181231772500920

After downloading:
- Locate:
  - `followers.html`
  - `following.html`
- Place both files in the same directory as the script

---

## ▶️ How to Run

1. Install dependencies:
```bash
pip install beautifulsoup4 pandas
