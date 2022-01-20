#include <iostream>
#include <ctime>
#include <string>

using namespace std;

void Hra(void);
int rozdatKarty(int, string);
void dalsiKarta(int&);
void Rozhodnuti(int, int);
int nahodneCislo(int, int);

void main() {

	char dalsiHra = 'n';

	do {
		Hra();

		cout << endl;
		cout << "Chcete hrat dalsi hru (a/n)? ";
		cin >> dalsiHra;
	} while (dalsiHra == 'A' || dalsiHra == 'a');
}

void Hra(void) {
	cout << "Vitejte u hospodske verze BlackJacku!" << endl;
	cout << "Pravidla hry: " << endl;
	cout << " - Hrac i Dealer na zacatku hry dostanou po jedne karte" << endl;
	cout << " - Zacina hrac, ktery se rozhoduje zda bude tahat dalsi karty, pricemz nesmi presahnout hranici 21" << endl;
	cout << " - Pote hraje Dealer, ktery taha karty dokud nema minimalne 17 bodu" << endl;
	cout << " - Po konci tazeni obou hracu se vyhodnoti vysledky, remiza jde ve prospech Dealera" << endl;
	cout << "---------------------------------------------------";
	srand((int)time(0));
	cout << "---------------------------------------------------" << endl;
	cout << "Hrac - ";
	int Hrac = rozdatKarty(1, "Vase karty jsou: ");
	cout << endl;
	cout << endl << "---------------------------------------------------" << endl;
	cout << "Dealer - ";
	int Dealer = rozdatKarty(1, "Karty Dealera jsou: ");
	cout << endl;

	dalsiKarta(Hrac);
	cout << endl;

	while ((Dealer < 17) && (Hrac <= 21))
	{
		Dealer += rozdatKarty(1, "Dealer vzal dalsi kartu. ");
		cout << endl;
		cout << "Dealer ma prave hodnotu: " << Dealer << endl;
	}
	cout << endl << "---------------------------------------------------" << endl;
	cout << "Vase hodnota karet je: " << Hrac << endl;
	cout << "Dealerova hodnota karet je: " << Dealer << endl;
	cout << endl << "---------------------------------------------------" << endl;

	Rozhodnuti(Hrac, Dealer);
}

void Rozhodnuti(int Hrac, int Dealer)
{
	if (Hrac == 21)
		cout << "Mate celkem 21. Vyhravate hru!" << endl;
	else if ((Hrac < 21) && (Hrac > Dealer))
		cout << "Mate blize k 21, vyhravate hru!" << endl;
	else if ((Dealer > 21) && (Hrac < 21))
		cout << "Dealer je pres, vyhravate hru!" << endl;
	else if ((Hrac > 21))
		cout << "Mate pres 21, prohravate hru!" << endl;
	else if ((Dealer >= Hrac))
		cout << "Bohuzel, prohravate hru!" << endl;
}

int rozdatKarty(int hodnota_karty, string zprava)
{
	int vracena_hodnota = 0;
	int hodnota = 0;

	for (int i = 0; i <= hodnota_karty; i++)
	{
		int karty = i;
		while (karty--)
		{
			hodnota = nahodneCislo(1, 11);
			cout << "Vytahnuta karta ma hodnotu: " << hodnota << " ";
			if (karty)
				cout << " , ";
			vracena_hodnota += hodnota;
		}
	}
	return vracena_hodnota;
}

void dalsiKarta(int& skoreHrace)
{
	int pocet_karet = 0;
	char dalsi_hit = "a" || "n";
	int hodnota_celkem = 0;
	hodnota_celkem = skoreHrace;
	cout << endl << "---------------------------------------------------" << endl;
	cout << "Budete chtit dalsi kartu? (a/n) ";
	cin >> dalsi_hit;
	cout << endl << "---------------------------------------------------" << endl;
	while (dalsi_hit == 'A' || dalsi_hit == 'a')
	{
		int nahoda = nahodneCislo(1, 11);
		cout << "Vytahnuta karta ma hodnotu: " << nahoda << endl;
		hodnota_celkem += nahoda;

		if ((hodnota_celkem > 0) && (hodnota_celkem < 21))
			pocet_karet += 1;
		cout << "Vas celkovy pocet je: " << hodnota_celkem << endl;
		cout << "---------------------------------------------------" << endl;
		if (hodnota_celkem > 21)
			break;
		cout << "Budete chtit dalsi kartu? (a/n) ";
		cin >> dalsi_hit;
	}
	skoreHrace = hodnota_celkem;
}

int nahodneCislo(int spodniHranice, int horniHranice)
{
	return 1 + rand() % (horniHranice - spodniHranice + 1);
}