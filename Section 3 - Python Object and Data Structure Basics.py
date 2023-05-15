23 % 2

2**3

0.1+0.2-0.3

a = a + a

type(a)

text = "hello myself"
len(text)

text[-3]

texttwo = 'abcdefgh'
texttwo[2:]
texttwo[:3]
texttwo[3:6]
texttwo[1:3]
texttwo[::]
texttwo[::3]
texttwo[2:7:2]
texttwo[::-1]

'Z' * 10 # 'ZZZZZZZZZZ'
'2' + 3 # err

'str'.upper() #'STR
'aSdEfG'.lower() #'asdefg'

'this is a string'.split('i') #['th', 's ', 's a str', 'ng']


#String formatting

print('this str is {}'.format('formatted =O')) #this str is formatted =O

print('the {} is in the {}'.format('banana', 'business')) #the banana is in the business

print('the {1} is in the {0}'.format('banana', 'business')) #the business is in the banana

print('the {1} is in the {1}'.format('banana', 'business')) #the business is in the business

print('the {a} {c} {b}'.format(a='something', b='else', c='magic')) #the something magic else

result = 100/777

print('the result was {r:10.3}'.format(r=result)) #the result was 0.129


#f formatting

name = 'Mario'

print(f'{name} Bros') #Mario Bros


#lists

my_list = [1,2,3]

another_list = ["string", 123, 12.34, [1,2]]

len(another_list) # 4

another_list[3][1] # 2

my_list + another_list # [1, 2, 3, 'string', 123, 12.34, [1, 2]]

another_list[0] = "STRING CAPS"
another_list # ['STRING CAPS', 123, 12.34, [1, 2]]

my_list.append(4)
my_list #[1, 2, 3, 4]

my_list.pop() #4 -> object removed
my_list #[1, 2, 3]

another_list.pop(2) #12.34
another_list.pop() # default is .pop(-1)

char_list = ['a', 'c', 'd', 'h', 'b']
num_list = [3,7,4,1,5]

char_list.sort()
char_list #['a', 'b', 'c', 'd', 'h']

None #-> none object

num_list.reverse()
num_list #[5, 1, 4, 7, 3] -> la da vuelta