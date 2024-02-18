from bs4 import BeautifulSoup

def znajdz_tytuly_i_ceny(html):
    tytuly_i_ceny = []
    soup = BeautifulSoup(html, 'html.parser')

    ksiazki = soup.find_all('div', class_='ksiazka')

    #zakladaja ze te dane znajduje sie w div lub czym o class ksiazka i tytul jest w h2 za dlugie sa tamte strony nie chcialo mi sie szuac tak samo z cena pzodro
    for ksiazka in ksiazki:
        tytul = ksiazka.find('h2').text.strip() 
        cena = ksiazka.find('span', class_='cena').text.strip()
        tytuly_i_ceny.append((tytul, cena))

    return tytuly_i_ceny



wynik = znajdz_tytuly_i_ceny(html)

for tytul, cena in wynik:
    print("Tytuł:", tytul)
    print("Cena:", cena)
    print()
