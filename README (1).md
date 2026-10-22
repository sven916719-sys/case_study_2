
# Social Network Adjacency Matrix Using Python

## 1. Introduction
A social networking platform connects users through
friendships. These connections can be represented
using a graph and an adjacency matrix.

Each user represents a vertex, and each friendship
represents an edge.

## 2. Problem Statement
The objective is to represent friendship connections
between users, check whether two users are friends,
and find all friends of a selected user.

## 3. Objectives
- Represent users and friendship connections.
- Create an adjacency matrix using Python.
- Check whether two users are friends.
- Find friends of a particular user.
- Understand graph representation in social networks.

## 4. Technologies Used
- Python 3
- Graph Data Structure
- Adjacency Matrix

## 5. Algorithm
1. Create a list of users.
2. Initialize a matrix with zeros.
3. Add friendship connections by setting matrix
   entries to 1 in both directions.
4. Display the adjacency matrix.
5. Check friendship between two users.
6. Display all friends of a selected user.

## 6. Sample Friendship Connections
- Amit — Priya
- Amit — Rahul
- Priya — Sneha
- Rahul — Sneha
- Sneha — Rohan

## 7. Sample Output
SOCIAL NETWORK ADJACENCY MATRIX

User      Amit      Priya     Rahul     Sneha     Rohan
Amit      0         1         1         0         0
Priya     1         0         0         1         0
Rahul     1         0         0         1         0
Sneha     0         1         1         0         1
Rohan     0         0         0         1         0

Friendship Checks:
Are Amit and Priya friends? True
Are Amit and Rohan friends? False
Friends of Sneha: ['Priya', 'Rahul', 'Rohan']

## 8. Complexity Analysis
Let n be the number of users.

- Matrix space complexity: O(n^2)
- Friendship lookup: O(1) after user indexing
- Finding friends: O(n)

## 9. Limitations
An adjacency matrix requires O(n^2) memory.
For millions of users, it consumes a large amount
of memory. Adjacency lists or sparse matrices are
more suitable for large social networks.

## 10. Conclusion
The adjacency matrix provides a simple way to
represent and analyze friendship connections.
Python can be used to check friendships and find
friends efficiently in a small example.

## 11. How to Run
Install Python 3 and execute:

python social_network.py

## 12. Upload to GitHub
Create a repository named:
Social-Network-Adjacency-Matrix

Run these commands in the project folder:

git init
git add social_network.py README.md
git commit -m "Add social network adjacency matrix case study"
git branch -M main
git remote add origin https://github.com/YOUR-USERNAME/Social-Network-Adjacency-Matrix.git
git push -u origin main

Replace YOUR-USERNAME with your GitHub username.
