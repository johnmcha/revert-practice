
def func():
  print('func()에 진입했습니다.')
  try:
    print('try구문에 진입했습니다.')
    return
    print('try구문에 끝났습니다..')
  except:
    print('except구문에 진입했습니다.')
  finally:
    print('finally구문에 진입했습니다.')
  print('func()가 끝났습니다다')

func()
