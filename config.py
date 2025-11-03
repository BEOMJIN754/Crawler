import os
from dotenv import load_dotenv

# .env 파일이 존재하면 해당 파일의 환경 변수를 로드합니다.
load_dotenv()

# 환경 변수에서 "GOOGLE_MAPS_API_KEY" 값을 가져옵니다.
API_KEY = os.getenv("GOOGLE_MAPS_API_KEY")

# Tier별 레스토랑 수집 개수 설정
# grid_tier.csv의 tier 값에 따라 수집할 레스토랑 개수를 지정합니다.
TIER_RESTAURANT_COUNT = {
    "HOT": 80,   # 핫플레이스 지역
    "MID": 50,   # 중간 지역
    "RES": 25    # 주거 지역
}
