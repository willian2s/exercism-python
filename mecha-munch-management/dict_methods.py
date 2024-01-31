"""Functions to manage a users shopping cart items."""


def add_item(current_cart: dict, items_to_add: list):
    """Add items to shopping cart.

    :param current_cart: dict - the current shopping cart.
    :param items_to_add: iterable - items to add to the cart.
    :return: dict - the updated user cart dictionary.
    """

    for item in items_to_add:
        if item in current_cart:
            current_cart[item] += 1
        else:
            current_cart[item] = 1
    return current_cart


def read_notes(notes: list):
    """Create user cart from an iterable notes entry.

    :param notes: iterable of items to add to cart.
    :return: dict - a user shopping cart dictionary.
    """

    return dict.fromkeys(notes, 1)


def update_recipes(ideas, recipe_updates):
    """Update the recipe ideas dictionary.

    :param ideas: dict - The "recipe ideas" dict.
    :param recipe_updates: dict - dictionary with updates for the ideas section.
    :return: dict - updated "recipe ideas" dict.
    """

    ideas.update(recipe_updates)

    return ideas


def sort_entries(cart):
    """Sort a users shopping cart in alphabetically order.

    :param cart: dict - a users shopping cart dictionary.
    :return: dict - users shopping cart sorted in alphabetical order.
    """

    sort = dict(sorted(cart.items()))
    return sort


def send_to_store(cart, isle_mapping):
    """Combine users order to isle and refrigeration information.

    :param cart: dict - users shopping cart dictionary.
    :param isle_mapping: dict - isle and refrigeration information dictionary.
    :return: dict - fulfillment dictionary ready to send to store.
    """

    fulfillment_cart = []
    for item in cart:
        quantity = cart[item]
        isle, refrigeration = isle_mapping[item]
        fulfillment_cart.append((item, quantity, isle, refrigeration))

    fulfillment_cart.sort(reverse=True)

    result = {}
    for item, quantity, isle, refrigeration in fulfillment_cart:
        result[item] = [quantity, isle, refrigeration]

    return result


def update_store_inventory(fulfillment_cart, store_inventory):
    """Update store inventory levels with user order.

    :param fulfillment cart: dict - fulfillment cart to send to store.
    :param store_inventory: dict - store available inventory
    :return: dict - store_inventory updated.
    """

    for item, details in fulfillment_cart.items():
        quantity_ordered, _, _ = details
        if item in store_inventory:
            store_inventory[item][0] -= quantity_ordered
            if store_inventory[item][0] <= 0:
                store_inventory[item][0] = 'Out of Stock'
    return store_inventory
