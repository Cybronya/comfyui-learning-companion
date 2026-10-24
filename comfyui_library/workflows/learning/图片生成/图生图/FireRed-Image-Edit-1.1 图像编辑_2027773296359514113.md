---
key: 图片生成/图生图/FireRed-Image-Edit-1.1 图像编辑_2027773296359514113.json
name: FireRed-Image-Edit-1.1 图像编辑_2027773296359514113
type: Image To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/FireRed-Image-Edit-1.1 图像编辑_2027773296359514113.json
hash: ec735bbba91363f9
coverage: 0.708333
learned_at: 2026-10-23 10:55:42
nodes: [VAELoader, ModelSamplingAuraFlow, TextEncodeQwenImageEditPlus, ComfySwitchNode, PrimitiveInt, VAEDecode, CFGNorm, LoadImage, PrimitiveBoolean, FluxKontextImageScale, VAEEncode, ComfySwitchNode, PrimitiveInt, PrimitiveFloat, PrimitiveFloat, ComfySwitchNode, LoraLoaderModelOnly, CLIPLoader, KSampler, SaveImage, LoadImage, TextEncodeQwenImageEditPlus, LoadImage, UNETLoader]
patterns: [image_to_image]
missing: []
parameters: {"cfg": 4, "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 15523038380465, "steps": 40}
---

# 图片生成/图生图/FireRed-Image-Edit-1.1 图像编辑_2027773296359514113.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/FireRed-Image-Edit-1.1 图像编辑_2027773296359514113.json`

## 结构

**生成流程**：Model → Encode → Sampling → Decode → Output → Other

**节点**（24 个）：
- `VAELoader`
- `ModelSamplingAuraFlow`
- `TextEncodeQwenImageEditPlus`
- `ComfySwitchNode`
- `PrimitiveInt`
- `VAEDecode` ★核心
- `CFGNorm`
- `LoadImage`
- `PrimitiveBoolean`
- `FluxKontextImageScale`
- `VAEEncode` ★核心
- `ComfySwitchNode`
- `PrimitiveInt`
- `PrimitiveFloat`
- `PrimitiveFloat`
- `ComfySwitchNode`
- `LoraLoaderModelOnly` ★核心
- `CLIPLoader`
- `KSampler` ★核心
- `SaveImage`
- `LoadImage`
- `TextEncodeQwenImageEditPlus`
- `LoadImage`
- `UNETLoader` ★核心

**识别到的模式**：image_to_image

## 关键参数

- `seed` = `15523038380465`
- `steps` = `40`
- `cfg` = `4`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **71%**（17/24）

**有卡**：`VAELoader`、`ModelSamplingAuraFlow`、`TextEncodeQwenImageEditPlus`、`VAEDecode`、`CFGNorm`、`LoadImage`、`PrimitiveBoolean`、`FluxKontextImageScale`、`VAEEncode`、`LoraLoaderModelOnly`、`CLIPLoader`、`KSampler`、`SaveImage`、`UNETLoader`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、UNETLoader、CLIPLoader、LoadImage、CFGNorm
