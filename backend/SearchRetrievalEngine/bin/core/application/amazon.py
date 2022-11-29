from bs4 import BeautifulSoup as bs
import requests as req

base_url = 'https://www.amazon.in'

# this function takes the input string which we want to search and convert it into a search page url
def get_search_query(user_input_string):
    search_query = '/s?k={}'
    query = user_input_string.replace(' ', '+')
    return search_query.format(query)


# this function return product page url from given product card
def get_product_url(card):
    product_url_tag = card.find('a', {'class': 'a-link-normal s-no-outline'})
    if product_url_tag != None:
        url = product_url_tag.get('href')
        return base_url + url


# this function return product name from given product card
def get_product_name(card):
    block_name = card.find('span', {'class': 'a-size-base-plus a-color-base a-text-normal'})
    block_name2 = card.find('span', {'class': 'a-size-medium a-color-base a-text-normal'})
    if block_name != None:
        return block_name.text
    elif block_name2 != None:
        return block_name2.text


# this function return product selling price given product card
def get_product_price(card):
    selling_price_block = card.find('span', {'class': 'a-price-whole'})
    if selling_price_block != None:
        return selling_price_block.text


# this function return product MRP, selling price and discount from given product card
def get_product_rating(card):
    product_rating = card.find('span', {'class': 'a-icon-alt'})
    if product_rating != None:
        return product_rating.text[:3]


# this function return product MRP, selling price and discount from given product card
def get_product_image(card):
    product_image = card.find('img', {'class': 's-image'})
    if product_image != None:
        return product_image.get('src')


# this function takes search page url and return all the possible product cards
def get_product_cards(search_page_url):
    page_content = req.get(search_page_url, headers={"User-Agent": "Requests"}).content
    bsoup_object = bs(page_content)
    cards = bsoup_object.find_all('div', {'data-component-type': 's-search-result'})
    cards2 = bsoup_object.find_all('li', {'class': 'a-carousel-card'})
    product_cards = []
    for card in cards2:
        product_cards.append(card)
    for card in cards:
        product_cards.append(card)
    return product_cards


# FINAL FUNCTION, In this function we will call each and every function declared above
def get_products_by_name_amazon(product_name):
    url = base_url + get_search_query(product_name)
    products_cards = get_product_cards(url)
    length = len(products_cards)
    product_details = []
    for index, card in enumerate(products_cards):
        product_dict = {}
        name = get_product_name(card)
        if name != None:
            product_dict["Product Name"] = name
            product_dict["Product Price"] = get_product_price(card)
            product_dict["Product Rating"] = get_product_rating(card)
            product_dict["Product Url"] = get_product_url(card)
            product_dict["Product Image Url"] = get_product_image(card)
            product_dict["Source"] = "Amazon"
            product_dict["index"] = (length - index) / length
            product_details.append(product_dict)
    return product_details
