import numpy as np

# ============================================================
# PageRank Algorithm on Stanford Web Graph
# ============================================================
# This project:
# 1. Loads a web graph edge list
# 2. Builds an adjacency matrix
# 3. Converts it to a stochastic matrix
# 4. Constructs the Google matrix
# 5. Uses power iteration to compute PageRank
# 6. Displays the top ranked webpages
# ============================================================


# ------------------------------------------------------------
# Load Matrix Tools
# ------------------------------------------------------------
%run Matrix_Tools.ipynb


# ------------------------------------------------------------
# Load Stanford Web Graph Data
# ------------------------------------------------------------
# File format:
# each row contains:
# [from_node, to_node]
# representing a directed edge

MM = np.loadtxt("web-Stanford-small.txt")

print("Matrix Market Shape:", MM.shape)

print("\nFirst 10 edges:")
for i in range(10):
    print("from:", MM[i][0], "\tto:", MM[i][1])


# ------------------------------------------------------------
# Create Adjacency Matrix
# ------------------------------------------------------------

n = 4109
A = zeros(n, n)

# Insert edges into adjacency matrix
# Note:
# Dataset nodes are 1-indexed
# Python uses 0-indexing

for link in MM:

    from_node = int(link[0]) - 1
    to_node = int(link[1]) - 1

    A[from_node][to_node] = 1.0


print("\nAdjacency matrix created.")


# ------------------------------------------------------------
# Create Stochastic Matrix S
# ------------------------------------------------------------
# Each column is normalized to sum to 1

S = 1.0 * A

rows, cols = S.shape

# Compute column sums
col_sums = [0.0 for j in range(cols)]

for j in range(cols):
    for i in range(rows):
        col_sums[j] += S[i][j]

# Normalize columns
for j in range(cols):

    if col_sums[j] != 0:

        for i in range(rows):
            S[i][j] /= col_sums[j]


print("Stochastic matrix created.")


# ------------------------------------------------------------
# Construct Google Matrix
# ------------------------------------------------------------

alpha = 0.85

J = ones(n, n)

G = 1.0 * J

for i in range(n):
    for j in range(n):

        G[i][j] = (
            alpha * S[i][j]
            + (1 - alpha) / n
        )


print("Google matrix created.")


# ------------------------------------------------------------
# Power Iteration Method
# ------------------------------------------------------------
# Computes dominant eigenvector of G
# which corresponds to PageRank scores

v = [1.0 for i in range(n)]

iterations = 20

for it in range(iterations):

    w = [0.0 for i in range(n)]

    # Matrix-vector multiplication
    for i in range(n):
        for j in range(n):
            w[i] += G[i][j] * v[j]

    # Normalize vector
    total = sum(w)

    for i in range(n):
        w[i] /= total

    v = w

    print(f"Iteration {it+1} completed.")


# ------------------------------------------------------------
# Rank Websites by PageRank Score
# ------------------------------------------------------------

score_index_pairs = []

for i in range(len(v)):
    score_index_pairs.append([v[i], i])

# Sort from highest score to lowest
score_index_pairs.sort(reverse=True)


# ------------------------------------------------------------
# Display Top 10 Websites
# ------------------------------------------------------------

print("\nTop 10 Ranked Websites:\n")

for i in range(10):

    score = score_index_pairs[i][0]

    # Convert back to 1-based indexing
    website_index = score_index_pairs[i][1] + 1

    print(
        f"Rank {i+1}: "
        f"Website {website_index} "
        f"| Score = {score:.8f}"
    )
