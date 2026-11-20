---
key: 平台全量/【阡陌】小红书FireRed-Image-Edit-1.1单图图像编辑工作流_2031303078774837250.json
name: 【阡陌】小红书FireRed-Image-Edit-1.1单图图像编辑工作流_2031303078774837250
type: Image To Image
status: completed
source: json
file: comfyui_library/workflows/平台全量/【阡陌】小红书FireRed-Image-Edit-1.1单图图像编辑工作流_2031303078774837250.json
hash: 6559ce62194d28ec
coverage: 0.708333
learned_at: 2026-11-14 01:26:29
nodes: [LoraLoaderModelOnly, CLIPLoader, PrimitiveInt, TextEncodeQwenImageEditPlus, PrimitiveInt, PrimitiveFloat, PrimitiveFloat, ComfySwitchNode, ComfySwitchNode, VAELoader, ComfySwitchNode, PrimitiveBoolean, LoadImage, ModelSamplingAuraFlow, CFGNorm, SaveImage, TextEncodeQwenImageEditPlus, UNETLoader, VAEDecode, FluxKontextImageScale, KSampler, VAEEncode, MuyeSizeSelector, LoadImage]
patterns: [image_to_image]
missing: []
parameters: {"cfg": 4, "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 43, "steps": 40}
---

# 平台全量/【阡陌】小红书FireRed-Image-Edit-1.1单图图像编辑工作流_2031303078774837250.json

> 来源文件 `comfyui_library/workflows/平台全量/【阡陌】小红书FireRed-Image-Edit-1.1单图图像编辑工作流_2031303078774837250.json`

## 结构

**生成流程**：Model → Encode → Sampling → Decode → Output → Other

**节点**（24 个）：
- `LoraLoaderModelOnly` ★核心
- `CLIPLoader`
- `PrimitiveInt`
- `TextEncodeQwenImageEditPlus`
- `PrimitiveInt`
- `PrimitiveFloat`
- `PrimitiveFloat`
- `ComfySwitchNode`
- `ComfySwitchNode`
- `VAELoader`
- `ComfySwitchNode`
- `PrimitiveBoolean`
- `LoadImage`
- `ModelSamplingAuraFlow`
- `CFGNorm`
- `SaveImage`
- `TextEncodeQwenImageEditPlus`
- `UNETLoader` ★核心
- `VAEDecode` ★核心
- `FluxKontextImageScale`
- `KSampler` ★核心
- `VAEEncode` ★核心
- `MuyeSizeSelector`
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

**有卡**：`LoraLoaderModelOnly`、`CLIPLoader`、`TextEncodeQwenImageEditPlus`、`VAELoader`、`PrimitiveBoolean`、`LoadImage`、`ModelSamplingAuraFlow`、`CFGNorm`、`SaveImage`、`UNETLoader`、`VAEDecode`、`FluxKontextImageScale`、`KSampler`、`VAEEncode`、`MuyeSizeSelector`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、UNETLoader、CLIPLoader、LoadImage、CFGNorm
