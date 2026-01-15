![SVG Banners](https://svg-banners.vercel.app/api?type=origin&text1=CosyVoice🤠&text2=Text-to-Speech%20💖%20Large%20Language%20Model&width=800&height=210)

**[English version / 英語版 README](README.md)**

## 👉🏻 CosyVoice 👈🏻

**Fun-CosyVoice 3.0**: [デモ](https://funaudiollm.github.io/cosyvoice3/); [論文](https://arxiv.org/pdf/2505.17589); [Modelscope](https://www.modelscope.cn/models/FunAudioLLM/Fun-CosyVoice3-0.5B-2512); [Huggingface](https://huggingface.co/FunAudioLLM/Fun-CosyVoice3-0.5B-2512); [CV3-Eval](https://github.com/FunAudioLLM/CV3-Eval)

**CosyVoice 2.0**: [デモ](https://funaudiollm.github.io/cosyvoice2/); [論文](https://arxiv.org/pdf/2412.10117); [Modelscope](https://www.modelscope.cn/models/iic/CosyVoice2-0.5B); [HuggingFace](https://huggingface.co/FunAudioLLM/CosyVoice2-0.5B)

**CosyVoice 1.0**: [デモ](https://fun-audio-llm.github.io); [論文](https://funaudiollm.github.io/pdf/CosyVoice_v1.pdf); [Modelscope](https://www.modelscope.cn/models/iic/CosyVoice-300M); [HuggingFace](https://huggingface.co/FunAudioLLM/CosyVoice-300M)

## ハイライト🔥

**Fun-CosyVoice 3.0** は大規模言語モデル（LLM）に基づく高度なテキスト読み上げ（TTS）システムで、コンテンツの一貫性、話者の類似性、プロソディの自然性において前任（CosyVoice 2.0）を上回る性能を発揮します。ワイルドなゼロショット多言語音声合成のために設計されています。

### 主な機能
- **言語対応**: 9つの主要言語（中国語、英語、日本語、韓国語、ドイツ語、スペイン語、フランス語、イタリア語、ロシア語）、18以上の中国語方言/アクセント（広東、閩南、四川、東北、陝西、山西、上海、天津、山東、寧夏、甘粛など）をカバーし、多言語/クロスリンガルゼロショット音声クローンを同時にサポート
- **コンテンツの一貫性と自然性**: コンテンツの一貫性、話者の類似性、プロソディの自然性において最先端の性能を達成
- **発音インペインティング**: 中国語ピンインと英語CMU音素の発音インペインティングをサポートし、より高い制御性を提供するため実運用に適している
- **テキスト正規化**: 数字、特殊記号、様々なテキスト形式の読み上げを従来のフロントエンドモジュールなしでサポート
- **バイストリーミング**: テキストインストリーミングと音声アウトストリーミングの両方をサポートし、高品質な音声出力を維持しながら150msという低レイテンシを実現
- **命令サポート**: 言語、方言、感情、速度、音量などの様々な命令をサポート
- **AMD GPU サポート**: AMD GPU向けのROCmサポートを追加！詳細は[ROCmセットアップ](#rocm-amd-gpu-サポート)セクションを参照


## ロードマップ

- [x] 2025/12

    - [x] Fun-CosyVoice3-0.5B-2512 基本モデル、RLモデルとその学習/推論スクリプトをリリース
    - [x] Fun-CosyVoice3-0.5B modelscope gradio spaceをリリース

- [x] 2025/08

    - [x] NVIDIA Yuekai Zhangの貢献により、triton trtllmランタイムサポートとcosyvoice2 grpo学習サポートを追加

- [x] 2025/07

    - [x] Fun-CosyVoice 3.0 評価セットをリリース

- [x] 2025/05

    - [x] CosyVoice2-0.5B vllmサポートを追加

- [x] 2024/12

    - [x] 25hz CosyVoice2-0.5Bをリリース

- [x] 2024/09

    - [x] 25hz CosyVoice-300M基本モデル
    - [x] 25hz CosyVoice-300M音声変換機能

- [x] 2024/08

    - [x] Repetition Aware Sampling(RAS)推論でllmの安定性向上
    - [x] ストリーミング推論モードサポート、rtf最適化のためのkv cacheとsdpaを含む

- [x] 2024/07

    - [x] Flow matching学習サポート
    - [x] ttsfrdが利用できない場合のWeTextProcessingサポート
    - [x] Fastapiサーバーとクライアント

## 評価

| モデル | オープンソース | モデルサイズ | test-zh<br>CER (%) ↓ | test-zh<br>SS (%) ↑ | test-en<br>WER (%) ↓ | test-en<br>SS (%) ↑ | test-hard<br>CER (%) ↓ | test-hard<br>SS (%) ↑ |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Human | - | - | 1.26 | 75.5 | 2.14 | 73.4 | - | - |
| Seed-TTS | ❌ | - | 1.12 | 79.6 | 2.25 | 76.2 | 7.59 | 77.6 |
| MiniMax-Speech | ❌ | - | 0.83 | 78.3 | 1.65 | 69.2 | - | - |
| F5-TTS | ✅ | 0.3B | 1.52 | 74.1 | 2.00 | 64.7 | 8.67 | 71.3 |
| Spark TTS | ✅ | 0.5B | 1.2 | 66.0 | 1.98 | 57.3 | - | - |
| CosyVoice2 | ✅ | 0.5B | 1.45 | 75.7 | 2.57 | 65.9 | 6.83 | 72.4 |
| FireRedTTS2 | ✅ | 1.5B | 1.14 | 73.2 | 1.95 | 66.5 | - | - |
| Index-TTS2 | ✅ | 1.5B | 1.03 | 76.5 | 2.23 | 70.6 | 7.12 | 75.5 |
| VibeVoice-1.5B | ✅ | 1.5B | 1.16 | 74.4 | 3.04 | 68.9 | - | - |
| VibeVoice-Realtime | ✅ | 0.5B | - | - | 2.05 | 63.3 | - | - |
| HiggsAudio-v2 | ✅ | 3B | 1.50 | 74.0 | 2.44 | 67.7 | - | - |
| VoxCPM | ✅ | 0.5B | 0.93 | 77.2 | 1.85 | 72.9 | 8.87 | 73.0 |
| GLM-TTS | ✅ | 1.5B | 1.03 | 76.1 | - | - | - | - |
| GLM-TTS RL | ✅ | 1.5B | 0.89 | 76.4 | - | - | - | - |
| Fun-CosyVoice3-0.5B-2512 | ✅ | 0.5B | 1.21 | 78.0 | 2.24 | 71.8 | 6.71 | 75.8 |
| Fun-CosyVoice3-0.5B-2512_RL | ✅ | 0.5B | 0.81 | 77.4 | 1.68 | 69.5 | 5.44 | 75.0 |


## インストール

### リポジトリのクローンとインストール

- リポジトリをクローン
    ``` sh
    git clone --recursive https://github.com/FunAudioLLM/CosyVoice.git
    # ネットワークエラーでサブモジュールのクローンに失敗した場合、成功するまで以下のコマンドを実行してください
    cd CosyVoice
    git submodule update --init --recursive
    ```

- Condaのインストール: https://docs.conda.io/en/latest/miniconda.html を参照してください
- Conda環境の作成:

    ``` sh
    conda create -n cosyvoice -y python=3.10
    conda activate cosyvoice
    pip install -r requirements.txt -i https://mirrors.aliyun.com/pypi/simple/ --trusted-host=mirrors.aliyun.com

    # sox互換性の問題に遭遇する場合
    # ubuntu
    sudo apt-get install sox libsox-dev
    # centos
    sudo yum install sox sox-devel
    ```

### モデルのダウンロード

事前学習済みの`Fun-CosyVoice3-0.5B`、`CosyVoice2-0.5B`、`CosyVoice-300M`、`CosyVoice-300M-SFT`、`CosyVoice-300M-Instruct`モデルと`CosyVoice-ttsfrd`リソースのダウンロードを強くお勧めします。

``` python
# modelscope SDKによるモデルダウンロード
from modelscope import snapshot_download
snapshot_download('FunAudioLLM/Fun-CosyVoice3-0.5B-2512', local_dir='pretrained_models/Fun-CosyVoice3-0.5B')
snapshot_download('iic/CosyVoice2-0.5B', local_dir='pretrained_models/CosyVoice2-0.5B')
snapshot_download('iic/CosyVoice-300M', local_dir='pretrained_models/CosyVoice-300M')
snapshot_download('iic/CosyVoice-300M-SFT', local_dir='pretrained_models/CosyVoice-300M-SFT')
snapshot_download('iic/CosyVoice-300M-Instruct', local_dir='pretrained_models/CosyVoice-300M-Instruct')
snapshot_download('iic/CosyVoice-ttsfrd', local_dir='pretrained_models/CosyVoice-ttsfrd')

# 海外ユーザー向け、huggingface SDKによるモデルダウンロード
from huggingface_hub import snapshot_download
snapshot_download('FunAudioLLM/Fun-CosyVoice3-0.5B-2512', local_dir='pretrained_models/Fun-CosyVoice3-0.5B')
snapshot_download('FunAudioLLM/CosyVoice2-0.5B', local_dir='pretrained_models/CosyVoice2-0.5B')
snapshot_download('FunAudioLLM/CosyVoice-300M', local_dir='pretrained_models/CosyVoice-300M')
snapshot_download('FunAudioLLM/CosyVoice-300M-SFT', local_dir='pretrained_models/CosyVoice-300M-SFT')
snapshot_download('FunAudioLLM/CosyVoice-300M-Instruct', local_dir='pretrained_models/CosyVoice-300M-Instruct')
snapshot_download('FunAudioLLM/CosyVoice-ttsfrd', local_dir='pretrained_models/CosyVoice-ttsfrd')
```

オプションで、`ttsfrd`リソースを解凍し、`ttsfrd`パッケージをインストールすると、より良いテキスト正規化性能が得られます。

ただし、このステップは必須ではありません。`ttsfrd`パッケージをインストールしない場合、デフォルトでwetextを使用します。

``` sh
cd pretrained_models/CosyVoice-ttsfrd/
unzip resource.zip -d .
pip install ttsfrd_dependency-0.1-py3-none-any.whl
pip install ttsfrd-0.4.2-cp310-cp310-linux_x86_64.whl
```

### 基本的な使い方

より良いパフォーマンスのため、`Fun-CosyVoice3-0.5B`の使用を強くお勧めします。
各モデルの詳細な使用方法については`example.py`のコードに従ってください。
```sh
python example.py
```

#### vLLM使用方法
CosyVoice2/3は現在**vLLM 0.11.x+ (V1エンジン)**と**vLLM 0.9.0 (レガシー)**をサポートしています。
古いvllmバージョン(<0.9.0)はCosyVoice推論をサポートしておらず、その間のバージョン（例：0.10.x）はテストされていません。

`vllm`には多くの特定の要件があることに注意してください。ハードウェアがvllmをサポートしていない場合や古い環境が破損した場合に備えて、新しい環境を作成できます。

``` sh
conda create -n cosyvoice_vllm --clone cosyvoice
conda activate cosyvoice_vllm
# for vllm==0.9.0
pip install vllm==v0.9.0 transformers==4.51.3 numpy==1.26.4 -i https://mirrors.aliyun.com/pypi/simple/ --trusted-host=mirrors.aliyun.com
# for vllm>=0.11.0
pip install vllm==v0.11.0 transformers==4.57.1 numpy==1.26.4 -i https://mirrors.aliyun.com/pypi/simple/ --trusted-host=mirrors.aliyun.com
python vllm_example.py
```

#### Webデモの開始

Webデモページを使ってCosyVoiceを素早く理解できます。

詳細はデモWebサイトを参照してください。

``` python
# sft推論の場合はiic/CosyVoice-300M-SFTに変更、instruct推論の場合はiic/CosyVoice-300M-Instructに変更
python3 webui.py --port 50000 --model_dir pretrained_models/CosyVoice-300M
```

#### 高度な使用方法

上級者ユーザーのために、`examples/libritts`で学習および推論スクリプトを提供しています。

### ROCm (AMD GPU) サポート

このリポジトリにはAMD GPU向けの実験的なROCmサポートが含まれています。ROCm実装は以下でテストされています：
- **GPU**: AMD Radeon Graphics (RDNA 3/Strix Halo)
- **ROCmバージョン**: 7.1.1
- **PyTorch**: 2.9.1+rocm7.1.1
- **torchaudio**: 2.9.0+rocm7.1.1

#### Dockerセットアップ（推奨）

AMD GPUでCosyVoiceを実行する最も簡単な方法はDockerを使用することです：

```bash
cd docker
docker compose -f docker-compose.rocm.yml up --build
```

Webインターフェースは`http://localhost:7860`で利用可能になります

#### 手動セットアップ

1. Conda環境の作成と依存関係のインストール：
```bash
conda create -n cosyvoice -y python=3.10
conda activate cosyvoice
pip install -r requirements-rocm.txt
```

2. ROCm最適化版PyTorchとtorchaudioのインストール：
```bash
pip uninstall -y torch torchvision torchaudio
pip install 'torch==2.9.1+rocm7.1.1.lw.git351ff442' \
            'torchaudio==2.9.0+rocm7.1.1.gite3c6ee2b' \
            --find-links https://repo.radeon.com/rocm/manylinux/rocm-rel-7.1.1/
```

3. テキスト処理用pyniniのインストール：
```bash
conda install -y -c conda-forge pynini==2.1.5
```

4. 通常通り推論を実行（GPUは自動的に検出されます）

**注**: ROCmサポートは実験的です。パフォーマンスはGPUモデルとROCmバージョンによって異なる場合があります。

#### デプロイ用ビルド

オプションで、サービスデプロイを行いたい場合、以下のステップを実行できます。

``` sh
cd runtime/python
docker build -t cosyvoice:v1.0 .
# instruct推論を使用する場合はiic/CosyVoice-300Mをiic/CosyVoice-300M-Instructに変更
# grpc使用の場合
docker run -d --runtime=nvidia -p 50000:50000 cosyvoice:v1.0 /bin/bash -c "cd /opt/CosyVoice/CosyVoice/runtime/python/grpc && python3 server.py --port 50000 --max_conc 4 --model_dir iic/CosyVoice-300M && sleep infinity"
cd grpc && python3 client.py --port 50000 --mode <sft|zero_shot|cross_lingual|instruct>
# fastapi使用の場合
docker run -d --runtime=nvidia -p 50000:50000 cosyvoice:v1.0 /bin/bash -c "cd /opt/CosyVoice/CosyVoice/runtime/python/fastapi && python3 server.py --port 50000 --model_dir iic/CosyVoice-300M && sleep infinity"
cd fastapi && python3 client.py --port 50000 --mode <sft|zero_shot|cross_lingual|instruct>
```

#### デプロイ向けNvidia TensorRT-LLMの使用

TensorRT-LLMを使用してcosyvoice2 llmを高速化すると、huggingface transformers実装と比較して4倍の高速化が可能です。
クイックスタート：

``` sh
cd runtime/triton_trtllm
docker compose up -d
```
詳細は[こちら](https://github.com/FunAudioLLM/CosyVoice/tree/main/runtime/triton_trtllm)を確認してください

## ディスカッションとコミュニケーション

[Github Issues](https://github.com/FunAudioLLM/CosyVoice/issues)で直接ディスカッションできます。

また、QRコードをスキャンして公式Dingdingチャットグループに参加することもできます。

<img src="./asset/dingding.png" width="250px">

## 謝辞

1. [FunASR](https://github.com/modelscope/FunASR)から多くのコードを借用しました
2. [FunCodec](https://github.com/modelscope/FunCodec)から多くのコードを借用しました
3. [Matcha-TTS](https://github.com/shivammehta25/Matcha-TTS)から多くのコードを借用しました
4. [AcademiCodec](https://github.com/yangdongchao/AcademiCodec)から多くのコードを借用しました
5. [WeNet](https://github.com/wenet-e2e/wenet)から多くのコードを借用しました

## 引用

``` bibtex
@article{du2024cosyvoice,
  title={Cosyvoice: A scalable multilingual zero-shot text-to-speech synthesizer based on supervised semantic tokens},
  author={Du, Zhihao and Chen, Qian and Zhang, Shiliang and Hu, Kai and Lu, Heng and Yang, Yexin and Hu, Hangrui and Zheng, Siqi and Gu, Yue and Ma, Ziyang and others},
  journal={arXiv preprint arXiv:2407.05407},
  year={2024}
}

@article{du2024cosyvoice,
  title={Cosyvoice 2: Scalable streaming speech synthesis with large language models},
  author={Du, Zhihao and Wang, Yuxuan and Chen, Qian and Shi, Xian and Lv, Xiang and Zhao, Tianyu and Gao, Zhifu and Yang, Yexin and Gao, Changfeng and Wang, Hui and others},
  journal={arXiv preprint arXiv:2412.10117},
  year={2024}
}

@article{du2025cosyvoice,
  title={CosyVoice 3: Towards In-the-wild Speech Generation via Scaling-up and Post-training},
  author={Du, Zhihao and Gao, Changfeng and Wang, Yuxuan and Yu, Fan and Zhao, Tianyu and Wang, Hao and Lv, Xiang and Wang, Hui and Shi, Xian and An, Keyu and others},
  journal={arXiv preprint arXiv:2505.17589},
  year={2025}
}

@inproceedings{lyu2025build,
  title={Build LLM-Based Zero-Shot Streaming TTS System with Cosyvoice},
  author={Lyu, Xiang and Wang, Yuxuan and Zhao, Tianyu and Wang, Hao and Liu, Huadai and Du, Zhihao},
  booktitle={ICASSP 2025-2025 IEEE International Conference on Acoustics, Speech and Signal Processing (ICASSP)},
  pages={1--2},
  year={2025},
  organization={IEEE}
}
```

## 免責事項
上記で提供される内容は学術目的のみであり、技術的機能を示すことを意図しています。一部の例はインターネットからソースされています。コンテンツがあなたの権利を侵害している場合は、削除をリクエストするためにご連絡ください。
