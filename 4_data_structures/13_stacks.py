browsing_session = []
# Add on top of the stack
browsing_session.append(1)
browsing_session.append(2)
browsing_session.append(3)
print(browsing_session)  # [1, 2, 3]

# Remove item on top of the stack
last = browsing_session.pop()
print(last)  # 3
print(browsing_session)  # [1, 2]

# Get item on top of the stack
print(browsing_session[-1])  # 2
