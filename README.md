# 🍽️ SmartResto System

SmartResto System is a Command-Line Interface (CLI) restaurant management application developed in Python. The project demonstrates the practical implementation of multiple data structures within a real-world restaurant operation scenario, including menu management, customer queues, kitchen processing, inventory tracking, and delivery routing.

---

## 🚀 Features

- View restaurant menu categories and items
- Manage customer queues
- Place food and beverage orders
- Automatically update ingredient stock
- Store order history
- Undo the most recent order
- Manage kitchen orders
- Complete kitchen processing tasks
- Display delivery routes
- Find the shortest delivery path using graph traversal
- Monitor ingredient inventory

---

## 📚 Data Structures Implemented

### 🌳 Tree
Used to organize menu categories and menu items hierarchically.

**Applications:**
- Menu navigation
- Category-based menu organization

### 📋 Queue
Used to manage customer waiting lines using the FIFO (First In, First Out) principle.

**Applications:**
- Customer service queue management

### 📚 Stack
Used to store order history following the LIFO (Last In, First Out) principle.

**Applications:**
- Undo last order feature

### 🔗 Linked List
Used to manage kitchen orders dynamically.

**Applications:**
- Adding new kitchen orders
- Removing completed kitchen orders

### 📖 Dictionary
Used for inventory and stock management.

**Applications:**
- Fast ingredient lookup
- Automatic stock updates after successful orders

### 🗺️ Graph
Used to represent delivery locations and routes.

**Applications:**
- Delivery route mapping
- Breadth-First Search (BFS) route discovery

---

## 🏗️ Project Structure

```text
SmartResto-System
│
├── data/
│
├── modules/
│   ├── tree_menu.py
│   ├── queue_antrian.py
│   ├── stack_undo.py
│   ├── linkedlist_dapur.py
│   ├── dictionary_stok.py
│   └── graph_delivery.py
│
├── services/
│
├── views/
│
├── utils/
│
└── main.py
```

---

## ▶️ Installation

### Clone the Repository

```bash
git clone https://github.com/yourusername/smartresto-system.git
```

### Navigate to the Project Directory

```bash
cd smartresto-system
```

### Run the Application

```bash
python main.py
```

---

## 💡 Learning Objectives

This project was developed to demonstrate the practical implementation of fundamental data structures in software development. It showcases how different data structures can work together to solve real-world restaurant management problems efficiently.

---

## 🛠️ Technologies Used

- Python 3
- JSON
- Object-Oriented Programming (OOP)
- Command Line Interface (CLI)

---

## 📈 Concepts Demonstrated

- Data Structures
  - Tree
  - Queue
  - Stack
  - Linked List
  - Dictionary (Hash Map)
  - Graph

- Algorithms
  - Breadth-First Search (BFS)

- Software Design
  - Modular Programming
  - Separation of Concerns
  - Service-Based Architecture

---

## 🎓 Academic Purpose

This project was created as part of a Data Structures course to demonstrate the implementation and integration of multiple data structures within a single application.

---

## 📄 License

This project is intended for educational and portfolio purposes.
