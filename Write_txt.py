# Write to Txt

products = ['Notebook','Monitor','Mouse','Car','House']

with open('produtcs.txt', "w") as writer:
    for prod_text in products:
        writer.write(prod_text + '\n')
