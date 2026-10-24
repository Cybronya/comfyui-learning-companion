---
key: 图片生成/图生图/精细表情控制_PixelSmile-Base-Workflows_2039269966586843138.json
name: 精细表情控制_PixelSmile-Base-Workflows_2039269966586843138
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/精细表情控制_PixelSmile-Base-Workflows_2039269966586843138.json
hash: ad24348ea8615e88
coverage: 0.774194
learned_at: 2026-10-23 13:21:07
nodes: [Anything Everywhere, EasyCache, ImageResizeKJv2, SetNode, GetNode, GetNode, PathchSageAttentionKJ, VAELoader, ReservedVRAMSetter, GGUFLoaderKJ, KSamplerSelect, VAEDecode, SamplerCustomAdvanced, CFGGuider, LoadImage, ConditioningZeroOut, LoraLoaderModelOnly, BasicScheduler, CLIPLoader, LoraLoaderModelOnly, TextEncodeQwenImageEditPlus, TextEncodeQwenImageEditPlus, FluxKontextImageScale, ResolutionMaster, VAEEncode, RandomNoise, PreviewImage, PreviewImageOutputNnegret, PreviewImage, PreviewImage, PixelSmileConditioning]
patterns: []
missing: []
---

# 图片生成/图生图/精细表情控制_PixelSmile-Base-Workflows_2039269966586843138.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/精细表情控制_PixelSmile-Base-Workflows_2039269966586843138.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（31 个）：
- `Anything Everywhere`
- `EasyCache`
- `ImageResizeKJv2`
- `SetNode`
- `GetNode`
- `GetNode`
- `PathchSageAttentionKJ`
- `VAELoader`
- `ReservedVRAMSetter`
- `GGUFLoaderKJ`
- `KSamplerSelect` ★核心
- `VAEDecode` ★核心
- `SamplerCustomAdvanced` ★核心
- `CFGGuider`
- `LoadImage`
- `ConditioningZeroOut`
- `LoraLoaderModelOnly` ★核心
- `BasicScheduler`
- `CLIPLoader`
- `LoraLoaderModelOnly` ★核心
- `TextEncodeQwenImageEditPlus`
- `TextEncodeQwenImageEditPlus`
- `FluxKontextImageScale`
- `ResolutionMaster`
- `VAEEncode` ★核心
- `RandomNoise`
- `PreviewImage`
- `PreviewImageOutputNnegret`
- `PreviewImage`
- `PreviewImage`
- `PixelSmileConditioning`

## 知识

覆盖率 **77%**（24/31）

**有卡**：`EasyCache`、`ImageResizeKJv2`、`PathchSageAttentionKJ`、`VAELoader`、`ReservedVRAMSetter`、`GGUFLoaderKJ`、`KSamplerSelect`、`VAEDecode`、`SamplerCustomAdvanced`、`CFGGuider`、`LoadImage`、`ConditioningZeroOut`、`LoraLoaderModelOnly`、`BasicScheduler`、`CLIPLoader`、`TextEncodeQwenImageEditPlus`、`FluxKontextImageScale`、`ResolutionMaster`、`VAEEncode`、`RandomNoise`、`PreviewImageOutputNnegret`、`PixelSmileConditioning`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPLoader、ConditioningZeroOut、LoadImage、CFGGuider、KSamplerSelect
