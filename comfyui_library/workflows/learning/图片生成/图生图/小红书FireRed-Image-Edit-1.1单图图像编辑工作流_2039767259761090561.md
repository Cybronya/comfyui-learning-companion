---
key: 图片生成/图生图/小红书FireRed-Image-Edit-1.1单图图像编辑工作流_2039767259761090561.json
name: 小红书FireRed-Image-Edit-1.1单图图像编辑工作流_2039767259761090561
type: Image To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/小红书FireRed-Image-Edit-1.1单图图像编辑工作流_2039767259761090561.json
hash: a186401e71df25b2
coverage: 0.72
learned_at: 2026-10-23 12:49:06
nodes: [LoraLoaderModelOnly, CLIPLoader, PrimitiveInt, PrimitiveInt, PrimitiveFloat, PrimitiveFloat, ComfySwitchNode, ComfySwitchNode, VAELoader, ComfySwitchNode, ModelSamplingAuraFlow, CFGNorm, UNETLoader, VAEDecode, KSampler, SaveImage, PrimitiveBoolean, FluxKontextImageScale, VAEEncode, LoadImage, TextEncodeQwenImageEditPlus, TextEncodeQwenImageEditPlus, MuyeSizeSelector, INTConstant, INTConstant]
patterns: [image_to_image]
missing: []
parameters: {"cfg": 4, "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 864456405854015, "steps": 40}
---

# 图片生成/图生图/小红书FireRed-Image-Edit-1.1单图图像编辑工作流_2039767259761090561.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/小红书FireRed-Image-Edit-1.1单图图像编辑工作流_2039767259761090561.json`

## 结构

**生成流程**：Model → Encode → Sampling → Decode → Output → Other

**节点**（25 个）：
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

**识别到的模式**：image_to_image

## 关键参数

- `seed` = `864456405854015`
- `steps` = `40`
- `cfg` = `4`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **72%**（18/25）

**有卡**：`LoraLoaderModelOnly`、`CLIPLoader`、`VAELoader`、`ModelSamplingAuraFlow`、`CFGNorm`、`UNETLoader`、`VAEDecode`、`KSampler`、`SaveImage`、`PrimitiveBoolean`、`FluxKontextImageScale`、`VAEEncode`、`LoadImage`、`TextEncodeQwenImageEditPlus`、`MuyeSizeSelector`、`INTConstant`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、UNETLoader、CLIPLoader、LoadImage、CFGNorm
