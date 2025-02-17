# Pixela Habit Tracker

Stay motivated and track your habits effortlessly with **Pixela Habit Tracker**! This simple and powerful tool helps you visualize progress over time using the **Pixela API**, making habit tracking more interactive and rewarding.

## 🚀 Features

✅ **Seamless Habit Tracking** – Log daily progress effortlessly with a simple API request.
✅ **Visual Graph Representation** – Watch your progress grow with customizable graphs.
✅ **Automatic Logging** – Update entries dynamically with ease.
✅ **Edit & Delete Entries** – Modify past records or remove them as needed.
✅ **Personalized Experience** – Customize your graphs for different activities (e.g., exercise, reading, coding).

## 🔧 How It Works

### 1️⃣ Set Up Your Credentials
Before running the script, update the following placeholders in `main.py`:
```python
USERNAME = "YOUR USERNAME"
TOKEN = "YOUR SELF GENERATED TOKEN"
GRAPH_ID = "YOUR GRAPH ID"
```

### 2️⃣ Track Your Progress
Run the script and enter your habit progress when prompted:
```bash
python main.py
```
You’ll be asked how many kilometers (or another unit) you completed today, and the data will be recorded on your graph.

### 3️⃣ Modify Your Data
Want to update an entry? Use the **PUT** request:
```python
new_pixel_data = {
    "quantity": "4.5"
}
response = requests.put(url=update_endpoint, json=new_pixel_data, headers=headers)
```

### 4️⃣ Delete an Entry
Need to remove an incorrect entry? Simply send a **DELETE** request:
```python
response = requests.delete(url=delete_endpoint, headers=headers)
```

## 🌍 API Endpoints

🔹 **Create a User** → `https://pixe.la/v1/users`
🔹 **Create a Graph** → `https://pixe.la/v1/users/{USERNAME}/graphs`
🔹 **Log a Habit** → `https://pixe.la/v1/users/{USERNAME}/graphs/{GRAPH_ID}`
🔹 **Update an Entry** → `https://pixe.la/v1/users/{USERNAME}/graphs/{GRAPH_ID}/{date}`
🔹 **Delete an Entry** → `https://pixe.la/v1/users/{USERNAME}/graphs/{GRAPH_ID}/{date}`

## 🎨 Customization

🎯 **Track Different Habits** – Change `GRAPH_ID` to monitor different activities like meditation, writing, or fitness.
🎨 **Personalize Your Graph** – Adjust `unit`, `type`, and `color` to make your graph more visually appealing.
🛠 **Automate Habit Logging** – Integrate the script into a cron job for seamless tracking.
