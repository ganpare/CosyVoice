#!/usr/bin/env python3
"""CosyVoice3 CPUモード動作確認スクリプト"""

import sys
sys.path.append('third_party/Matcha-TTS')
import os
os.environ['CUDA_VISIBLE_DEVICES'] = ''  # CPUモードを強制

from cosyvoice.cli.cosyvoice import AutoModel

def test_cosyvoice3():
    """CosyVoice3の動作確認"""
    print("=" * 60)
    print("CosyVoice3 CPUモード動作確認")
    print("=" * 60)

    # モデルのロード
    print("\n1. モデルをロード中...")
    try:
        cosyvoice = AutoModel(model_dir='pretrained_models/Fun-CosyVoice3-0.5B')
        print("✅ モデルのロードに成功しました！")
    except Exception as e:
        print(f"❌ モデルのロードに失敗しました: {e}")
        return False

    # 利用可能なスピーカーを確認
    print("\n2. 利用可能なスピーカーを確認中...")
    try:
        spks = cosyvoice.list_available_spks()
        print(f"✅ 利用可能なスピーカー: {spks}")
    except Exception as e:
        print(f"❌ スピーカー情報の取得に失敗しました: {e}")

    # 簡単な音声合成テスト（短いテキスト）
    print("\n3. 音声合成テストを実施中...")
    print("   テキスト: 'こんにちは、これはテストです。'")
    print("   ※ CPUモードのため時間がかかる場合があります...")

    try:
        import torchaudio
        text = 'こんにちは、これはテストです。'
        prompt_text = 'You are a helpful assistant.<|endofprompt|>希望你以后能够做的比我还好呦。'
        prompt_audio = './asset/zero_shot_prompt.wav'

        # 推論実行（stream=Falseで全体を一度に生成）
        for i, j in enumerate(cosyvoice.inference_zero_shot(
            text,
            prompt_text,
            prompt_audio,
            stream=False
        )):
            output_file = f'test_output_{i}.wav'
            torchaudio.save(output_file, j['tts_speech'], cosyvoice.sample_rate)
            print(f"✅ 音声ファイルを保存しました: {output_file}")

            # 音声ファイルの情報を表示
            waveform = j['tts_speech']
            duration = waveform.shape[1] / cosyvoice.sample_rate
            print(f"   サンプリングレート: {cosyvoice.sample_rate} Hz")
            print(f"   音声長: {duration:.2f} 秒")
            print(f"   チャンネル数: {waveform.shape[0]}")

        print("\n" + "=" * 60)
        print("🎉 動作確認が完了しました！")
        print("=" * 60)
        return True

    except Exception as e:
        print(f"❌ 音声合成に失敗しました: {e}")
        import traceback
        traceback.print_exc()
        return False

if __name__ == '__main__':
    success = test_cosyvoice3()
    sys.exit(0 if success else 1)
