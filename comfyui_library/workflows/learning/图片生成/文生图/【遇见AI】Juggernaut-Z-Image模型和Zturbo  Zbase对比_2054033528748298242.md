---
key: 图片生成/文生图/【遇见AI】Juggernaut-Z-Image模型和Zturbo  Zbase对比_2054033528748298242.json
name: 【遇见AI】Juggernaut-Z-Image模型和Zturbo  Zbase对比_2054033528748298242
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/【遇见AI】Juggernaut-Z-Image模型和Zturbo  Zbase对比_2054033528748298242.json
hash: 1d008e28918cef6a
coverage: 0.966667
learned_at: 2026-10-21 02:58:06
nodes: [VAEDecode, CLIPTextEncode, KSampler, VAEDecode, KSampler, VAEDecode, CLIPTextEncode, KSampler, EmptyLatentImage, CR Seed, CLIPTextEncode, CLIPTextEncode, CLIPTextEncode, CLIPTextEncode, easy promptLine, SaveImage, SaveImage, LoadImage, MarkdownNote, LoadImage, UNETLoader, UNETLoader, UNETLoader, CLIPLoader, VAELoader, VAELoader, CLIPLoader, CLIPLoader, VAELoader, SaveImage]
patterns: [text_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 1280, "sampler_name": "euler", "scheduler": "simple", "seed": 710423545231473, "steps": 8, "width": 720}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/文生图/【遇见AI】Juggernaut-Z-Image模型和Zturbo  Zbase对比_2054033528748298242.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/【遇见AI】Juggernaut-Z-Image模型和Zturbo  Zbase对比_2054033528748298242.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Output → Other

**节点**（30 个）：
- `VAEDecode` ★核心
- `CLIPTextEncode` ★核心
- `KSampler` ★核心
- `VAEDecode` ★核心
- `KSampler` ★核心
- `VAEDecode` ★核心
- `CLIPTextEncode` ★核心
- `KSampler` ★核心
- `EmptyLatentImage` ★核心
- `CR Seed`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `easy promptLine`
- `SaveImage`
- `SaveImage`
- `LoadImage`
- `MarkdownNote`
- `LoadImage`
- `UNETLoader` ★核心
- `UNETLoader` ★核心
- `UNETLoader` ★核心
- `CLIPLoader`
- `VAELoader`
- `VAELoader`
- `CLIPLoader`
- `CLIPLoader`
- `VAELoader`
- `SaveImage`

**识别到的模式**：text_to_image

## 关键参数

- `seed` = `710423545231473`
- `steps` = `8`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`
- `width` = `720`
- `height` = `1280`
- `batch_size` = `1`

## 知识

覆盖率 **97%**（29/30）

**有卡**：`VAEDecode`、`CLIPTextEncode`、`KSampler`、`EmptyLatentImage`、`CR Seed`、`easy promptLine`、`SaveImage`、`LoadImage`、`UNETLoader`、`CLIPLoader`、`VAELoader`

**用到的条目**：KSampler、VAEDecode、VAELoader、CLIPTextEncode、CLIPLoader、EmptyLatentImage、LoadImage、UNETLoader

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
