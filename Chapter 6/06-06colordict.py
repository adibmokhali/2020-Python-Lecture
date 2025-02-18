color = dict(검은색='black', 흰색='white', 녹색='green', 파란색='blue')
print(color)

print(color.get('녹색'))
print(color.get('노란색'))
print()

color['노란색'] = 'yellow'
print(color)
print()

c = '흰색'
print('삭재: %s %s' % (c, color.pop('흰색')))
print(color)
c = '빨간색'
print('삭제: %s %s' % (c, color.pop('없어요')))

print('임의 삭제: {} '.format(color.popitem()))
print('임의 삭제 후: {} '.format(color))
del color[c]
print('{} 삭제 후: {}'.format(c, color))

color.clear()
print(color)