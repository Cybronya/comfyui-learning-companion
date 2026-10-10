---
key: Qwen-Image-2.1_文生图+4步加速_2103505307195502594.json
name: Qwen-Image-2.1_文生图+4步加速_2103505307195502594
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/Qwen-Image-2.1_文生图+4步加速_2103505307195502594.json
hash: 46b56dddadc1ce1f
coverage: 0.923077
learned_at: 2026-10-10 20:59:00
nodes: [VAELoader, ConditioningZeroOut, ModelAttentionBackend, CLIPLoader, KSampler, CLIPTextEncode, PreviewImage, LoraLoaderModelOnly, UNETLoader, EmptyLatentImage, SaveImageAdvanced, VAEDecode, SaveImage]
patterns: [text_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 1080, "sampler_name": "euler", "scheduler": "simple", "seed": 66, "steps": 6, "width": 1920}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# Qwen-Image-2.1_文生图+4步加速_2103505307195502594.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/Qwen-Image-2.1_文生图+4步加速_2103505307195502594.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Output → Other

**节点**（13 个）：
- `VAELoader`
- `ConditioningZeroOut`
- `ModelAttentionBackend`
- `CLIPLoader`
- `KSampler` ★核心
- `CLIPTextEncode` ★核心
- `PreviewImage`
- `LoraLoaderModelOnly` ★核心
- `UNETLoader` ★核心
- `EmptyLatentImage` ★核心
- `SaveImageAdvanced`
- `VAEDecode` ★核心
- `SaveImage`

**识别到的模式**：text_to_image

## 关键参数

- `seed` = `66`
- `steps` = `6`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`
- `width` = `1920`
- `height` = `1080`
- `batch_size` = `1`

## 知识

覆盖率 **92%**（12/13）

**有卡**：`VAELoader`、`ConditioningZeroOut`、`ModelAttentionBackend`、`CLIPLoader`、`KSampler`、`CLIPTextEncode`、`LoraLoaderModelOnly`、`UNETLoader`、`EmptyLatentImage`、`SaveImageAdvanced`、`VAEDecode`、`SaveImage`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、ConditioningZeroOut、EmptyLatentImage

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
