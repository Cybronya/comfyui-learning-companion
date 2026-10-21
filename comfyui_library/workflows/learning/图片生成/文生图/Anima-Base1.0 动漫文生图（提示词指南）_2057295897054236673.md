---
key: 图片生成/文生图/Anima-Base1.0 动漫文生图（提示词指南）_2057295897054236673.json
name: Anima-Base1.0 动漫文生图（提示词指南）_2057295897054236673
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/Anima-Base1.0 动漫文生图（提示词指南）_2057295897054236673.json
hash: f9ff0b6d89f57fac
coverage: 0.923077
learned_at: 2026-10-19 22:45:22
nodes: [VAELoader, CLIPLoader, UNETLoader, CLIPTextEncode, CLIPTextEncode, VAEDecode, KSampler, EmptyLatentImage, CR Text, MarkdownNote, SaveImage, Int, Int]
patterns: [text_to_image]
missing: []
parameters: {"batch_size": 1, "cfg": 4, "denoise": 1, "height": 1024, "sampler_name": "er_sde", "scheduler": "simple", "seed": 297097606940485, "steps": 30, "width": 1024}
---

# 图片生成/文生图/Anima-Base1.0 动漫文生图（提示词指南）_2057295897054236673.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/Anima-Base1.0 动漫文生图（提示词指南）_2057295897054236673.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Output → Other

**节点**（13 个）：
- `VAELoader`
- `CLIPLoader`
- `UNETLoader` ★核心
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `VAEDecode` ★核心
- `KSampler` ★核心
- `EmptyLatentImage` ★核心
- `CR Text`
- `MarkdownNote`
- `SaveImage`
- `Int`
- `Int`

**识别到的模式**：text_to_image

## 关键参数

- `seed` = `297097606940485`
- `steps` = `30`
- `cfg` = `4`
- `sampler_name` = `er_sde`
- `scheduler` = `simple`
- `denoise` = `1`
- `width` = `1024`
- `height` = `1024`
- `batch_size` = `1`

## 知识

覆盖率 **92%**（12/13）

**有卡**：`VAELoader`、`CLIPLoader`、`UNETLoader`、`CLIPTextEncode`、`VAEDecode`、`KSampler`、`EmptyLatentImage`、`CR Text`、`SaveImage`、`Int`

**用到的条目**：KSampler、VAEDecode、VAELoader、CLIPTextEncode、CLIPLoader、EmptyLatentImage、UNETLoader、SaveImage
