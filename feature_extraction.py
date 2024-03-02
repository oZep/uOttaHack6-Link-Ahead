from urllib.parse import urlparse

other_features = [
    "qty_mx_servers", # DNS lookup
    "qty_ip_resolved", # Involves a DNS lookup
    "email_in_url", # Simple Regex
    "ttl_hostname", # Involves a DNS lookup
    "tls_ssl_certificate", # Involves actually contacting the host?
    ]


symbol_to_name = {
    "qty_dot": ".",
    "qty_hyphen": "-",
    "qty_underline": "_",
    "qty_slash": "/",
    "qty_questionmark": "?",
    "qty_at": "@",
    "qty_and" : "&",
    "qty_exclamation": "!",
    "qty_equal": "=",
    "qty_space": " ",
    "qty_tilde": "~",
    "qty_comma": ",",
    "qty_plus": "+",
    "qty_asterisk": "*",
    "qty_hashtag": "#",
    "qty_dollar": "$",
    "qty_percent": "%"
}

name_to_symbol = { v: k for k, v in symbol_to_name.items() }

vowels = "aeiuyo"

def count_vowels(s):
    num = 0
    for i in s:
        if i in vowels:
            num += 1
    return num


def feature_extract_substr(s):
    features = {}

    # Count stuff
    features["length"] = len(s)
    features["vowels"] = count_vowels(s)

    # Do all the symbol-counting features
    for c in symbol_to_name.values():
        features[name_to_symbol[c]] = s.count(c)
    return features


def feature_extract_url(url):
    # Split up the URL into the components we're gonna measure
    u = urlparse(url)

    if len(u.path.split("/")) > 1:
        final_file = u.path.split("/")[-1]
        directory = u.path[:len(u.path)-len(final_file)]
    else:
        final_file = u.path.split("/")[-1]
        directory = ""

    params = u.query
    domain = u.netloc

    # Get their features
    url_histogram = feature_extract_substr(u)
    file_histogram = feature_extract_substr(final_file)
    directory_histogram = feature_extract_substr(directory)
    params_histogram = feature_extract_substr(params)
    domain_histogram = feature_extract_substr(domain)

    # Rename them into a big array like the CSV we found on Kaggle
    features = {}
    for k in url_histogram:
        features[k+"_url"] = url_histogram[k]

    for k in file_histogram:
        features[k+"_file"] = file_histogram[k]

    for k in params_histogram:
        features[k+"_params"] = params_histogram[k]

    for k in directory_histogram:
        features[k+"_directory"] = directory_histogram[k]

    for k in domain_histogram:
        features[k+"_domain"] = domain_histogram[k]


    return features
    
    

        
