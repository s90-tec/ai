
# Goal Stack Planning - Blocks World

state = {
    "ON(A,TABLE)",
    "ON(B,TABLE)",
    "CLEAR(A)",
    "CLEAR(B)",
    "HAND_EMPTY"
}

stack = ["ON(B,A)"]
plan = []

while stack:

    goal = stack.pop()

    if goal in state:
        continue

    if goal == "ON(B,A)":
        stack.extend([
            "MOVE(B,A)",
            "HAND_EMPTY",
            "ON(B,TABLE)",
            "CLEAR(A)",
            "CLEAR(B)"
        ])

    elif goal == "MOVE(B,A)":

        if all(x in state for x in [
            "HAND_EMPTY", "ON(B,TABLE)",
            "CLEAR(A)", "CLEAR(B)"
        ]):

            state.remove("ON(B,TABLE)")
            state.remove("CLEAR(A)")
            state.add("ON(B,A)")

            plan.append("Move B onto A")

print("Plan:")
for action in plan:
    print(action)

print("Final State:", state)
