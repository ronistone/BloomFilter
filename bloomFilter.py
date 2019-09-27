import math
from bitarray import bitarray
from hashlib import md5


class BloomFilter:

    def __init__(self, numberItems: float, falsePositiveProbability: float):
        self._numberItems = numberItems
        self._falsePositiveProbability = falsePositiveProbability

        self._numberHash = self._calculateNumberHash()
        self._vetorSize = self._calculateVetorSize()

        self._bit_vetor = self._initializeBitVetor()

    def _calculateVetorSize(self) -> float:
        return math.ceil(-(self._numberItems * math.log(self._falsePositiveProbability)) / (math.log(2) * math.log(2)))

    def _calculateNumberHash(self) -> float:
        return math.ceil(-(math.log2(self._falsePositiveProbability)))

    def _initializeBitVetor(self) -> bitarray:
        bits = bitarray(self._vetorSize)
        bits.setall(0)
        return bits

    @staticmethod
    def _calculateHash(value: str, i: int):
        return int.from_bytes(md5(str(i).encode() + value.encode()).digest(), "big")

    def insert(self, value: str) -> None:
        for i in range(self._numberHash):
            hashValue = self._calculateHash(value, i)
            self._bit_vetor[hashValue % self._vetorSize] = True

    def check(self, value: str) -> bool:
        for i in range(self._numberHash):
            hashValue = self._calculateHash(value, i)
            if not self._bit_vetor[hashValue % self._vetorSize]:
                return False

        return True


if __name__ == '__main__':
    n = float(input("Insert the number of items: "))
    k = float(input("Insert the false positive probability: "))

    bloom = BloomFilter(n, k)

    print("Number of hashs: ", bloom._numberHash)
    print("Vector Size: ", bloom._vetorSize)

    while True:
        option = input("1 - insert\n2 - check\n0 - exit\noption: ")

        if option == "1":
            value = input("Insert value to insert: ")
            bloom.insert(value)
        elif option == "2":
            value = input("Insert value to check: ")
            if bloom.check(value):
                print(value, "exist")
            else:
                print(value, "not exist")
        elif option == "0":
            break
