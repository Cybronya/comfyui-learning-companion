---
key: 图片生成/文生图/Z-image-turbo ControNet文生图姿势控制_2045229213636108290.json
name: Z-image-turbo ControNet文生图姿势控制_2045229213636108290
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/Z-image-turbo ControNet文生图姿势控制_2045229213636108290.json
hash: 08a506303517a44f
coverage: 0.866667
learned_at: 2026-10-21 02:56:15
nodes: [ModelPatchLoader, CLIPTextEncode, VAELoader, CLIPLoader, QwenImageDiffsynthControlnet, LoadImage, UNETLoader, CLIPTextEncode, PreviewImage, ImageScale, PreviewImage, KSampler, EmptyLatentImage, VAEDecode, SaveImage]
patterns: [text_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 1536, "sampler_name": "euler", "scheduler": "simple", "seed": 236155400606637, "steps": 8, "width": 1536}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/文生图/Z-image-turbo ControNet文生图姿势控制_2045229213636108290.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/Z-image-turbo ControNet文生图姿势控制_2045229213636108290.json`

## 结构

**生成流程**：Model → Condition → Latent → Control → Sampling → Decode → Process → Output → Other

**节点**（15 个）：
- `ModelPatchLoader`
- `CLIPTextEncode` ★核心
- `VAELoader`
- `CLIPLoader`
- `QwenImageDiffsynthControlnet`
- `LoadImage`
- `UNETLoader` ★核心
- `CLIPTextEncode` ★核心
- `PreviewImage`
- `ImageScale`
- `PreviewImage`
- `KSampler` ★核心
- `EmptyLatentImage` ★核心
- `VAEDecode` ★核心
- `SaveImage`

**识别到的模式**：text_to_image

## 关键参数

- `seed` = `236155400606637`
- `steps` = `8`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`
- `width` = `1536`
- `height` = `1536`
- `batch_size` = `1`

## 知识

覆盖率 **87%**（13/15）

**有卡**：`ModelPatchLoader`、`CLIPTextEncode`、`VAELoader`、`CLIPLoader`、`QwenImageDiffsynthControlnet`、`LoadImage`、`UNETLoader`、`ImageScale`、`KSampler`、`EmptyLatentImage`、`VAEDecode`、`SaveImage`

**用到的条目**：KSampler、VAEDecode、VAELoader、CLIPTextEncode、CLIPLoader、EmptyLatentImage、LoadImage、UNETLoader

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
