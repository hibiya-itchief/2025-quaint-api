import jwt
from datetime import datetime, timedelta, timezone
import ulid
from app.config import settings

def create_qr_jwt(user_id, groups, name):
    payload = {
        "sub": user_id,  # ユーザーID
        "groups": groups,  # 権限（例: ["guest"]）
        "name": name,      # 表示名（任意）
        "exp": int((datetime.now(timezone.utc) + timedelta(days=30)).timestamp()), # 有効期限
        "iss": "quaint-api", # 独自issuer
        "jti": ulid.new().str          # 一意ID
    }
    token = jwt.encode(payload, settings.jwt_privatekey, algorithm="RS256")
    return token