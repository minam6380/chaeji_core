def generate_strategy(topic: str) -> str:
    return f'[전략 초안] {topic}: 결론→근거→절차→주의점'

if __name__ == '__main__':
    print(generate_strategy('테스트'))
