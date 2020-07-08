class Vending:
    def __init__(self):
        self.p = {'콜라':500, '사이다':400, '환타': 600, '삼다수': 200, '탄산수': 150 }
        self.n = {1:'콜라', 2:'사이다', 3:'환타', 4:'삼다수', 5:'탄산수'}
        self.stock = {1:5, 2:5, 3:5, 4:5, 5:5 }
        self.money = 0
    
    def showmenu(self):
        print('[메뉴정보]')
        i = 1
        for k, v in self.p.items():
            print(str(i)+'.', k, v, '원')
            i+=1
        print()                      

    def inputmoney(self):
        while True:
            try:
                self.money += int( input('돈 투입:'))
            except Exception as e:
                print(e)
                continue
            else:
                print('투입금액:', self.money)
                print()
                break

    def buy(self):
        try:
            n = int(input('번호선택(종료:0):'))
        except Exception as e:
            print(e)
        else:
            if n == 0:
                return False
            if n >= 1 and n <= len(self.p):

                if self.stock[n] > 0 :

                    if self.money >= self.p[ self.n[n] ]:
                        print( self.n[n], '구입완료' )
                        self.money = self.money - self.p[ self.n[n]]


                        self.stock[n] = self.stock[n] - 1
                        print( self.n[n], ' : ' , self.stock[n] , '개 남음')

                        print('잔액', self.money)
                    else:
                        print('잔액부족')
                        self.inputmoney()
                else:
                    print( self.n[n], '재고없음' )
                
            else:
                print('잘못된 번호')
        return True

v = Vending()
v.showmenu()
v.inputmoney()

while v.buy():
    print()

print('자판기 종료')
print('반환 : ', v.money , '원')


