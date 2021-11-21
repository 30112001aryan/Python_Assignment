test_list = [{'name': 'affirm', 'confidence': 0.9448149204254}, {'name': 'affirm', 'confidence': 0.944814920425415}, {'name': 'inform', 'confidence': 0.9842240810394287}, {'name': 'inform', 'confidence': 0.9842240810394287}]
res = list(map(dict, set(tuple(sorted(sub.items())) for sub in test_list)))
print("The list after removing duplicates : " + str(res))
