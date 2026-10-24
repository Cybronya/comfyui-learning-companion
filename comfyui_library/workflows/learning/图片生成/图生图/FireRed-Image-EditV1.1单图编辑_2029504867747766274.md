---
key: 图片生成/图生图/FireRed-Image-EditV1.1单图编辑_2029504867747766274.json
name: FireRed-Image-EditV1.1单图编辑_2029504867747766274
type: Image To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/FireRed-Image-EditV1.1单图编辑_2029504867747766274.json
hash: 01101b1683193c6c
coverage: 0.708333
learned_at: 2026-10-23 10:55:44
nodes: [VAELoader, ModelSamplingAuraFlow, TextEncodeQwenImageEditPlus, ComfySwitchNode, PrimitiveInt, VAEDecode, CFGNorm, PrimitiveBoolean, FluxKontextImageScale, VAEEncode, ComfySwitchNode, PrimitiveInt, PrimitiveFloat, PrimitiveFloat, KSampler, ComfySwitchNode, SaveImage, UNETLoader, LoraLoaderModelOnly, CLIPLoader, LoadImage, LoadImage, TextEncodeQwenImageEditPlus, LoadImage]
patterns: [image_to_image]
missing: []
parameters: {"cfg": 4, "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 43, "steps": 40}
---

# 图片生成/图生图/FireRed-Image-EditV1.1单图编辑_2029504867747766274.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/FireRed-Image-EditV1.1单图编辑_2029504867747766274.json`

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
- `PrimitiveBoolean`
- `FluxKontextImageScale`
- `VAEEncode` ★核心
- `ComfySwitchNode`
- `PrimitiveInt`
- `PrimitiveFloat`
- `PrimitiveFloat`
- `KSampler` ★核心
- `ComfySwitchNode`
- `SaveImage`
- `UNETLoader` ★核心
- `LoraLoaderModelOnly` ★核心
- `CLIPLoader`
- `LoadImage`
- `LoadImage`
- `TextEncodeQwenImageEditPlus`
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

覆盖率 **71%**（17/24）

**有卡**：`VAELoader`、`ModelSamplingAuraFlow`、`TextEncodeQwenImageEditPlus`、`VAEDecode`、`CFGNorm`、`PrimitiveBoolean`、`FluxKontextImageScale`、`VAEEncode`、`KSampler`、`SaveImage`、`UNETLoader`、`LoraLoaderModelOnly`、`CLIPLoader`、`LoadImage`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、UNETLoader、CLIPLoader、LoadImage、CFGNorm
