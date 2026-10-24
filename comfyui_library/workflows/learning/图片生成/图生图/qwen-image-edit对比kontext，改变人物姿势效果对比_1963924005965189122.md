---
key: 图片生成/图生图/qwen-image-edit对比kontext，改变人物姿势效果对比_1963924005965189122.json
name: qwen-image-edit对比kontext，改变人物姿势效果对比_1963924005965189122
type: Image To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/qwen-image-edit对比kontext，改变人物姿势效果对比_1963924005965189122.json
hash: 33549f4304b05aed
coverage: 0.961538
learned_at: 2026-10-23 11:42:52
nodes: [ConditioningZeroOut, VAEEncode, ReferenceLatent, FluxGuidance, VAELoader, UNETLoader, DualCLIPLoader, Seed, UNETLoader, CLIPTextEncode, VAELoader, CLIPLoader, KSampler, SaveImage, VAEDecode, TextEncodeQwenImageEdit, CLIPTextEncode, ModelSamplingAuraFlow, KSampler, VAEDecode, SaveImage, EmptySD3LatentImage, GetImageSize, LoadImage, ImageScale, PreviewImage]
patterns: [image_to_image]
missing: []
parameters: {"cfg": 2.5, "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 698612145549055, "steps": 20}
---

# 图片生成/图生图/qwen-image-edit对比kontext，改变人物姿势效果对比_1963924005965189122.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/qwen-image-edit对比kontext，改变人物姿势效果对比_1963924005965189122.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（26 个）：
- `ConditioningZeroOut`
- `VAEEncode` ★核心
- `ReferenceLatent`
- `FluxGuidance`
- `VAELoader`
- `UNETLoader` ★核心
- `DualCLIPLoader`
- `Seed`
- `UNETLoader` ★核心
- `CLIPTextEncode` ★核心
- `VAELoader`
- `CLIPLoader`
- `KSampler` ★核心
- `SaveImage`
- `VAEDecode` ★核心
- `TextEncodeQwenImageEdit`
- `CLIPTextEncode` ★核心
- `ModelSamplingAuraFlow`
- `KSampler` ★核心
- `VAEDecode` ★核心
- `SaveImage`
- `EmptySD3LatentImage`
- `GetImageSize`
- `LoadImage`
- `ImageScale`
- `PreviewImage`

**识别到的模式**：image_to_image

## 关键参数

- `seed` = `698612145549055`
- `steps` = `20`
- `cfg` = `2.5`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **96%**（25/26）

**有卡**：`ConditioningZeroOut`、`VAEEncode`、`ReferenceLatent`、`FluxGuidance`、`VAELoader`、`UNETLoader`、`DualCLIPLoader`、`Seed`、`CLIPTextEncode`、`CLIPLoader`、`KSampler`、`SaveImage`、`VAEDecode`、`TextEncodeQwenImageEdit`、`ModelSamplingAuraFlow`、`EmptySD3LatentImage`、`GetImageSize`、`LoadImage`、`ImageScale`

**用到的条目**：KSampler、VAEDecode、VAELoader、UNETLoader、CLIPTextEncode、CLIPLoader、ConditioningZeroOut、LoadImage
