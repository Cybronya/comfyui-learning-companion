---
key: 图片生成/文生图/F.2klein9b自动溶图打光一致性_2058899052313530370.json
name: F.2klein9b自动溶图打光一致性_2058899052313530370
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/F.2klein9b自动溶图打光一致性_2058899052313530370.json
hash: 7b19307b4c86875f
coverage: 0.904762
learned_at: 2026-10-19 23:02:18
nodes: [CLIPLoader, Note, VAELoader, VAEEncode, ReferenceLatent, GetImageSize, Flux2Scheduler, KSamplerSelect, BasicGuider, easy positive, UNETLoader, CLIPTextEncode, Image Comparer (rgthree), LayerUtility: ImageScaleByAspectRatio V2, Int, RandomNoise, LoraLoaderModelOnly, SamplerCustomAdvanced, VAEDecode, SaveImage, LoadImage]
patterns: []
missing: []
---

# 图片生成/文生图/F.2klein9b自动溶图打光一致性_2058899052313530370.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/F.2klein9b自动溶图打光一致性_2058899052313530370.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（21 个）：
- `CLIPLoader`
- `Note`
- `VAELoader`
- `VAEEncode` ★核心
- `ReferenceLatent`
- `GetImageSize`
- `Flux2Scheduler`
- `KSamplerSelect` ★核心
- `BasicGuider`
- `easy positive`
- `UNETLoader` ★核心
- `CLIPTextEncode` ★核心
- `Image Comparer (rgthree)`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `Int`
- `RandomNoise`
- `LoraLoaderModelOnly` ★核心
- `SamplerCustomAdvanced` ★核心
- `VAEDecode` ★核心
- `SaveImage`
- `LoadImage`

## 知识

覆盖率 **90%**（19/21）

**有卡**：`CLIPLoader`、`VAELoader`、`VAEEncode`、`ReferenceLatent`、`GetImageSize`、`Flux2Scheduler`、`KSamplerSelect`、`BasicGuider`、`easy positive`、`UNETLoader`、`CLIPTextEncode`、`LayerUtility: ImageScaleByAspectRatio V2`、`Int`、`RandomNoise`、`LoraLoaderModelOnly`、`SamplerCustomAdvanced`、`VAEDecode`、`SaveImage`、`LoadImage`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、UNETLoader、CLIPTextEncode、CLIPLoader、LoadImage、KSamplerSelect
