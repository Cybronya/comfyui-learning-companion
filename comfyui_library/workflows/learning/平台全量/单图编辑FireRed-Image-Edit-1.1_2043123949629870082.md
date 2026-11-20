---
key: 平台全量/单图编辑FireRed-Image-Edit-1.1_2043123949629870082.json
name: 单图编辑FireRed-Image-Edit-1.1_2043123949629870082
type: Image To Image
status: completed
source: json
file: comfyui_library/workflows/平台全量/单图编辑FireRed-Image-Edit-1.1_2043123949629870082.json
hash: deb8f99b5c8ad466
coverage: 0.730769
learned_at: 2026-11-14 01:48:34
nodes: [LoraLoaderModelOnly, CLIPLoader, PrimitiveInt, PrimitiveInt, PrimitiveFloat, PrimitiveFloat, ComfySwitchNode, ComfySwitchNode, VAELoader, ComfySwitchNode, ModelSamplingAuraFlow, CFGNorm, VAEDecode, KSampler, PrimitiveBoolean, FluxKontextImageScale, VAEEncode, TextEncodeQwenImageEditPlus, MuyeSizeSelector, TextEncodeQwenImageEditPlus, INTConstant, TextEncodeQwenImageEditPlus, SaveImage, UNETLoader, LoadImage, INTConstant]
patterns: [image_to_image]
missing: []
parameters: {"cfg": 4, "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 906577678661566, "steps": 40}
---

# 平台全量/单图编辑FireRed-Image-Edit-1.1_2043123949629870082.json

> 来源文件 `comfyui_library/workflows/平台全量/单图编辑FireRed-Image-Edit-1.1_2043123949629870082.json`

## 结构

**生成流程**：Model → Encode → Sampling → Decode → Output → Other

**节点**（26 个）：
- `LoraLoaderModelOnly` ★核心
- `CLIPLoader`
- `PrimitiveInt`
- `PrimitiveInt`
- `PrimitiveFloat`
- `PrimitiveFloat`
- `ComfySwitchNode`
- `ComfySwitchNode`
- `VAELoader`
- `ComfySwitchNode`
- `ModelSamplingAuraFlow`
- `CFGNorm`
- `VAEDecode` ★核心
- `KSampler` ★核心
- `PrimitiveBoolean`
- `FluxKontextImageScale`
- `VAEEncode` ★核心
- `TextEncodeQwenImageEditPlus`
- `MuyeSizeSelector`
- `TextEncodeQwenImageEditPlus`
- `INTConstant`
- `TextEncodeQwenImageEditPlus`
- `SaveImage`
- `UNETLoader` ★核心
- `LoadImage`
- `INTConstant`

**识别到的模式**：image_to_image

## 关键参数

- `seed` = `906577678661566`
- `steps` = `40`
- `cfg` = `4`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **73%**（19/26）

**有卡**：`LoraLoaderModelOnly`、`CLIPLoader`、`VAELoader`、`ModelSamplingAuraFlow`、`CFGNorm`、`VAEDecode`、`KSampler`、`PrimitiveBoolean`、`FluxKontextImageScale`、`VAEEncode`、`TextEncodeQwenImageEditPlus`、`MuyeSizeSelector`、`INTConstant`、`SaveImage`、`UNETLoader`、`LoadImage`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、UNETLoader、CLIPLoader、LoadImage、CFGNorm
