animals = input('Heyvanlari girin: ').split(', ')
prices = { 'inek': 500, 'toyuq': 50, 'qoyun': 120, 'at': 900, 'keci': 210 }
# print('Umumi qiymet:', sum(map(lambda animal: prices[animal], animals)))



try:
    if not 3 <= len(animals) <= 10:
        raise ValueError
    print('Umumi qiymet:', sum(map(lambda animal: prices[animal], animals)))
except KeyError as message:
    print("Heyvanin adini sehv daxil etmisiniz")
except ValueError:
    print("Daxil etdiyiniz say 10-dan artiq və ya 3-dən az olmamalidir")
except Exception:
    print("Sistemde bilinmeyen bir xeta bas verdi. Yeniden yoxlamaginiz xahis olunur.")