import wikipediaapi
from math import ceil
# initialize wikipedia
wiki_wiki = wikipediaapi.Wikipedia('en',extract_format=wikipediaapi.ExtractFormat.WIKI)

page_py = wiki_wiki.page('senegal')
def wiki_extract_all(sujet,):
    """
    # fonction qui return les titres des sections et les textes associés aux sections
    # sous forme d'un dictionnaire {titre:texte}
    # d'un article wikipédia nommé "sujet" (string) s'il existe
    """
    wiki_page = wiki_wiki.page(sujet)
    exists = wiki_page.exists()

    if not exists:
        return {}

    sections = wiki_page.sections
    titles = [section.title for section in sections]
    texts = [section.text for section in sections]
    zip_dict = zip(titles, texts) # pairing
    wiki_dic = dict(zip_dict)
    return wiki_dic

def wiki_extract_summary(sujet,):
    """
    # fonction qui return le résumé texte
    # d'un article wikipédia nommé "sujet" (string) s'il existe
    """
    wiki_page = wiki_wiki.page(sujet)
    exists = wiki_page.exists()
    if not exists:
        return ""
    return wiki_page.summary

def wiki_extract_summary_part(sujet, part):
    """
    # fonction qui return le résumé texte
    # d'un article wikipédia nommé "sujet" (string) s'il existe
    # part est un pourcentage
    """
    wiki_page = wiki_wiki.page(sujet)
    exists = wiki_page.exists()
    if not exists:
        return ""
    summary = wiki_page.summary
    return summary[:min(ceil(len(summary)*part),600)]

def wiki_extract_categories(sujet,):
    """
    # fonction qui return les catégories auxquelles appartient 
    # un article wikipédia nommé "sujet" (string) s'il existe,
    # sous forme d'un dictionnaire catégorie / value
    """
    wiki_page = wiki_wiki.page(sujet)
    exists = wiki_page.exists()
    if not exists:
        return ""
    return wiki_page.categories

def wiki_extract_pages_f_category(category,max_number=1):
    """
    # fonction inverse qui return les pages auxquelles appartenant à une catégorie
    # un article wikipédia nommé "sujet" s'il existe,
    # sous forme d'une liste de pages
    """

    # essayer de comprendre avec la doc
    # cat = wiki_wiki.page("Category:%s}" %category)
    # print(cat)
    # categorymembers = cat.categorymembers.values()
    # return categorymembers


def wiki_articles_all_languages(page):
    """
    # fonction qui return les pages dans toutes les langues trouvées d'un article à partir d'une pag
    # déjà obtenue 
    """
    wikis = page.langlinks
    return wikis