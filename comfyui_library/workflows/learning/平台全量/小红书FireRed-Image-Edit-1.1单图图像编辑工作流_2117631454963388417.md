---
key: 平台全量/小红书FireRed-Image-Edit-1.1单图图像编辑工作流_2117631454963388417.json
name: 小红书FireRed-Image-Edit-1.1单图图像编辑工作流_2117631454963388417
type: Image To Image
status: completed
source: json
file: comfyui_library/workflows/平台全量/小红书FireRed-Image-Edit-1.1单图图像编辑工作流_2117631454963388417.json
hash: 6de20ea58d8b83be
coverage: 0.757576
learned_at: 2026-11-14 02:01:21
nodes: [LoraLoaderModelOnly, CLIPLoader, PrimitiveInt, PrimitiveInt, PrimitiveFloat, PrimitiveFloat, ComfySwitchNode, ComfySwitchNode, VAELoader, ComfySwitchNode, ModelSamplingAuraFlow, CFGNorm, UNETLoader, VAEDecode, KSampler, SaveImage, PrimitiveBoolean, FluxKontextImageScale, VAEEncode, LoadImage, TextEncodeQwenImageEditPlus, TextEncodeQwenImageEditPlus, MuyeSizeSelector, INTConstant, INTConstant, LoraLoaderModelOnly, LoraLoaderModelOnly, easy anythingIndexSwitch, LazyCache, ModelAttentionBackend, FluxKontextImageScale, LoadImage, ComfySwitchNode]
patterns: [image_to_image]
missing: []
parameters: {"cfg": 4, "denoise": 1, "sampler_name": "er_sde", "scheduler": "beta57", "seed": 822382850343272, "steps": 40}
---

# 平台全量/小红书FireRed-Image-Edit-1.1单图图像编辑工作流_2117631454963388417.json

> 来源文件 `comfyui_library/workflows/平台全量/小红书FireRed-Image-Edit-1.1单图图像编辑工作流_2117631454963388417.json`

## 结构

**生成流程**：Model → Encode → Sampling → Decode → Output → Other

**节点**（33 个）：
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
- `UNETLoader` ★核心
- `VAEDecode` ★核心
- `KSampler` ★核心
- `SaveImage`
- `PrimitiveBoolean`
- `FluxKontextImageScale`
- `VAEEncode` ★核心
- `LoadImage`
- `TextEncodeQwenImageEditPlus`
- `TextEncodeQwenImageEditPlus`
- `MuyeSizeSelector`
- `INTConstant`
- `INTConstant`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `easy anythingIndexSwitch`
- `LazyCache`
- `ModelAttentionBackend`
- `FluxKontextImageScale`
- `LoadImage`
- `ComfySwitchNode`

**识别到的模式**：image_to_image

## 关键参数

- `seed` = `822382850343272`
- `steps` = `40`
- `cfg` = `4`
- `sampler_name` = `er_sde`
- `scheduler` = `beta57`
- `denoise` = `1`

## 知识

覆盖率 **76%**（25/33）

**有卡**：`LoraLoaderModelOnly`、`CLIPLoader`、`VAELoader`、`ModelSamplingAuraFlow`、`CFGNorm`、`UNETLoader`、`VAEDecode`、`KSampler`、`SaveImage`、`PrimitiveBoolean`、`FluxKontextImageScale`、`VAEEncode`、`LoadImage`、`TextEncodeQwenImageEditPlus`、`MuyeSizeSelector`、`INTConstant`、`easy anythingIndexSwitch`、`LazyCache`、`ModelAttentionBackend`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、UNETLoader、CLIPLoader、LoadImage、CFGNorm
