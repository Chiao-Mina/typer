from django.contrib import admin
from .models import Score


@admin.register(Score)  # 把 Score 這個資料模型註冊到管理後台
class ScoreAdmin(admin.ModelAdmin):  # 定義 Score 在後台的顯示方式
    list_display = (  # 後台列表頁「顯示哪些欄位」
        'user',        # 使用者（誰打的）
        'score',       # 分數
        'wpm',         # 每分鐘打字數（words per minute）
        'accuracy',    # 正確率
        'category',    # 題目分類
        'mode',        # 練習模式
        'created_at',  # 建立時間
    )

    list_filter = (  # 右側「篩選器」可以按這些欄位過濾
        'category',    # 依分類篩選
        'mode',        # 依模式篩選
        'created_at',  # 依時間篩選
    )

    search_fields = (  # 上方「搜尋框」可以搜尋這些欄位
        'user__username',  # 使用者的帳號名
        'category',        # 分類
    )