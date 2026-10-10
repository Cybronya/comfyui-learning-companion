---
key: 千问qwen-image-2.1文生图工作流（不可商用）_2101941085793771521.json
name: 千问qwen-image-2.1文生图工作流（不可商用）_2101941085793771521
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/千问qwen-image-2.1文生图工作流（不可商用）_2101941085793771521.json
hash: e7bc3a2e6a7ec3b8
coverage: 0.923077
learned_at: 2026-10-10 20:59:38
nodes: [ConditioningZeroOut, VAEDecode, SaveImage, UNETLoader, EmptyLatentImage, PreviewImage, CLIPLoader, KSampler, CLIPTextEncode, VAELoader, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly]
patterns: [text_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 1920, "sampler_name": "euler", "scheduler": "simple", "seed": 1050187723721623, "steps": 8, "width": 1440}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 千问qwen-image-2.1文生图工作流（不可商用）_2101941085793771521.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/千问qwen-image-2.1文生图工作流（不可商用）_2101941085793771521.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Output

**节点**（13 个）：
- `ConditioningZeroOut`
- `VAEDecode` ★核心
- `SaveImage`
- `UNETLoader` ★核心
- `EmptyLatentImage` ★核心
- `PreviewImage`
- `CLIPLoader`
- `KSampler` ★核心
- `CLIPTextEncode` ★核心
- `VAELoader`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心

**识别到的模式**：text_to_image

## 关键参数

- `width` = `1440`
- `height` = `1920`
- `batch_size` = `1`
- `seed` = `1050187723721623`
- `steps` = `8`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **92%**（12/13）

**有卡**：`ConditioningZeroOut`、`VAEDecode`、`SaveImage`、`UNETLoader`、`EmptyLatentImage`、`CLIPLoader`、`KSampler`、`CLIPTextEncode`、`VAELoader`、`LoraLoaderModelOnly`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、ConditioningZeroOut、EmptyLatentImage

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
