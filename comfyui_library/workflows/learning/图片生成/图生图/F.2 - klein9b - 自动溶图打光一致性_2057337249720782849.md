---
key: 图片生成/图生图/F.2 - klein9b - 自动溶图打光一致性_2057337249720782849.json
name: F.2 - klein9b - 自动溶图打光一致性_2057337249720782849
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/F.2 - klein9b - 自动溶图打光一致性_2057337249720782849.json
hash: 1462ebb7d4338554
coverage: 0.904762
learned_at: 2026-10-23 10:52:39
nodes: [CLIPLoader, Note, VAELoader, VAEEncode, ReferenceLatent, GetImageSize, Flux2Scheduler, KSamplerSelect, BasicGuider, easy positive, UNETLoader, CLIPTextEncode, Image Comparer (rgthree), LayerUtility: ImageScaleByAspectRatio V2, Int, RandomNoise, LoraLoaderModelOnly, SamplerCustomAdvanced, VAEDecode, SaveImage, LoadImage]
patterns: []
missing: []
---

# 图片生成/图生图/F.2 - klein9b - 自动溶图打光一致性_2057337249720782849.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/F.2 - klein9b - 自动溶图打光一致性_2057337249720782849.json`

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
