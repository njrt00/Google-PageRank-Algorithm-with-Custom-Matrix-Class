# Google PageRank Algorithm with Custom Matrix Class

This project implements the **Google PageRank algorithm from scratch** using a custom matrix class and power iteration on the Stanford Web Graph dataset. It demonstrates how search engines rank webpages based on link structure using linear algebra and Markov chains.

---

## Overview

The PageRank algorithm models the web as a directed graph where:

- Nodes represent webpages
- Edges represent hyperlinks between pages

The goal is to compute the importance (rank) of each webpage based on the structure of incoming links.

This implementation avoids high-level linear algebra libraries for core computations and instead builds everything using a custom `Matrix` class.

---

## Key Concepts

### 1. Adjacency Matrix
Represents the directed graph of webpages:
- `A[i][j] = 1` if page *i* links to page *j*
- Otherwise `0`

---

### 2. Stochastic Matrix
Each column is normalized so it sums to 1:

:contentReference[oaicite:0]{index=0}

---

### 3. Google Matrix

The Google matrix introduces random jumps (damping factor):

:contentReference[oaicite:1]{index=1}

Where:
- \( \alpha \) = damping factor (typically 0.85)
- \( S \) = stochastic matrix
- \( J \) = all-ones matrix
- \( n \) = number of nodes

---

### 4. PageRank Computation (Power Iteration)

We compute the dominant eigenvector:

:contentReference[oaicite:2]{index=2}

After several iterations, \( v \) converges to the PageRank scores.

---

## Features

- Custom-built `Matrix` class (no NumPy linear algebra used for core logic)
- Manual matrix operations (addition, multiplication, slicing, transpose)
- Construction of adjacency, stochastic, and Google matrices
- Power iteration method for eigenvector computation
- Ranking of webpages based on importance

---

## Dataset

This project uses a subset of the **Stanford Web Graph dataset**, where:
- Each row represents a directed edge between two webpages

---

## Example Output

```text
Top 10 Ranked Websites:

Rank 1: Website 985 | Score = 0.00431215
Rank 2: Website 123 | Score = 0.00398144
Rank 3: Website 47  | Score = 0.00375210
...
