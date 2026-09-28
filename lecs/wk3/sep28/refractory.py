# Raw data
subject_ids = [
    "005bc437-e2b3-4502-a1af-802c9553436a",
    "013427b3-be9a-48ad-a1b9-a8a47d3abc57",
    "0b4a3454-ba7a-4ab5-b9bf-711312069ba8",
    "11e5b23d-3e70-4ff6-a52d-e53a853fd16f",
    "11f5b8ce-74f5-491a-907f-e5d99c2c8c14",
    "134eb286-a1e6-480e-9137-15c9790805de",
    "1d230e0e-9aec-4bf4-a2ff-4353b0290017",
    "1d51e00f-1d80-44e4-8a78-d528acec6ce8",
    "1f86e503-f68b-4b17-b81a-d5e891fe63e7",
    "25126c59-b212-4930-ab01-e7f79d3e25bc",
    "27614631-0178-4fb6-8402-4af8673dc493",
    "295bbe25-8692-4a73-ac75-d82819e45485",
    "2f360ba8-125b-4743-bcca-9d36528b5953",
    "2fc99978-0d9f-46fd-83a9-983be6024fa8",
    "369ce5ea-b7f7-4260-a3f4-281852bfcc42",
    "377c8e07-3c77-435b-9c5f-beacf9c93022",
    "3bf93774-80e9-4e27-bc7c-dc6d774e755b",
    "4175c624-229e-4c3f-8ff3-2b927554a0c9",
    "4d95944e-81cf-4003-8ba1-609c6258b346",
    "57042e51-7ca6-42b2-8609-8a1f9f0edd70",
]

responses = [
    ["PR", "PD", "PD", "PD", "PD"],
    ["VGPR", "PR", "PD", "PR", "PD", "PR"],
    ["PR"],
    ["PR"],
    ["PR", "PR", "PD"],
    ["PR", "PD", "PR"],
    ["PR"],
    ["PR", "PD", "PD", "PD"],
    ["VGPR"],
    ["PD", "PD", "PD", "PD", "PD", "PD"],
    ["PD", "PR"],
    ["PR", "PD", "PR"],
    ["PR", "PR", "PR"],
    ["PD"],
    ["PR", "PD", "PD", "PD"],
    ["PR"],
    ["PR", "PR", "PD", "PR", "PD"],
    ["PR"],
    ["PR", "PD", "PR", "PR"],
    ["PR", "PD", "PD", "PD", "PD", "PD"],
]

# ToDo: Determine how many subjects are Relapsed.
    # Relapsed: When a subject has a positive response (PR, VGPR, or CR) followed by a negative response (PD)
    # at some later time point.
#

# TODO: my solution is wrong... should be 10.
relapsed_subjects = 0
for i in range(len(subject_ids)):
    has_positive = False
    for j in responses[i]:
        if j in ["PR", "VGPR", "CR"]:
            has_positive = True
        if has_positive and j == "PD":
            relapsed_subjects += 1
            # should break here (?)

print(relapsed_subjects)


# prof solution
observations = ["PR", "PD", "PD", "PD", "PD"]
# 1. search for positive
# 2. search for negative
# 3. stop when I find a negative after a positive

relapsed = 0
for observations in responses:
    negative, positive, index = -1, len(observations), 0
    while index < len(observations) and negative < positive:
        if observations[index] in ["PR", "VGPR", "CR"]:
            positive = index
        elif observations[index] in ["PD"]:
            negative = index
        index += 1
    relapsed += int(negative > positive)
print(relapsed)
