def build_info(first_name, last_name, **details): # **details is an empty dictionary
    """Create dictionary of user information."""
    info = {}
    info['first_name'] = first_name
    info['last_name']  = last_name

    for key, value in details.items():
        info[key] = value

    return info
