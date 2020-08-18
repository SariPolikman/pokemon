import requests

url_ = "https://pokeapi.co/api/v2/"


def pokemon(poke):
    return requests.get(url=f"{url_}pokemon/{poke}", verify=False).json()


def by_url(a_url):
    return requests.get(url=a_url, verify=False).json()


def chain(pid):
    poke_ = pokemon(pid)
    old_name = poke_['name']
    species_url = poke_['species']['url']
    evolution_chain_url = by_url(species_url)['evolution_chain']['url']
    chain = by_url(evolution_chain_url)['chain']

    return [old_name, chain]

