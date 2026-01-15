# CosyVoice3 ROCm環境構築ガイド

このガイドは、T5Gemma-TTSプロジェクトのROCm構成をベースにしたCosyVoice3のROCm環境構築方法を説明します。

## 前提条件

- AMD GPU（ROCm対応）
- Docker と Docker Compose
- Linux環境（Ubuntu 22.04推奨）

## ROCm対応ファイル

以下のファイルを作成しました：

1. **docker/Dockerfile.rocm**: ROCm対応Dockerfile
2. **docker/docker-compose.rocm.yml**: ROCm対応docker-compose設定
3. **requirements-rocm.txt**: CUDA依存を削除したrequirementsファイル

## 主な変更点

### CUDA依存パッケージの置き換え

| パッケージ | CUDA版 | ROCm版 |
|----------|--------|--------|
| PyTorch | torch==2.3.1 (cu121) | ROCm版（repo.radeon.com） |
| TorchAudio | torchaudio==2.3.1 (cu121) | ROCm版（repo.radeon.com） |
| ONNX Runtime | onnxruntime-gpu (CUDA) | onnxruntime (CPU only) |
| TensorRT | tensorrt-cu12 | 削除（NVIDIA専用） |

### 追加変更

- ベースイメージ: `nvidia/cuda` → `rocm/pytorch`
- デバイスアクセス: `/dev/kfd`, `/dev/dri` を追加
- セキュリティ: `seccomp:unconfined` を追加
- 共有メモリ: `64gb`（統一メモリ用）

## 使用方法

### 1. Dockerイメージのビルド

```bash
cd ~/document/CosyVoice/docker
docker compose -f docker-compose.rocm.yml build
```

### 2. コンテナの起動

```bash
docker compose -f docker-compose.rocm.yml up
```

### 3. コンテナ内でWebUIを起動

```bash
# 別のターミナルでコンテナに入る
docker exec -it cosyvoice-rocm bash

# Conda環境をアクティベート
conda activate cosyvoice

# WebUIを起動
cd /workspace/CosyVoice
python webui.py
```

### 4. ブラウザでアクセス

```
http://localhost:7860
```

## GPU設定

### GFXバージョンの設定（必要に応じて）

AMD GPUの種類に応じて、`docker-compose.rocm.yml`の`HSA_OVERRIDE_GFX_VERSION`を設定してください：

```yaml
environment:
  # 例: AMD Radeon 8060S (Strix HALO)
  HSA_OVERRIDE_GFX_VERSION: "gfx1151"
```

**主なGFXバージョン:**
- `gfx1100`: Navi 21 / RX 6800 series
- `gfx1101`: Navi 22 / RX 6900 series
- `gfx1102`: Navi 23 / RX 7600 series
- `gfx1150`: RDNA 3.5 / Strix HALO base
- `gfx1151`: RDNA 3.5 / Strix HALO

### GPUアクセスの確認

コンテナ内で以下のコマンドを実行して、GPUが認識されているか確認できます：

```bash
rocm-smi
python -c "import torch; print(torch.cuda.is_available())"
```

## 注意事項

### ONNX Runtime

ONNX Runtime GPU版はROCmに対応していないため、CPU版を使用します。一部の機能でパフォーマンスが低下する可能性があります。

### TensorRT

TensorRTはNVIDIA専用のため削除しました。CosyVoice3はTensorRTなしで動作します。

### パフォーマンス

ROCm環境では、CUDA環境と比較してパフォーマンスが若干低下する場合があります。最新のROCmバージョンを使用することで、最適なパフォーマンスを得られます。

## トラブルシューティング

### GPUが認識されない場合

1. デバイスアクセスを確認：
   ```bash
   ls -l /dev/kfd /dev/dri
   ```

2. コンテナのデバイス設定を確認：
   ```bash
   docker inspect cosyvoice-rocm | grep Devices
   ```

3. グループ membershipsを確認：
   ```bash
   groups
   # videoとrenderグループに含まれている必要があります
   ```

### メモリ不足の場合

共有メモリサイズを増やします：
```yaml
shm_size: '128gb'  # 64gbから増量
```

### PyTorchがGPUを認識しない場合

1. ROCmバージョンを確認：
   ```bash
   rocm-smi
   python -c "import torch; print(torch.version.cuda)"
   ```

2. GFXバージョンオーバーライドを試す：
   ```yaml
   HSA_OVERRIDE_GFX_VERSION: "gfx1151"
   ```

## 参考情報

- [T5Gemma-TTS ROCm構成](../T5Gemma-TTS/Dockerfile.rocm)
- [ROCm PyTorch](https://rocm.docs.amd.com/projects/install-on-linux/en/latest/how-to/3rd-party-pytorch.html)
- [AMD GPU GFXバージョン](https://github.com/torvalds/linux/blob/master/drivers/gpu/drm/amd/amdgpu_drv.c)

## サポート

問題が発生した場合は、以下のログを確認してください：

```bash
docker compose -f docker-compose.rocm.yml logs -f
```

---

**作成日**: 2026-01-15
**ベース**: T5Gemma-TTS ROCm configuration
**テスト環境**: AMD Radeon 8060S (Strix HALO), ROCm 7.1.1
