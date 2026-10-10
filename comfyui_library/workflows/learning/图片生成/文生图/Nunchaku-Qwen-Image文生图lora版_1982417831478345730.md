---
key: Nunchaku-Qwen-Image文生图lora版_1982417831478345730.json
name: Nunchaku-Qwen-Image文生图lora版_1982417831478345730
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/Nunchaku-Qwen-Image文生图lora版_1982417831478345730.json
hash: e9a2f10d0a682df5
coverage: 0.916667
learned_at: 2026-10-10 20:58:48
nodes: [ConditioningZeroOut, VAEDecode, SaveImage, NunchakuQwenImageLoraLoader, CLIPLoader, VAELoader, NunchakuQwenImageLoraStack, NunchakuQwenImageDiTLoader, PreviewImage, CLIPTextEncode, KSampler, EmptyLatentImage]
patterns: [text_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 512, "sampler_name": "euler", "scheduler": "kl_optimal", "seed": 127087507019677, "steps": 8, "width": 512}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# Nunchaku-Qwen-Image文生图lora版_1982417831478345730.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/Nunchaku-Qwen-Image文生图lora版_1982417831478345730.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output

**节点**（12 个）：
- `ConditioningZeroOut`
- `VAEDecode` ★核心
- `SaveImage`
- `NunchakuQwenImageLoraLoader` ★核心
- `CLIPLoader`
- `VAELoader`
- `NunchakuQwenImageLoraStack`
- `NunchakuQwenImageDiTLoader`
- `PreviewImage`
- `CLIPTextEncode` ★核心
- `KSampler` ★核心
- `EmptyLatentImage` ★核心

**识别到的模式**：text_to_image

## 关键参数

- `seed` = `127087507019677`
- `steps` = `8`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `kl_optimal`
- `denoise` = `1`
- `width` = `512`
- `height` = `512`
- `batch_size` = `1`

## 知识

覆盖率 **92%**（11/12）

**有卡**：`ConditioningZeroOut`、`VAEDecode`、`SaveImage`、`NunchakuQwenImageLoraLoader`、`CLIPLoader`、`VAELoader`、`NunchakuQwenImageLoraStack`、`NunchakuQwenImageDiTLoader`、`CLIPTextEncode`、`KSampler`、`EmptyLatentImage`

**用到的条目**：KSampler、VAEDecode、VAELoader、CLIPTextEncode、CLIPLoader、ConditioningZeroOut、EmptyLatentImage、NunchakuQwenImageLoraStack

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
