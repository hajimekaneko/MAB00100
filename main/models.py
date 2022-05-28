import uuid
from django.db import models
from django.utils import timezone

# AbstractBaseUserを利用してUserモデルをカスタマイズ
# PermissionsMixinを用いてUserの認証を行う
# BaseUserManager利用してUserManagerモデルをカスタマイズ
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager

class UserProfileManager(BaseUserManager):
    """Manager for user profiles"""

    # ユーザを作成するメソッド
    def create_user(self, email, username, password=None):
        """Create a new user profile"""

        # emailが入力されていないときはValueErrorを呼び出す
        if not email:
            raise ValueError('User must have an email address')

        # emailのドメインを小文字に変換
        email = self.normalize_email(email)
        # UserProfileモデルを参照してuserを定義
        user = self.model(email=email, username=username)
        # userが入力したパスワードをハッシュ化
        user.set_password(password)
        # settings.pyでdefaultに設定されているDBに保存
        user.save(using=self._db)

        return user

    def create_superuser(self, email, username, password):
        """Create and save a new superuser with given details"""

        # 上記create_userを利用
        user = self.create_user(email, username, password)

        # superuserの権限を適用
        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)

        return user


class UserProfile(AbstractBaseUser, PermissionsMixin):
    """Database model for users in the system"""

    # カラム名 = データ型（オプション）
    email = models.EmailField(max_length=255, unique=True)
    username = models.CharField(max_length=255,  unique=True, null=False)
    userId = models.CharField(primary_key=True, max_length=255,  editable=True)
    loggedin = models.BooleanField(default=False, help_text='ログイン状態か')
    created = models.DateTimeField('入会日', default=timezone.now)
    # ユーザが退会したらここをFalseにする（論理削除）
    is_active = models.BooleanField(default=True)
    # 管理画面にアクセスできるか
    is_staff = models.BooleanField(default=False)
    # Managerのメソッドを使えるようにする
    objects = UserProfileManager()
    # emailを利用したログイン認証に変更
    USERNAME_FIELD = 'username'
    # 必須項目追加
    REQUIRED_FIELDS = ['email']


    # 1つのnameフィールドで表示したいので、既存のメソッドをオーバーライド
    def get_full_name(self):
        """Retrieve full name of user"""
        return self.username

    def get_short_name(self):
        """Retrieve short name of user"""
        return self.username

    def __str__(self):
        return self.email