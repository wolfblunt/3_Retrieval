from bs4 import BeautifulSoup as bs
from operator import itemgetter
import requests as req

base_url = 'https://www.flipkart.com'

# this function takes the input string which we want to search and convert it into a search page url
def get_search_query(user_input_string):
    search_query = '/search?q={}'
    query = user_input_string.replace(' ', '+')
    return search_query.format(query)


# this function return product page url from given product card
def get_product_url(card):
    if card.find('a'):
        url = card.find('a').get('href')
        return base_url + url


# this function return product name from given product card
def get_product_name(card):
    block_name = card.find('a', {'class': 's1Q9rs'})
    block_name2 = card.find('div', {'class': '_4rR01T'})
    if block_name != None:
        return block_name.text.strip()
    elif block_name2 != None:
        return block_name2.text


# this function return product selling price given product card
def get_product_price(card):
    selling_price_block = card.find('div', {'class': '_30jeq3'})
    if selling_price_block != None:
        return selling_price_block.text


# this function return product MRP, selling price and discount from given product card
def get_product_rating(card):
    product_rating = card.find('div', {'class': '_3LWZlK'})
    if product_rating != None:
        return product_rating.text


# this function return product selling price given product card
def get_product_image(card):
    product_image = card.find('img', {'class': '_396cs4 _3exPp9'})
    if product_image != None:
        return product_image.get('src')


# this function takes search page url and return all the possible product cards
def get_product_cards(search_page_url):
    page_content = req.get(search_page_url, headers={"User-Agent": "Requests"}).content
    bsoup_object = bs(page_content)
    cards = bsoup_object.find_all('div', {'class': '_4ddWXP'})
    cards2 = bsoup_object.find_all('div', {'class': '_2kHMtA'})
    product_cards = []
    for card in cards:
        product_cards.append(card)
    for card in cards2:
        product_cards.append(card)
    return product_cards


# FINAL FUNCTION, In this function we will call each and every function declared above
def get_products_by_name_flipkart(product_name):
    url = base_url + get_search_query(product_name)
    products_cards = get_product_cards(url)
    product_details = []
    length = len(products_cards)
    for index, card in enumerate(products_cards):
        product_dict = {}
        name = get_product_name(card)
        if name != None:
            product_dict["Product Name"] = name
            product_dict["Product Price"] = get_product_price(card)[1:]
            product_dict["Product Rating"] = get_product_rating(card)
            product_dict["Product Url"] = get_product_url(card)
            product_dict["Product Image Url"] = get_product_image(card)
            product_dict["Source"] = "Flipkart"
            product_dict["index"] = (length - index) / length
            product_details.append(product_dict)
    return product_details


# ranking algorithm of e-commerce on basis of product title and rating
def rank_algorithm_ecommerce(product_details, query):
    words = query.split(' ')

    for product in product_details:
        placement_score = product['index'] * 30
        rating_score = 0
        name_score = 0
        if product['Product Rating'] is not None:
            rating_score = float(product['Product Rating']) * 7

        if product['Product Name'] is not None:
            occur = 0
            for word in words:
                if word.lower() in product['Product Name'].lower():
                    occur = occur + 1
            name_score = (occur / len(words)) * 35

        total_score = name_score + rating_score + placement_score
        product['Score'] = total_score

    ranked_product_details = sorted(product_details, key=itemgetter('Score'), reverse=True)

    return ranked_product_details