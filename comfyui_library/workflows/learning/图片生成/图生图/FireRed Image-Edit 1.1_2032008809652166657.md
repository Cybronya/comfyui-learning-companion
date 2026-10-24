---
key: 图片生成/图生图/FireRed Image-Edit 1.1_2032008809652166657.json
name: FireRed Image-Edit 1.1_2032008809652166657
type: Image To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/FireRed Image-Edit 1.1_2032008809652166657.json
hash: 88f68fc173ad6352
coverage: 0.666667
learned_at: 2026-10-23 10:55:27
nodes: [ComfySwitchNode, PrimitiveFloat, PrimitiveFloat, KSampler, VAEDecode, ComfySwitchNode, ModelSamplingAuraFlow, CFGNorm, VAEEncode, ComfySwitchNode, PrimitiveInt, PrimitiveInt, TextEncodeQwenImageEditPlus, CLIPLoader, UNETLoader, LoraLoaderModelOnly, SaveImage, VAELoader, LoadImage, LoadImage, Note, PrimitiveBoolean, LoadImage, ImageScale, TextEncodeQwenImageEditPlus, ImageScale, DF_Get_image_size, ImageScale, PrimitiveInt, PrimitiveInt]
patterns: [image_to_image]
missing: []
parameters: {"cfg": 4, "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 43, "steps": 40}
---

# 图片生成/图生图/FireRed Image-Edit 1.1_2032008809652166657.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/FireRed Image-Edit 1.1_2032008809652166657.json`

## 结构

**生成流程**：Model → Encode → Sampling → Decode → Process → Output → Other

**节点**（30 个）：
- `ComfySwitchNode`
- `PrimitiveFloat`
- `PrimitiveFloat`
- `KSampler` ★核心
- `VAEDecode` ★核心
- `ComfySwitchNode`
- `ModelSamplingAuraFlow`
- `CFGNorm`
- `VAEEncode` ★核心
- `ComfySwitchNode`
- `PrimitiveInt`
- `PrimitiveInt`
- `TextEncodeQwenImageEditPlus`
- `CLIPLoader`
- `UNETLoader` ★核心
- `LoraLoaderModelOnly` ★核心
- `SaveImage`
- `VAELoader`
- `LoadImage`
- `LoadImage`
- `Note`
- `PrimitiveBoolean`
- `LoadImage`
- `ImageScale`
- `TextEncodeQwenImageEditPlus`
- `ImageScale`
- `DF_Get_image_size`
- `ImageScale`
- `PrimitiveInt`
- `PrimitiveInt`

**识别到的模式**：image_to_image

## 关键参数

- `seed` = `43`
- `steps` = `40`
- `cfg` = `4`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **67%**（20/30）

**有卡**：`KSampler`、`VAEDecode`、`ModelSamplingAuraFlow`、`CFGNorm`、`VAEEncode`、`TextEncodeQwenImageEditPlus`、`CLIPLoader`、`UNETLoader`、`LoraLoaderModelOnly`、`SaveImage`、`VAELoader`、`LoadImage`、`PrimitiveBoolean`、`ImageScale`、`DF_Get_image_size`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPLoader、LoadImage、UNETLoader、CFGNorm
