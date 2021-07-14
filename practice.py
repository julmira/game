# [모종 고르기]

seed_chioce = input("고추, 감자, 양파 중 당신이 심을 모종을 골라주세요. : ")
print("당신은 {0}을/를 고르셨습니다.".format(seed_chioce))

count = 2

print("[1일차] 당신은 밭고랑에 {0} 모종을 심었습니다.".format(seed_chioce))

while count > 0:
    print("남은 행동력 : {0}".format(count))
    print("이제 무엇을 하시겠습니까? :")
    act = input("a.약치기  b.물주기  c.거름주기  d.행동 종료 : ")
    if act == "a":
        count -= 1
        print("당신은 약을 뿌렸습니다. 해충이 박멸되었습니다.")
    elif act == "b":
        count -= 1
        print("당신은 물을 주었습니다. 식물이 싱싱해집니다.")
    elif act == "c":
        count -= 1
        print("당신은 거름을 주었습니다. 식물이 성장이 빨라집니다.")
    else:
        break
print("다음 날로 넘어갑니다.")