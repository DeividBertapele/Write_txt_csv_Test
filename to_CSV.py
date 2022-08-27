# Write to csv

products = ['Notebook','Monitor','Mouse','Car','House']

with open('produtcs.csv', "w") as writer:
    for prod_text in products:
        writer.write(prod_text + '\n')