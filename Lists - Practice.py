
products = ['ice cream','banana','apple','chips']
print(products)

# Append method : Only one itms adds at the end of the list
products.append('lays')
print(products)

products.append('mobile')
print(products)


# Make a copy of the list
products_copy = products.copy()
print(products_copy)

# Clear the products list
products.clear()
print(products)

# Count the list items
print(products_copy.count('lays'))

# Extend another list in products_copy list. first we add something in products list and then add it to the products_copy list
products.append('soap')
products.append('eggs')

print(products)

products_copy.extend(products)
print(products_copy)

# Insert item on index 1
products_copy.insert(0, 'ice cream - banana flavour')
print(products_copy)

# Pop an item from the list
products_copy.pop(1)
print(products_copy)

# Remove first element from the list
products_copy.insert(0, 'ice cream - banana flavour')
print(products_copy)

products_copy.remove('ice cream - banana flavour')
print(products_copy)

# Reverse the order of a list
products_copy.reverse()
print(products_copy)

# Sort the list
products_copy.sort()
print(products_copy)

#Index of a specific item
print(products_copy.index('apple'))