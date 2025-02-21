### 1. 설치 방법
```
pip install tcmaker
```

### 2. 데이터 형식 지정 예시
실행 폴더에 `format.txt`파일이 있어야 합니다. 이 파일에는 데이터의 형식을 지정합니다.

```format.txt
[Var]
n: 1~100
x: -1000~1000
m: 1~n
y: 0~1

[Format]
n m
drept(n,x,' ')
rept(m,y,'\n')
```
여기서 `rept(반복횟수,변수명,구분자)` 명령이 있습니다. `drept`명령은 사용법은 동일한데 데이터의 중복없이 반복하는 명령입니다. 값의 범위는 변수 정의에 따릅니다.

위 명령으로 생성되는 데이터의 예시
```
5 4
-12 123 2 -982
0
1
1
0
```

### 3. 실행 방법 예시
아래와 같은 파일을 만들어서 실행합니다.
```
import tcmaker

start_n = 1    # 데이터 시작 번호
end_n = 10     # 데이터 끝 번호

for i in range(start_n, end_n+1):
  format_file = 'format.txt'        # 데이터 형식 지정 파일명
  input_file = f'test{i:02d}.in'    # 만들 입력 파일명
  output_file = f'test{i:02d}.out'  # 만들 출력 파일명
  run_file = 'solve.py'             # 정답 코드 파일명
  terminal = 'PowerShell'           # 터미널 종류(PowerShell 또는 아무거나)

  tcm = tcmaker.tcmaker()
  tcm.generate(format_file, input_file, output_file, run_file, terminal)
```

### 4. 기타
아직 부족한 점이 많습니다. 변수명 정의 또는 `rept`명령에 변수와 수식 혼용 사용가능합니다. 차차 업데이트하도록 하겠습니다.
