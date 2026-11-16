# Singleton 패턴 실습

## 선택 언어와 실행 환경

- 언어: Python
- 실행 환경: Python 3.9.6
- 별도 패키지 설치는 필요하지 않습니다.

## 실행 방법

저장소 폴더에서 다음 명령을 실행합니다.

```bash
python3 singleton.py
```

## 실행 결과

```text
같은 인스턴스인가요? True
첫 번째 변수에서 설정한 counter: 42
두 번째 변수에서 읽은 counter: 42
```

## 구현 설명

싱글톤 객체는 `AppSettings` 클래스의 클래스 변수 `_instance`에 저장했습니다. `AppSettings()`를 호출하면 `__new__`가 `_instance`를 먼저 확인해서, 객체가 없을 때만 새로 만들어 저장하고 이미 있으면 그 객체를 그대로 돌려줍니다. 그래서 몇 번을 요청해도 새 객체가 만들어지지 않습니다. 실행 결과에서 `first is second`가 `True`로 나오고, `first.counter = 42`로 바꾼 값이 `second.counter`로도 42가 읽혀서 두 변수가 같은 객체를 공유한다는 걸 확인했습니다. 이 예제는 과제 조건에 맞춰 단일 프로세스, 단일 스레드 환경만 가정했습니다.
