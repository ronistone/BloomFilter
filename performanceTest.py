from utils import track
from bloomFilter import BloomFilter
import unittest


class PerformanceTest(unittest.TestCase):

    def testBloomFilterVsPythonDataStructuresWith100kItems(self):
        testSize = 100000
        inputs = generateData(testSize)
        print("  ====   Testing with 100k  =====  ")
        testPythonDictionary(inputs, testSize)
        testBloomFilter(inputs, testSize)
        testPythonSet(inputs, testSize)
        testPythonList(inputs, testSize)
        print("==================================")

    def testBloomFilterVsPythonDataStructuresWith1kkItems(self):
        testSize = 1000000
        inputs = generateData(testSize)
        print("  ====   Testing with 1kk  =====  ")
        testPythonDictionary(inputs, testSize)
        testBloomFilter(inputs, testSize)
        testPythonSet(inputs, testSize)
        # testPythonList(inputs,testSize)
        print("==================================")

    def testBloomFilterVsPythonDataStructuresWith10kkItems(self):
        testSize = 10000000
        inputs = generateData(testSize)
        print("testing with 10kk")
        testPythonDictionary(inputs, testSize)
        testBloomFilter(inputs, testSize)
        testPythonSet(inputs, testSize)
        # testPythonList(inputs,testSize)


def testBloomFilter(inputs, testSize):

    print("Testing Bloom Filter With", testSize)
    bloom = testBloomFilterInserting(testSize, inputs)
    found = testBloomFilterChecking(bloom, inputs)
    assert found == testSize


def testPythonDictionary(inputs, testSize):
    print("Testing Dictionary With", testSize)
    dictionary = testPythonDictInserting(inputs)
    found = testPythonDictChecking(dictionary, inputs)
    assert found == testSize


def testPythonList(inputs, testSize):
    print("Testing List With", testSize)
    l = testPythonListInserting(inputs)
    found = testPythonListChecking(l, inputs)
    assert found == testSize


def testPythonSet(inputs, testSize):
    print("Testing Set With", testSize)
    s = testPythonSetInserting(inputs)
    found = testPythonSetChecking(s, inputs)
    assert found == testSize


@track
def testBloomFilterChecking(bloom: BloomFilter, data: list) -> int:
    found = 0
    for i in data:
        if bloom.check(i):
            found += 1
    return found


@track
def testBloomFilterInserting(testSize: int, data: list) -> BloomFilter:
    bloom = BloomFilter(testSize * 10, 0.01)

    for i in data:
        bloom.insert(i)
    return bloom


@track
def testPythonDictInserting(data: list) -> dict:
    d = {}
    for i in data:
        d[i] = True
    return d


@track
def testPythonDictChecking(d: dict, data: list) -> int:
    found = 0
    for i in data:
        if d.get(i) is not None:
            found += 1
    return found

@track
def testPythonListInserting(data: list) -> list:
    l = []
    for i in data:
        l.append(i)
    return l


@track
def testPythonListChecking(l: list, data: list) -> int:
    found = 0
    for i in data:
        if l.index(i) is not None:
            found += 1
    return found

@track
def testPythonSetInserting(data: list) -> set:
    l = set()
    for i in data:
        l.add(i)
    return l


@track
def testPythonSetChecking(s: set, data: list) -> int:
    found = 0
    for i in data:
        if i in s:
            found += 1
    return found


def generateData(quantity):
    return [str(i) for i in range(quantity)]
