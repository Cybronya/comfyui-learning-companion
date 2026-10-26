---
key: 数字人/数字人/小红书编辑模型FireRed Image Edit 1.1 8步加速_2029994284878929921.json
name: 小红书编辑模型FireRed Image Edit 1.1 8步加速_2029994284878929921
type: Image To Image
status: completed
source: json
file: comfyui_library/workflows/数字人/数字人/小红书编辑模型FireRed Image Edit 1.1 8步加速_2029994284878929921.json
hash: 66c9c7e74971fab7
coverage: 0.807692
learned_at: 2026-10-26 02:01:59
nodes: [ModelSamplingAuraFlow, TextEncodeQwenImageEditPlus, CFGNorm, FluxKontextImageScale, VAEEncode, PrimitiveInt, PrimitiveInt, Switch any [Crystools], Switch any [Crystools], PrimitiveFloat, PrimitiveFloat, VAELoader, CLIPLoader, LoadImage, LoadImage, VAEDecode, KSampler, SaveImage, PrimitiveBoolean, LoraLoaderModelOnly, Fast Groups Bypasser (rgthree), TextEncodeQwenImageEditPlus, Switch any [Crystools], LoraLoaderModelOnly, UNETLoader, LoadImage]
patterns: [image_to_image]
missing: []
parameters: {"cfg": 4, "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 43, "steps": 40}
---

# 数字人/数字人/小红书编辑模型FireRed Image Edit 1.1 8步加速_2029994284878929921.json

> 来源文件 `comfyui_library/workflows/数字人/数字人/小红书编辑模型FireRed Image Edit 1.1 8步加速_2029994284878929921.json`

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
- `PrimitiveBoolean`
- `LoraLoaderModelOnly` ★核心
- `Fast Groups Bypasser (rgthree)`
- `TextEncodeQwenImageEditPlus`
- `Switch any [Crystools]`
- `LoraLoaderModelOnly` ★核心
- `UNETLoader` ★核心
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

**有卡**：`ModelSamplingAuraFlow`、`TextEncodeQwenImageEditPlus`、`CFGNorm`、`FluxKontextImageScale`、`VAEEncode`、`Switch any [Crystools]`、`VAELoader`、`CLIPLoader`、`LoadImage`、`VAEDecode`、`KSampler`、`SaveImage`、`PrimitiveBoolean`、`LoraLoaderModelOnly`、`UNETLoader`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、UNETLoader、CLIPLoader、LoadImage、CFGNorm
