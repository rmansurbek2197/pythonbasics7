class SetAmallari:
    def __init__(self, set1, set2):
        self.set1 = set1
        self.set2 = set2

    def birlashtirma(self):
        return self.set1.union(self.set2)

    def qatnashma(self):
        return self.set1.intersection(self.set2)

    def farq(self):
        return self.set1.difference(self.set2)

    def simmetrikFarq(self):
        return self.set1.symmetric_difference(self.set2)

    def kiritish(self, element):
        self.set1.add(element)

    def ochirish(self, element):
        self.set1.remove(element)

def main():
    set1 = {1, 2, 3, 4}
    set2 = {3, 4, 5, 6}
    amallar = SetAmallari(set1, set2)
    print("Birlashtirma:", amallar.birlashtirma())
    print("Qatnashma:", amallar.qatnashma())
    print("Farq:", amallar.farq())
    print("Simmetrik farq:", amallar.simmetrikFarq())
    amallar.kiritish(7)
    print("Set1 ga 7 qo'shildadi:", amallar.set1)
    amallar.ochirish(4)
    print("Set1 dan 4 ochirildi:", amallar.set1)

if __name__ == "__main__":
    main()