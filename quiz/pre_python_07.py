"""7. 1부터 100까지 수의 합을 계산하고 있다. 
이 때 합이 최초로 1000을 넘게 하는 수가 무엇인지 코드를 만들고 답을 구하시오


<출력>
 45
"""
result = 0
for i in range(1,100):
	result += i
	if result > 1000:
		print(i) 
		break  

