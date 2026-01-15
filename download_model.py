#!/usr/bin/env python3
"""CosyVoice3モデルダウンロードスクリプト"""

from modelscope import snapshot_download

print("Fun-CosyVoice3-0.5B-2512モデルのダウンロードを開始します...")

snapshot_download(
    'FunAudioLLM/Fun-CosyVoice3-0.5B-2512',
    local_dir='pretrained_models/Fun-CosyVoice3-0.5B'
)

print("モデルのダウンロードが完了しました！")
