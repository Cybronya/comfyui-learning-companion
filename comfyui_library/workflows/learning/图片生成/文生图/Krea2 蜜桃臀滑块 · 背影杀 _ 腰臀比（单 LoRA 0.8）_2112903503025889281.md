---
key: 图片生成/文生图/Krea2 蜜桃臀滑块 · 背影杀 _ 腰臀比（单 LoRA 0.8）_2112903503025889281.json
name: Krea2 蜜桃臀滑块 · 背影杀 _ 腰臀比（单 LoRA 0.8）_2112903503025889281
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/Krea2 蜜桃臀滑块 · 背影杀 _ 腰臀比（单 LoRA 0.8）_2112903503025889281.json
hash: eef5722bc7cbd3ef
coverage: 1
learned_at: 2026-10-26 22:07:32
nodes: [KSampler, VAEDecode, VAELoader, CLIPLoader, ResolutionSelector, ModelSamplingAuraFlow, UNETLoader, CLIPTextEncode, CompressImages, CLIPTextEncode, SaveImage, EmptyLatentImage, LoraLoaderModelOnly]
patterns: [text_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 1024, "sampler_name": "er_sde", "scheduler": "simple", "seed": 817420159879581, "steps": 8, "width": 1024}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/文生图/Krea2 蜜桃臀滑块 · 背影杀 _ 腰臀比（单 LoRA 0.8）_2112903503025889281.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/Krea2 蜜桃臀滑块 · 背影杀 _ 腰臀比（单 LoRA 0.8）_2112903503025889281.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（13 个）：
- `KSampler` ★核心
- `VAEDecode` ★核心
- `VAELoader`
- `CLIPLoader`
- `ResolutionSelector`
- `ModelSamplingAuraFlow`
- `UNETLoader` ★核心
- `CLIPTextEncode` ★核心
- `CompressImages`
- `CLIPTextEncode` ★核心
- `SaveImage`
- `EmptyLatentImage` ★核心
- `LoraLoaderModelOnly` ★核心

**识别到的模式**：text_to_image

## 关键参数

- `seed` = `817420159879581`
- `steps` = `8`
- `cfg` = `1`
- `sampler_name` = `er_sde`
- `scheduler` = `simple`
- `denoise` = `1`
- `width` = `1024`
- `height` = `1024`
- `batch_size` = `1`

## 知识

覆盖率 **100%**（13/13）

**有卡**：`KSampler`、`VAEDecode`、`VAELoader`、`CLIPLoader`、`ResolutionSelector`、`ModelSamplingAuraFlow`、`UNETLoader`、`CLIPTextEncode`、`CompressImages`、`SaveImage`、`EmptyLatentImage`、`LoraLoaderModelOnly`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、EmptyLatentImage、ResolutionSelector

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
