---
key: 图片生成/文生图/FireRed Image Edit 1.1 8步加速_2073313339664584705.json
name: FireRed Image Edit 1.1 8步加速_2073313339664584705
type: Image To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/FireRed Image Edit 1.1 8步加速_2073313339664584705.json
hash: 90099ab272aaf775
coverage: 0.807692
learned_at: 2026-10-20 00:01:11
nodes: [ModelSamplingAuraFlow, TextEncodeQwenImageEditPlus, CFGNorm, FluxKontextImageScale, VAEEncode, PrimitiveInt, PrimitiveInt, Switch any [Crystools], Switch any [Crystools], PrimitiveFloat, PrimitiveFloat, VAELoader, CLIPLoader, LoadImage, LoadImage, VAEDecode, KSampler, SaveImage, LoadImage, PrimitiveBoolean, LoraLoaderModelOnly, Fast Groups Bypasser (rgthree), TextEncodeQwenImageEditPlus, Switch any [Crystools], LoraLoaderModelOnly, UNETLoader]
patterns: [image_to_image]
missing: []
parameters: {"cfg": 4, "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 43, "steps": 40}
---

# 图片生成/文生图/FireRed Image Edit 1.1 8步加速_2073313339664584705.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/FireRed Image Edit 1.1 8步加速_2073313339664584705.json`

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
- `LoadImage`
- `LoadImage`
- `VAEDecode` ★核心
- `KSampler` ★核心
- `SaveImage`
- `LoadImage`
- `PrimitiveBoolean`
- `LoraLoaderModelOnly` ★核心
- `Fast Groups Bypasser (rgthree)`
- `TextEncodeQwenImageEditPlus`
- `Switch any [Crystools]`
- `LoraLoaderModelOnly` ★核心
- `UNETLoader` ★核心

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

**有卡**：`ModelSamplingAuraFlow`、`TextEncodeQwenImageEditPlus`、`CFGNorm`、`FluxKontextImageScale`、`VAEEncode`、`Switch any [Crystools]`、`VAELoader`、`CLIPLoader`、`LoadImage`、`VAEDecode`、`KSampler`、`SaveImage`、`PrimitiveBoolean`、`LoraLoaderModelOnly`、`UNETLoader`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、UNETLoader、CLIPLoader、LoadImage、CFGNorm
