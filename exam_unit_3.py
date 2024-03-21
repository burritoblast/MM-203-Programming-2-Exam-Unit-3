def square(num):
    return num * num

def inches_to_mm(inches):
    return inches * 25.4

def root(num, iterations=10):
    x = num
    for _ in range(iterations):
        x = 0.5 * (x + num / x)
    return x

def cube(num):
    return num * num * num

def area_of_circle(radius):
    pi = 3.14159
    return pi * radius * radius

def greeting(name):
    return f"Hello, {name}!"

def flatten(arr):
    flat_list = []
    for item in arr:
        if isinstance(item, list):
            flat_list.extend(flatten(item))
        else:
            flat_list.append(item)
    return flat_list

def process_structure(node):
    if node is None:
        return {'sum': 0, 'deepest': 0, 'nodes': 0}
    
    left = process_structure(node.get('left'))
    right = process_structure(node.get('right'))
    
    total_sum = node['value'] + left['sum'] + right['sum']
    deepest_level = 1 + max(left['deepest'], right['deepest'])
    total_nodes = 1 + left['nodes'] + right['nodes']
    
    return {'sum': total_sum, 'deepest': deepest_level, 'nodes': total_nodes}

def books_starting_with_the(books):
    return [book for book in books if book['title'].startswith('The')]

def books_by_authors_with_t(books):
    return [book for book in books if 't' in book['author'].lower()]

def books_after_1992(books):
    return len([book for book in books if book['publication_year'] > 1992])

def books_before_2004(books):
    return len([book for book in books if book['publication_year'] < 2004])

def isbn_for_author(books, author_name):
    return [book['isbn'] for book in books if author_name.lower() in book['author'].lower()]

def list_books_alphabetically(books, descending=False):
    return sorted(books, key=lambda x: x['title'], reverse=descending)

def list_books_chronologically(books, descending=False):
    return sorted(books, key=lambda x: x['publication_year'], reverse=descending)

def list_books_grouped_by_author_lastname(books):
    books_by_author = {}
    for book in books:
        author_lastname = book['author'].split()[-1]
        if author_lastname not in books_by_author:
            books_by_author[author_lastname] = []
        books_by_author[author_lastname].append(book)
    return books_by_author

def list_books_grouped_by_author_firstname(books):
    books_by_author = {}
    for book in books:
        author_firstname = book['author'].split()[0]
        if author_firstname not in books_by_author:
            books_by_author[author_firstname] = []
        books_by_author[author_firstname].append(book)
    return books_by_author