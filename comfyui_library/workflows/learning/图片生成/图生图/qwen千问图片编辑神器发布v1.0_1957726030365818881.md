---
key: 图片生成/图生图/qwen千问图片编辑神器发布v1.0_1957726030365818881.json
name: qwen千问图片编辑神器发布v1.0_1957726030365818881
type: Image To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/qwen千问图片编辑神器发布v1.0_1957726030365818881.json
hash: f8c1ef34e2ecb7fe
coverage: 1
learned_at: 2026-10-23 11:44:25
nodes: [KSampler, VAELoader, CLIPLoader, FluxKontextImageScale, VAEEncode, CLIPTextEncode, VAEDecode, LoadImage, TextEncodeQwenImageEdit, UNETLoader, easy imageConcat, SaveImage, LayerUtility: ImageScaleByAspectRatio V2]
patterns: [image_to_image]
missing: []
parameters: {"cfg": 2.5, "denoise": 1, "sampler_name": "euler", "scheduler": "normal", "seed": 1, "steps": 20}
---

# 图片生成/图生图/qwen千问图片编辑神器发布v1.0_1957726030365818881.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/qwen千问图片编辑神器发布v1.0_1957726030365818881.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（13 个）：
- `KSampler` ★核心
- `VAELoader`
- `CLIPLoader`
- `FluxKontextImageScale`
- `VAEEncode` ★核心
- `CLIPTextEncode` ★核心
- `VAEDecode` ★核心
- `LoadImage`
- `TextEncodeQwenImageEdit`
- `UNETLoader` ★核心
- `easy imageConcat`
- `SaveImage`
- `LayerUtility: ImageScaleByAspectRatio V2`

**识别到的模式**：image_to_image

## 关键参数

- `seed` = `1`
- `steps` = `20`
- `cfg` = `2.5`
- `sampler_name` = `euler`
- `scheduler` = `normal`
- `denoise` = `1`

## 知识

覆盖率 **100%**（13/13）

**有卡**：`KSampler`、`VAELoader`、`CLIPLoader`、`FluxKontextImageScale`、`VAEEncode`、`CLIPTextEncode`、`VAEDecode`、`LoadImage`、`TextEncodeQwenImageEdit`、`UNETLoader`、`easy imageConcat`、`SaveImage`、`LayerUtility: ImageScaleByAspectRatio V2`

**用到的条目**：KSampler、VAEDecode、VAELoader、UNETLoader、CLIPTextEncode、CLIPLoader、LoadImage、TextEncodeQwenImageEdit
