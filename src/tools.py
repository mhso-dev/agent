from datetime import datetime
from zoneinfo import ZoneInfo

from langchain_core.tools import tool


@tool
def get_time(timezone: str = "Asia/Seoul") -> str:
    """주어진 시간대(예: 'Asia/Seoul', 'UTC')의 현재 시각을 ISO 형식으로 반환합니다."""
    return datetime.now(ZoneInfo(timezone)).isoformat()


@tool
def calculate(expression: str) -> str:
    """파이썬 산술 표현식을 받아 계산 결과를 문자열로 반환합니다.
    안전을 위해 +, -, *, /, ., 숫자, 괄호만 허용합니다.
    예: '12 * (3 + 4)' -> '84'"""
    allowed = set("0123456789.+-*/() ")
    if not set(expression).issubset(allowed):
        return "허용되지 않은 문자가 있습니다."
    try:
        return str(eval(expression))
    except Exception as exc:
        return f"계산 실패: {exc}"


@tool
def fake_search(query: str) -> str:
    """가짜 웹 검색을 흉내냅니다. 실제로는 외부 API를 부르지 않고 학습용 더미 결과를 반환합니다."""
    return f"'{query}'에 대한 더미 검색 결과: 관련 기사 3건이 발견되었습니다."


@tool
def multiply(a: int, b: int) -> int:
    """두 정수 a와 b를 곱한 값을 반환합니다."""
    return a * b
