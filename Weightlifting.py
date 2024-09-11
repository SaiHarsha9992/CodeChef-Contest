# cook your dish here
# Read input
A1, A2, B1, B2, C1, C2 = map(int, input().split())

# Calculate the best scores in each round
best_round_1 = max(A1, A2)
best_round_2 = max(B1, B2)
best_round_3 = max(C1, C2)

# Calculate the total score
total_score = best_round_1 + best_round_2 + best_round_3

# Output the total score
print(total_score)
