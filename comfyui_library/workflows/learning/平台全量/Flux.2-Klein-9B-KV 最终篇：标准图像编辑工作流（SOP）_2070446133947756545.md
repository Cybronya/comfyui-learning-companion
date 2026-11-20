---
key: 平台全量/Flux.2-Klein-9B-KV 最终篇：标准图像编辑工作流（SOP）_2070446133947756545.json
name: Flux.2-Klein-9B-KV 最终篇：标准图像编辑工作流（SOP）_2070446133947756545
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/Flux.2-Klein-9B-KV 最终篇：标准图像编辑工作流（SOP）_2070446133947756545.json
hash: 01b8b71bcad4a02c
coverage: 0.541667
learned_at: 2026-11-14 00:28:57
nodes: [SamplerCustom, GetNode, LoraLoaderModelOnly, SetNode, SetNode, VAEEncode, GetNode, GetNode, GetNode, Flux2Scheduler, KSamplerSelect, Image Comparer (rgthree), SetNode, SetNode, VAEEncode, SetNode, LoadImage, ImageResizeKJv2, GrowMaskWithBlur, CLIPTextEncode, SetNode, GetNode, MarkdownNote, ColorMatchV2, BasicScheduler, UNETLoader, CLIPLoader, ImageResizeKJv2, SetNode, SetNode, SetNode, Seed (rgthree), GetNode, GetNode, GetNode, LoadImage, SetLatentNoiseMask, PreviewImage, ReferenceLatent, ReferenceLatent, VAEDecode, SaveImage, easy promptLine, FluxKVCache, VAELoader, Anything Everywhere3, Reroute, ConditioningZeroOut]
patterns: []
missing: []
---

# 平台全量/Flux.2-Klein-9B-KV 最终篇：标准图像编辑工作流（SOP）_2070446133947756545.json

> 来源文件 `comfyui_library/workflows/平台全量/Flux.2-Klein-9B-KV 最终篇：标准图像编辑工作流（SOP）_2070446133947756545.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（48 个）：
- `SamplerCustom` ★核心
- `GetNode`
- `LoraLoaderModelOnly` ★核心
- `SetNode`
- `SetNode`
- `VAEEncode` ★核心
- `GetNode`
- `GetNode`
- `GetNode`
- `Flux2Scheduler`
- `KSamplerSelect` ★核心
- `Image Comparer (rgthree)`
- `SetNode`
- `SetNode`
- `VAEEncode` ★核心
- `SetNode`
- `LoadImage`
- `ImageResizeKJv2`
- `GrowMaskWithBlur`
- `CLIPTextEncode` ★核心
- `SetNode`
- `GetNode`
- `MarkdownNote`
- `ColorMatchV2`
- `BasicScheduler`
- `UNETLoader` ★核心
- `CLIPLoader`
- `ImageResizeKJv2`
- `SetNode`
- `SetNode`
- `SetNode`
- `Seed (rgthree)`
- `GetNode`
- `GetNode`
- `GetNode`
- `LoadImage`
- `SetLatentNoiseMask`
- `PreviewImage`
- `ReferenceLatent`
- `ReferenceLatent`
- `VAEDecode` ★核心
- `SaveImage`
- `easy promptLine`
- `FluxKVCache`
- `VAELoader`
- `Anything Everywhere3`
- `Reroute`
- `ConditioningZeroOut`

## 知识

覆盖率 **54%**（26/48）

**有卡**：`SamplerCustom`、`LoraLoaderModelOnly`、`VAEEncode`、`Flux2Scheduler`、`KSamplerSelect`、`LoadImage`、`ImageResizeKJv2`、`GrowMaskWithBlur`、`CLIPTextEncode`、`ColorMatchV2`、`BasicScheduler`、`UNETLoader`、`CLIPLoader`、`Seed (rgthree)`、`SetLatentNoiseMask`、`ReferenceLatent`、`VAEDecode`、`SaveImage`、`easy promptLine`、`FluxKVCache`、`VAELoader`、`ConditioningZeroOut`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、UNETLoader、CLIPLoader、CLIPTextEncode、ConditioningZeroOut、LoadImage
