
# Case Study: Social Network Adjacency Matrix

users = ["Amit", "Priya", "Rahul", "Sneha", "Rohan"]
n = len(users)

# Create adjacency matrix
adjacency_matrix = [[0] * n for _ in range(n)]

# Friendship connections
friendships = [
    ("Amit", "Priya"),
    ("Amit", "Rahul"),
    ("Priya", "Sneha"),
    ("Rahul", "Sneha"),
    ("Sneha", "Rohan")
]

# Add friendships to the matrix
for user1, user2 in friendships:
    i = users.index(user1)
    j = users.index(user2)

    adjacency_matrix[i][j] = 1
    adjacency_matrix[j][i] = 1


# Display adjacency matrix
print("SOCIAL NETWORK ADJACENCY MATRIX")
print()

print(f"{'User':<10}", end="")
for user in users:
    print(f"{user:<10}", end="")
print()

for i, user in enumerate(users):
    print(f"{user:<10}", end="")
    for value in adjacency_matrix[i]:
        print(f"{value:<10}", end="")
    print()


# Check friendship
def are_friends(user1, user2):
    i = users.index(user1)
    j = users.index(user2)
    return adjacency_matrix[i][j] == 1


# Find all friends
def find_friends(user):
    i = users.index(user)
    return [
        users[j]
        for j in range(n)
        if adjacency_matrix[i][j] == 1
    ]


# Display results
print("\nFriendship Checks:")
print("Are Amit and Priya friends?",
      are_friends("Amit", "Priya"))

print("Are Amit and Rohan friends?",
      are_friends("Amit", "Rohan"))

print("Friends of Sneha:", find_friends("Sneha"))
