---
key: 图片生成/文生图/Moss + QwenImage2.1 文生+图片编辑_2112165438787510273.json
name: Moss + QwenImage2.1 文生+图片编辑_2112165438787510273
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/Moss + QwenImage2.1 文生+图片编辑_2112165438787510273.json
hash: 4ec88a2356427d0c
coverage: 0.717391
learned_at: 2026-10-21 02:53:45
nodes: [VAELoader, CLIPTextEncode, CLIPTextEncode, EmptyLatentImage, ResolutionSelector, VAEDecode, SaveImage, PrimitiveStringMultiline, SamplerCustomAdvanced, RandomNoise, ManualSigmas, CFGGuider, KSamplerSelect, PrimitiveStringMultiline, ComfySwitchNode, easy isNone, VAELoader, easy showAnything, TextEncodeQwenImage21, ComfySwitchNode, ComfySwitchNode, ComfySwitchNode, ComfySwitchNode, ComfySwitchNode, TextGenerate, CLIPLoader, LoadImage, LoadImage, LoadImage, Any Switch (rgthree), LoadImage, LoadImage, LoadImage, CLIPLoader, LoadImage, LoadImage, UNETLoader, LoraLoaderModelOnly, SkipLayerGuidanceDiTSimple, UNETLoader, ComfySwitchNode, LoadImage, easy showAnything, JsonExtractString, PrimitiveStringMultiline, CLIPLoader]
patterns: []
missing: []
parameters: {"batch_size": 1, "height": 1024, "width": 1024}
---

# 图片生成/文生图/Moss + QwenImage2.1 文生+图片编辑_2112165438787510273.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/Moss + QwenImage2.1 文生+图片编辑_2112165438787510273.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Output → Other

**节点**（46 个）：
- `VAELoader`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `EmptyLatentImage` ★核心
- `ResolutionSelector`
- `VAEDecode` ★核心
- `SaveImage`
- `PrimitiveStringMultiline`
- `SamplerCustomAdvanced` ★核心
- `RandomNoise`
- `ManualSigmas`
- `CFGGuider`
- `KSamplerSelect` ★核心
- `PrimitiveStringMultiline`
- `ComfySwitchNode`
- `easy isNone`
- `VAELoader`
- `easy showAnything`
- `TextEncodeQwenImage21`
- `ComfySwitchNode`
- `ComfySwitchNode`
- `ComfySwitchNode`
- `ComfySwitchNode`
- `ComfySwitchNode`
- `TextGenerate`
- `CLIPLoader`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `Any Switch (rgthree)`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `CLIPLoader`
- `LoadImage`
- `LoadImage`
- `UNETLoader` ★核心
- `LoraLoaderModelOnly` ★核心
- `SkipLayerGuidanceDiTSimple`
- `UNETLoader` ★核心
- `ComfySwitchNode`
- `LoadImage`
- `easy showAnything`
- `JsonExtractString`
- `PrimitiveStringMultiline`
- `CLIPLoader`

## 关键参数

- `width` = `1024`
- `height` = `1024`
- `batch_size` = `1`

## 知识

覆盖率 **72%**（33/46）

**有卡**：`VAELoader`、`CLIPTextEncode`、`EmptyLatentImage`、`ResolutionSelector`、`VAEDecode`、`SaveImage`、`SamplerCustomAdvanced`、`RandomNoise`、`ManualSigmas`、`CFGGuider`、`KSamplerSelect`、`easy isNone`、`TextEncodeQwenImage21`、`TextGenerate`、`CLIPLoader`、`LoadImage`、`UNETLoader`、`LoraLoaderModelOnly`、`SkipLayerGuidanceDiTSimple`、`JsonExtractString`

**用到的条目**：VAEDecode、TextEncodeQwenImage21、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、EmptyLatentImage、ResolutionSelector
