---
key: 图片生成/图生图/FireRed Image Edit 1.1 8步加速_2031361650225319938.json
name: FireRed Image Edit 1.1 8步加速_2031361650225319938
type: Image To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/FireRed Image Edit 1.1 8步加速_2031361650225319938.json
hash: c63631a533d2384d
coverage: 0.807692
learned_at: 2026-10-23 10:55:25
nodes: [ModelSamplingAuraFlow, TextEncodeQwenImageEditPlus, CFGNorm, FluxKontextImageScale, VAEEncode, PrimitiveInt, PrimitiveInt, Switch any [Crystools], Switch any [Crystools], PrimitiveFloat, PrimitiveFloat, VAELoader, CLIPLoader, VAEDecode, KSampler, SaveImage, PrimitiveBoolean, LoraLoaderModelOnly, Fast Groups Bypasser (rgthree), TextEncodeQwenImageEditPlus, Switch any [Crystools], LoraLoaderModelOnly, UNETLoader, LoadImage, LoadImage, LoadImage]
patterns: [image_to_image]
missing: []
parameters: {"cfg": 4, "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 43, "steps": 40}
---

# 图片生成/图生图/FireRed Image Edit 1.1 8步加速_2031361650225319938.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/FireRed Image Edit 1.1 8步加速_2031361650225319938.json`

## 结构

**生成流程**：Model → Encode → Sampling → Decode → Output → Other

**节点**（26 个）：
- `ModelSamplingAuraFlow`
- `TextEncodeQwenImageEditPlus`
- `CFGNorm`
- `FluxKontextImageScale`
- `VAEEncode` ★核心
- `PrimitiveInt`
- `PrimitiveInt`
- `Switch any [Crystools]`
- `Switch any [Crystools]`
- `PrimitiveFloat`
- `PrimitiveFloat`
- `VAELoader`
- `CLIPLoader`
- `VAEDecode` ★核心
- `KSampler` ★核心
- `SaveImage`
- `PrimitiveBoolean`
- `LoraLoaderModelOnly` ★核心
- `Fast Groups Bypasser (rgthree)`
- `TextEncodeQwenImageEditPlus`
- `Switch any [Crystools]`
- `LoraLoaderModelOnly` ★核心
- `UNETLoader` ★核心
- `LoadImage`
- `LoadImage`
- `LoadImage`

**识别到的模式**：image_to_image

## 关键参数

- `seed` = `43`
- `steps` = `40`
- `cfg` = `4`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **81%**（21/26）

**有卡**：`ModelSamplingAuraFlow`、`TextEncodeQwenImageEditPlus`、`CFGNorm`、`FluxKontextImageScale`、`VAEEncode`、`Switch any [Crystools]`、`VAELoader`、`CLIPLoader`、`VAEDecode`、`KSampler`、`SaveImage`、`PrimitiveBoolean`、`LoraLoaderModelOnly`、`UNETLoader`、`LoadImage`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、UNETLoader、CLIPLoader、LoadImage、CFGNorm
