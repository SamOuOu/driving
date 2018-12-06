#檢視是否可以開車
country = input('請問你是哪個國家？')
age = input('請問你幾歲？')
age = int(age)

if country == '台灣' or '臺灣':
    if age >= 18:
        print('你可以在台灣考駕照開車撞人')
    else:
        print('你不能考駕照開車撞人')
        if country == '美國' or 'USA':
            if age >= 16:
                print('你可以在美國考駕照開車撞人')
            else:
                print('你不能考駕照開車撞人')
        