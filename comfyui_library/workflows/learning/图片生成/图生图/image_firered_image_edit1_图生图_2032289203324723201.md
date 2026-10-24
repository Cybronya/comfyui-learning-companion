---
key: 图片生成/图生图/image_firered_image_edit1_图生图_2032289203324723201.json
name: image_firered_image_edit1_图生图_2032289203324723201
type: Image To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/image_firered_image_edit1_图生图_2032289203324723201.json
hash: 95de651dda076617
coverage: 0.681818
learned_at: 2026-10-23 11:37:51
nodes: [ModelSamplingAuraFlow, ComfySwitchNode, PrimitiveInt, CFGNorm, ComfySwitchNode, PrimitiveInt, PrimitiveFloat, PrimitiveFloat, ComfySwitchNode, VAELoader, CLIPLoader, LoraLoaderModelOnly, UNETLoader, VAEEncode, PrimitiveBoolean, TextEncodeQwenImageEditPlus, TextEncodeQwenImageEditPlus, KSampler, VAEDecode, FluxKontextImageScale, SaveImage, LoadImage]
patterns: [image_to_image]
missing: []
parameters: {"cfg": 4, "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 43, "steps": 40}
---

# 图片生成/图生图/image_firered_image_edit1_图生图_2032289203324723201.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/image_firered_image_edit1_图生图_2032289203324723201.json`

## 结构

**生成流程**：Model → Encode → Sampling → Decode → Output → Other

**节点**（22 个）：
- `ModelSamplingAuraFlow`
- `ComfySwitchNode`
- `PrimitiveInt`
- `CFGNorm`
- `ComfySwitchNode`
- `PrimitiveInt`
- `PrimitiveFloat`
- `PrimitiveFloat`
- `ComfySwitchNode`
- `VAELoader`
- `CLIPLoader`
- `LoraLoaderModelOnly` ★核心
- `UNETLoader` ★核心
- `VAEEncode` ★核心
- `PrimitiveBoolean`
- `TextEncodeQwenImageEditPlus`
- `TextEncodeQwenImageEditPlus`
- `KSampler` ★核心
- `VAEDecode` ★核心
- `FluxKontextImageScale`
- `SaveImage`
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

覆盖率 **68%**（15/22）

**有卡**：`ModelSamplingAuraFlow`、`CFGNorm`、`VAELoader`、`CLIPLoader`、`LoraLoaderModelOnly`、`UNETLoader`、`VAEEncode`、`PrimitiveBoolean`、`TextEncodeQwenImageEditPlus`、`KSampler`、`VAEDecode`、`FluxKontextImageScale`、`SaveImage`、`LoadImage`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、UNETLoader、CLIPLoader、LoadImage、CFGNorm
