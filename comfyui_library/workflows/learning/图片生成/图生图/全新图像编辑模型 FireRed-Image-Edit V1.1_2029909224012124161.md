---
key: 图片生成/图生图/全新图像编辑模型 FireRed-Image-Edit V1.1_2029909224012124161.json
name: 全新图像编辑模型 FireRed-Image-Edit V1.1_2029909224012124161
type: Image To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/全新图像编辑模型 FireRed-Image-Edit V1.1_2029909224012124161.json
hash: ece75840554ddd37
coverage: 0.807692
learned_at: 2026-10-23 12:13:13
nodes: [ModelSamplingAuraFlow, TextEncodeQwenImageEditPlus, CFGNorm, PrimitiveInt, PrimitiveInt, Switch any [Crystools], Switch any [Crystools], PrimitiveFloat, VAEDecode, SaveImage, Switch any [Crystools], LoraLoaderModelOnly, CLIPLoader, KSampler, PrimitiveBoolean, LoraLoaderModelOnly, LoadImage, UNETLoader, Fast Groups Bypasser (rgthree), VAELoader, FluxKontextImageScale, PrimitiveFloat, VAEEncode, LoadImage, LoadImage, TextEncodeQwenImageEditPlus]
patterns: [image_to_image]
missing: []
parameters: {"cfg": 4, "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 323539247414515, "steps": 40}
---

# 图片生成/图生图/全新图像编辑模型 FireRed-Image-Edit V1.1_2029909224012124161.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/全新图像编辑模型 FireRed-Image-Edit V1.1_2029909224012124161.json`

## 结构

**生成流程**：Model → Encode → Sampling → Decode → Output → Other

**节点**（26 个）：
- `ModelSamplingAuraFlow`
- `TextEncodeQwenImageEditPlus`
- `CFGNorm`
- `PrimitiveInt`
- `PrimitiveInt`
- `Switch any [Crystools]`
- `Switch any [Crystools]`
- `PrimitiveFloat`
- `VAEDecode` ★核心
- `SaveImage`
- `Switch any [Crystools]`
- `LoraLoaderModelOnly` ★核心
- `CLIPLoader`
- `KSampler` ★核心
- `PrimitiveBoolean`
- `LoraLoaderModelOnly` ★核心
- `LoadImage`
- `UNETLoader` ★核心
- `Fast Groups Bypasser (rgthree)`
- `VAELoader`
- `FluxKontextImageScale`
- `PrimitiveFloat`
- `VAEEncode` ★核心
- `LoadImage`
- `LoadImage`
- `TextEncodeQwenImageEditPlus`

**识别到的模式**：image_to_image

## 关键参数

- `seed` = `323539247414515`
- `steps` = `40`
- `cfg` = `4`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **81%**（21/26）

**有卡**：`ModelSamplingAuraFlow`、`TextEncodeQwenImageEditPlus`、`CFGNorm`、`Switch any [Crystools]`、`VAEDecode`、`SaveImage`、`LoraLoaderModelOnly`、`CLIPLoader`、`KSampler`、`PrimitiveBoolean`、`LoadImage`、`UNETLoader`、`VAELoader`、`FluxKontextImageScale`、`VAEEncode`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、UNETLoader、CLIPLoader、LoadImage、CFGNorm
