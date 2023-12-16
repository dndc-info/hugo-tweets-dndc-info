param (
    [string]$cm
)

# 変更をステージング
git add .

# コミット
git commit -m $cm

# プッシュ
git push origin main
