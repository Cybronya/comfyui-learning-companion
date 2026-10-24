---
key: 图片生成/图生图/firered-image-edit-1.1官方发布版_2030518527010021378.json
name: firered-image-edit-1.1官方发布版_2030518527010021378
type: Image To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/firered-image-edit-1.1官方发布版_2030518527010021378.json
hash: 1a0e47c8c35df124
coverage: 0.708333
learned_at: 2026-10-23 11:34:54
nodes: [ModelSamplingAuraFlow, TextEncodeQwenImageEditPlus, ComfySwitchNode, PrimitiveInt, SaveImage, VAEDecode, CFGNorm, PrimitiveBoolean, FluxKontextImageScale, VAEEncode, ComfySwitchNode, PrimitiveInt, PrimitiveFloat, PrimitiveFloat, KSampler, ComfySwitchNode, LoadImage, TextEncodeQwenImageEditPlus, LoadImage, LoadImage, CLIPLoader, VAELoader, LoraLoaderModelOnly, UNETLoader]
patterns: [image_to_image]
missing: []
parameters: {"cfg": 4, "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 43, "steps": 40}
---

# 图片生成/图生图/firered-image-edit-1.1官方发布版_2030518527010021378.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/firered-image-edit-1.1官方发布版_2030518527010021378.json`

## 结构

**生成流程**：Model → Encode → Sampling → Decode → Output → Other

**节点**（24 个）：
- `ModelSamplingAuraFlow`
- `TextEncodeQwenImageEditPlus`
- `ComfySwitchNode`
- `PrimitiveInt`
- `SaveImage`
- `VAEDecode` ★核心
- `CFGNorm`
- `PrimitiveBoolean`
- `FluxKontextImageScale`
- `VAEEncode` ★核心
- `ComfySwitchNode`
- `PrimitiveInt`
- `PrimitiveFloat`
- `PrimitiveFloat`
- `KSampler` ★核心
- `ComfySwitchNode`
- `LoadImage`
- `TextEncodeQwenImageEditPlus`
- `LoadImage`
- `LoadImage`
- `CLIPLoader`
- `VAELoader`
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

覆盖率 **71%**（17/24）

**有卡**：`ModelSamplingAuraFlow`、`TextEncodeQwenImageEditPlus`、`SaveImage`、`VAEDecode`、`CFGNorm`、`PrimitiveBoolean`、`FluxKontextImageScale`、`VAEEncode`、`KSampler`、`LoadImage`、`CLIPLoader`、`VAELoader`、`LoraLoaderModelOnly`、`UNETLoader`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、UNETLoader、CLIPLoader、LoadImage、CFGNorm
