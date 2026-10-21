---
key: 图片生成/文生图/千问 qwen image 2.1 多图编辑 图片编辑 +全节点注释_2101953245253033985.json
name: 千问 qwen image 2.1 多图编辑 图片编辑 +全节点注释_2101953245253033985
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/千问 qwen image 2.1 多图编辑 图片编辑 +全节点注释_2101953245253033985.json
hash: 6e66680222aed93a
coverage: 0.475
learned_at: 2026-10-20 01:52:19
nodes: [VAEDecode, UNETLoader, QwenImage21Cache, VAELoader, Anything Everywhere3, BatchImagesNode, TextEncodeQwenImage21, ResolutionSelector, EmptyLatentImage, ComfySwitchNode, LoadImage, KSampler, CLIPLoader, CLIPLoader, CR Text, Note, Note, Note, Note, Note, Note, Note, Note, Note, Note, Note, Note, Note, Note, Note, Note, Note, Note, Note, LoadImage, LoadImage, SaveImage, CR Prompt Text, LoadImage, TextGenerateLTX2Prompt]
patterns: []
missing: []
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 1024, "sampler_name": "euler", "scheduler": "simple", "seed": 676628828280961, "steps": 40, "width": 1024}
---

# 图片生成/文生图/千问 qwen image 2.1 多图编辑 图片编辑 +全节点注释_2101953245253033985.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/千问 qwen image 2.1 多图编辑 图片编辑 +全节点注释_2101953245253033985.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（40 个）：
- `VAEDecode` ★核心
- `UNETLoader` ★核心
- `QwenImage21Cache`
- `VAELoader`
- `Anything Everywhere3`
- `BatchImagesNode`
- `TextEncodeQwenImage21`
- `ResolutionSelector`
- `EmptyLatentImage` ★核心
- `ComfySwitchNode`
- `LoadImage`
- `KSampler` ★核心
- `CLIPLoader`
- `CLIPLoader`
- `CR Text`
- `Note`
- `Note`
- `Note`
- `Note`
- `Note`
- `Note`
- `Note`
- `Note`
- `Note`
- `Note`
- `Note`
- `Note`
- `Note`
- `Note`
- `Note`
- `Note`
- `Note`
- `Note`
- `Note`
- `LoadImage`
- `LoadImage`
- `SaveImage`
- `CR Prompt Text`
- `LoadImage`
- `TextGenerateLTX2Prompt`

## 关键参数

- `width` = `1024`
- `height` = `1024`
- `batch_size` = `1`
- `seed` = `676628828280961`
- `steps` = `40`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **48%**（19/40）

**有卡**：`VAEDecode`、`UNETLoader`、`QwenImage21Cache`、`VAELoader`、`BatchImagesNode`、`TextEncodeQwenImage21`、`ResolutionSelector`、`EmptyLatentImage`、`LoadImage`、`KSampler`、`CLIPLoader`、`CR Text`、`SaveImage`、`CR Prompt Text`、`TextGenerateLTX2Prompt`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、CLIPLoader、EmptyLatentImage、ResolutionSelector、LoadImage
