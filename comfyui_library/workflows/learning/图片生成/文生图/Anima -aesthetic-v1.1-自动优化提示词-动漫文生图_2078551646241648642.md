---
key: 图片生成/文生图/Anima -aesthetic-v1.1-自动优化提示词-动漫文生图_2078551646241648642.json
name: Anima -aesthetic-v1.1-自动优化提示词-动漫文生图_2078551646241648642
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/Anima -aesthetic-v1.1-自动优化提示词-动漫文生图_2078551646241648642.json
hash: d4f7fa2d4e55e7bd
coverage: 0.916667
learned_at: 2026-10-20 00:18:42
nodes: [CLIPTextEncode, RHLLMChatNode, CR Prompt Text, UNETLoader, CLIPLoader, VAELoader, SaveImage, ShowText|pysssss, CLIPTextEncode, KSampler, VAEDecode, EmptyLatentImage]
patterns: [text_to_image]
missing: []
parameters: {"batch_size": 1, "cfg": 4.5, "denoise": 1, "height": 1920, "sampler_name": "er_sde", "scheduler": "beta", "seed": 649321620182424, "steps": 40, "width": 1080}
---

# 图片生成/文生图/Anima -aesthetic-v1.1-自动优化提示词-动漫文生图_2078551646241648642.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/Anima -aesthetic-v1.1-自动优化提示词-动漫文生图_2078551646241648642.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Output → Other

**节点**（12 个）：
- `CLIPTextEncode` ★核心
- `RHLLMChatNode`
- `CR Prompt Text`
- `UNETLoader` ★核心
- `CLIPLoader`
- `VAELoader`
- `SaveImage`
- `ShowText|pysssss`
- `CLIPTextEncode` ★核心
- `KSampler` ★核心
- `VAEDecode` ★核心
- `EmptyLatentImage` ★核心

**识别到的模式**：text_to_image

## 关键参数

- `seed` = `649321620182424`
- `steps` = `40`
- `cfg` = `4.5`
- `sampler_name` = `er_sde`
- `scheduler` = `beta`
- `denoise` = `1`
- `width` = `1080`
- `height` = `1920`
- `batch_size` = `1`

## 知识

覆盖率 **92%**（11/12）

**有卡**：`CLIPTextEncode`、`RHLLMChatNode`、`CR Prompt Text`、`UNETLoader`、`CLIPLoader`、`VAELoader`、`SaveImage`、`KSampler`、`VAEDecode`、`EmptyLatentImage`

**用到的条目**：KSampler、VAEDecode、VAELoader、CLIPTextEncode、CLIPLoader、EmptyLatentImage、UNETLoader、CR Prompt Text
