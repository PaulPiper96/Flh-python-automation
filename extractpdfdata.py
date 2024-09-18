from pdfquery import PDFQuery
'''
Die Datei extrahiert Daten aus dem Kundenfragebogen. Zuständig dafür ist die KLasse KFPDF. Etwaige Informationen werden mithilfe des 
pdfquerry Pakets verabeitet. Da eine Semantische Überpfrüfung etwas schwierig ist, zählt ein Zähler die gesammelten Elemente des 
Dokuments mit und extrahiert Infos an der relevanten Stelle.!!!!!Das Skript muss mit mehreren KFs getestet werden, da die IF-Abfragen gewisse
Strings überprüfen!!!!!
Des weiteren sollte sobald sich die Struktur des KFs ändert diese Datei angepasst werden!!!!
'''
# Stores relevant data inside the class
class KFinfos:
    def __init__(self, Geschaeftsname, Name, Emailmarkt, Adresse, weitereStandorte, Domainkaufen, Domain,
                 Emailweiterleiten, Emailerstellen, Emailadresse, EmailzurWeiterleitung, Emailhomepage,
                 duzenodersiezen, Theme, Font):
        self.Geschaeftsname = Geschaeftsname
        self.Name = Name
        self.Emailmarkt = Emailmarkt
        self.Adresse = Adresse
        self.weitereStandorte = weitereStandorte
        self.Domainkaufen = Domainkaufen
        self.Domain = Domain
        self.Emailweiterleiten = Emailweiterleiten
        self.Emailerstellen = Emailerstellen
        self.Emailadresse = Emailadresse
        self.EmailzurWeiterleitung = EmailzurWeiterleitung
        self.Emailhomepage = Emailhomepage
        self.duzenodersiezen = duzenodersiezen
        self.Theme = Theme
        self.Font = Font

    def print_attributes(self):
        for attr, value in self.__dict__.items():
            print(f"{attr}: {value}")


class KFPDF:
    def __init__(self):
        self.Geschaeftsname = "empty"
        self.Name = "empty"
        self.Emailmarkt = "empty"
        self.Adresse = "empty"
        self.weitereStandorte = False
        self.Domainkaufen = False
        self.Domain = "empty"
        self.Emailweiterleiten = False
        self.Emailerstellen = False
        self.Emailadresse = "empty"
        self.EmailzurWeiterleitung = "empty"
        self.Emailhomepage = "empty"
        self.duzenodersiezen = "empty"
        self.Theme = "empty"
        self.Font = "empty"

        self.createData()

    def createData(self):
        pdf = PDFQuery('/Users/pc/Desktop/FLHMEDIA/KF EDEKA Josephine Liehr, HP Business, LP, 3D.pdf')
        pdf.load()
        text_elements = pdf.pq('LTTextBoxHorizontal')  # LTTextBoxHorizontal, 'LTTextLineHorizontal, LTTextBoxHorizontal'
        self.iteratetroughpdf(text_elements)
        self.createKFInfos()

    def createKFInfos(self):
        _kfinfos = KFinfos(self.Geschaeftsname, self.Name, self.Emailmarkt, self.Adresse, self.weitereStandorte,
                           self.Domainkaufen, self.Domain, self.Emailweiterleiten, self.Emailerstellen, self.Emailadresse,
                           self.EmailzurWeiterleitung, self.Emailhomepage, self.duzenodersiezen, self.Theme, self.Font)
        _kfinfos.print_attributes()

    def printentiretree(self, level, textelement):
        print(f"{level} Element Type: {type(textelement).__name__} {textelement} {textelement.text}")

    def iteratetroughpdf(self, text_elements):
        level = 0
        for textelement in text_elements:
            level += 1
            if level == 3:
                self.Geschaeftsname = textelement.text
            if level == 4:
                self.Name = textelement.text
            if level == 6:
                self.Emailmarkt = textelement.text
            if level == 7:
                self.Adresse = textelement.text
            if level == 9 and (textelement.text.strip() in ["Ja", "ja", "JA"]):
                self.weitereStandorte = True
            if level == 13 and (textelement.text.strip() in ["Nein", "nein", "NEIN"]):
                self.Domainkaufen = True
            if level == 14 and self.Domainkaufen:
                self.Domain = textelement.text
            if level == 15 and (textelement.text.strip() in ["Ja", "ja", "JA"]):
                self.Emailerstellen = True
            if level == 16 and self.Emailerstellen:
                self.Emailadresse = textelement.text
            if level == 17 and (textelement.text.strip() in ["Ja", "ja", "JA"]):
                self.Emailweiterleiten = True
            if level == 41 and self.Emailweiterleiten:
                self.EmailzurWeiterleitung = textelement.text
            if level == 42:
                self.Emailhomepage = textelement.text
            if level == 43:
                self.duzenodersiezen = textelement.text
            if level == 45:
                self.Theme = textelement.text
            if level == 46:
                self.Font = textelement.text


# Creating an instance of KFPDF class
pdf = KFPDF()


