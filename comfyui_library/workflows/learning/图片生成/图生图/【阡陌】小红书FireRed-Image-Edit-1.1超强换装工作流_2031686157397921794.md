---
key: 图片生成/图生图/【阡陌】小红书FireRed-Image-Edit-1.1超强换装工作流_2031686157397921794.json
name: 【阡陌】小红书FireRed-Image-Edit-1.1超强换装工作流_2031686157397921794
type: Image To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/【阡陌】小红书FireRed-Image-Edit-1.1超强换装工作流_2031686157397921794.json
hash: ef0a5e09aca7c134
coverage: 0.766667
learned_at: 2026-10-23 11:52:51
nodes: [LoraLoaderModelOnly, CLIPLoader, PrimitiveInt, PrimitiveInt, PrimitiveFloat, PrimitiveFloat, ComfySwitchNode, ComfySwitchNode, VAELoader, ComfySwitchNode, PrimitiveBoolean, ModelSamplingAuraFlow, CFGNorm, UNETLoader, VAEDecode, FluxKontextImageScale, KSampler, VAEEncode, MuyeSizeSelector, LoadImage, ConditioningZeroOut, LoadImage, LoadImage, LoadImage, TextEncodeQwenImageEditPlus, easy imageConcat, SaveImage, LoadImage, LoadImage, ImageConcatMulti]
patterns: [image_to_image]
missing: []
parameters: {"cfg": 4, "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 186799469750009, "steps": 40}
---

# 图片生成/图生图/【阡陌】小红书FireRed-Image-Edit-1.1超强换装工作流_2031686157397921794.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/【阡陌】小红书FireRed-Image-Edit-1.1超强换装工作流_2031686157397921794.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（30 个）：
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
- `PrimitiveBoolean`
- `ModelSamplingAuraFlow`
- `CFGNorm`
- `UNETLoader` ★核心
- `VAEDecode` ★核心
- `FluxKontextImageScale`
- `KSampler` ★核心
- `VAEEncode` ★核心
- `MuyeSizeSelector`
- `LoadImage`
- `ConditioningZeroOut`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `TextEncodeQwenImageEditPlus`
- `easy imageConcat`
- `SaveImage`
- `LoadImage`
- `LoadImage`
- `ImageConcatMulti`

**识别到的模式**：image_to_image

## 关键参数

- `seed` = `186799469750009`
- `steps` = `40`
- `cfg` = `4`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **77%**（23/30）

**有卡**：`LoraLoaderModelOnly`、`CLIPLoader`、`VAELoader`、`PrimitiveBoolean`、`ModelSamplingAuraFlow`、`CFGNorm`、`UNETLoader`、`VAEDecode`、`FluxKontextImageScale`、`KSampler`、`VAEEncode`、`MuyeSizeSelector`、`LoadImage`、`ConditioningZeroOut`、`TextEncodeQwenImageEditPlus`、`easy imageConcat`、`SaveImage`、`ImageConcatMulti`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、UNETLoader、CLIPLoader、ConditioningZeroOut、LoadImage
