---
key: 平台全量/双图编辑版（全能编辑模型 VS flux.2klein）_2019336417431789570.json
name: 双图编辑版（全能编辑模型 VS flux.2klein）_2019336417431789570
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/双图编辑版（全能编辑模型 VS flux.2klein）_2019336417431789570.json
hash: 4c718b0e5814e119
coverage: 0.923077
learned_at: 2026-11-14 01:50:51
nodes: [CFGGuider, RandomNoise, KSamplerSelect, ReferenceLatent, ReferenceLatent, SamplerCustomAdvanced, GetImageSize, VAEEncode, ReferenceLatent, ReferenceLatent, PrimitiveInt, LoadImage, CLIPTextEncode, ImageResize+, VAELoader, CLIPLoader, Flux2Scheduler, EmptyFlux2LatentImage, VAEEncode, CLIPTextEncode, UNETLoader, VAEDecode, SaveImage, LayerUtility: ImageReelComposit, CR Text, StringFunction|pysssss, ImageResize+, PreviewImage, LayerUtility: ImageReel, LoadImage, SaveImage, RH_Captioner, PreviewImage, CR Text, RH_Nano_Banana2_Image2Image, LoadImage, LoadImage, LayerUtility: ImageReelComposit, LayerUtility: ImageReel]
patterns: []
missing: []
---

# 平台全量/双图编辑版（全能编辑模型 VS flux.2klein）_2019336417431789570.json

> 来源文件 `comfyui_library/workflows/平台全量/双图编辑版（全能编辑模型 VS flux.2klein）_2019336417431789570.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（39 个）：
- `CFGGuider`
- `RandomNoise`
- `KSamplerSelect` ★核心
- `ReferenceLatent`
- `ReferenceLatent`
- `SamplerCustomAdvanced` ★核心
- `GetImageSize`
- `VAEEncode` ★核心
- `ReferenceLatent`
- `ReferenceLatent`
- `PrimitiveInt`
- `LoadImage`
- `CLIPTextEncode` ★核心
- `ImageResize+`
- `VAELoader`
- `CLIPLoader`
- `Flux2Scheduler`
- `EmptyFlux2LatentImage`
- `VAEEncode` ★核心
- `CLIPTextEncode` ★核心
- `UNETLoader` ★核心
- `VAEDecode` ★核心
- `SaveImage`
- `LayerUtility: ImageReelComposit`
- `CR Text`
- `StringFunction|pysssss`
- `ImageResize+`
- `PreviewImage`
- `LayerUtility: ImageReel`
- `LoadImage`
- `SaveImage`
- `RH_Captioner`
- `PreviewImage`
- `CR Text`
- `RH_Nano_Banana2_Image2Image`
- `LoadImage`
- `LoadImage`
- `LayerUtility: ImageReelComposit`
- `LayerUtility: ImageReel`

## 知识

覆盖率 **92%**（36/39）

**有卡**：`CFGGuider`、`RandomNoise`、`KSamplerSelect`、`ReferenceLatent`、`SamplerCustomAdvanced`、`GetImageSize`、`VAEEncode`、`LoadImage`、`CLIPTextEncode`、`ImageResize+`、`VAELoader`、`CLIPLoader`、`Flux2Scheduler`、`EmptyFlux2LatentImage`、`UNETLoader`、`VAEDecode`、`SaveImage`、`LayerUtility: ImageReelComposit`、`CR Text`、`StringFunction|pysssss`、`LayerUtility: ImageReel`、`RH_Captioner`、`RH_Nano_Banana2_Image2Image`

**用到的条目**：VAEDecode、VAELoader、UNETLoader、CLIPLoader、CLIPTextEncode、LoadImage、CFGGuider、KSamplerSelect
