---
key: 平台全量/一键提取人物衣服-One click extraction of character clothin_2031573125279780865.json
name: 一键提取人物衣服-One click extraction of character clothin_2031573125279780865
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/一键提取人物衣服-One click extraction of character clothin_2031573125279780865.json
hash: 20fe007b1eb2520d
coverage: 0.761905
learned_at: 2026-11-14 01:28:50
nodes: [SaveImage, KSamplerSelect, SamplerCustomAdvanced, RandomNoise, VAELoader, EmptyFlux2LatentImage, CFGGuider, Flux2Scheduler, CLIPTextEncode, ConditioningZeroOut, GetImageSize, ReferenceLatent, LayerUtility: ImageReel, LayerUtility: ImageReelComposit, CR Text, Fast Groups Bypasser (rgthree), easy imageScaleDownToSize, VAEEncode, VAEDecode, Image Comparer (rgthree), SaveImage, SaveImage, Image Comparer (rgthree), SeedVR2VideoUpscaler, SeedVR2LoadVAEModel, SeedVR2LoadDiTModel, easy cleanGpuUsed, easy cleanGpuUsed, SetNode, SetNode, SetNode, GetNode, GetNode, GetNode, GetNode, UNETLoader, CLIPLoader, LoraLoaderModelOnly, LoraLoaderModelOnly, ReferenceLatent, JWInteger, LoadImage]
patterns: []
missing: []
---

# 平台全量/一键提取人物衣服-One click extraction of character clothin_2031573125279780865.json

> 来源文件 `comfyui_library/workflows/平台全量/一键提取人物衣服-One click extraction of character clothin_2031573125279780865.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（42 个）：
- `SaveImage`
- `KSamplerSelect` ★核心
- `SamplerCustomAdvanced` ★核心
- `RandomNoise`
- `VAELoader`
- `EmptyFlux2LatentImage`
- `CFGGuider`
- `Flux2Scheduler`
- `CLIPTextEncode` ★核心
- `ConditioningZeroOut`
- `GetImageSize`
- `ReferenceLatent`
- `LayerUtility: ImageReel`
- `LayerUtility: ImageReelComposit`
- `CR Text`
- `Fast Groups Bypasser (rgthree)`
- `easy imageScaleDownToSize`
- `VAEEncode` ★核心
- `VAEDecode` ★核心
- `Image Comparer (rgthree)`
- `SaveImage`
- `SaveImage`
- `Image Comparer (rgthree)`
- `SeedVR2VideoUpscaler`
- `SeedVR2LoadVAEModel`
- `SeedVR2LoadDiTModel`
- `easy cleanGpuUsed`
- `easy cleanGpuUsed`
- `SetNode`
- `SetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `UNETLoader` ★核心
- `CLIPLoader`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `ReferenceLatent`
- `JWInteger`
- `LoadImage`

## 知识

覆盖率 **76%**（32/42）

**有卡**：`SaveImage`、`KSamplerSelect`、`SamplerCustomAdvanced`、`RandomNoise`、`VAELoader`、`EmptyFlux2LatentImage`、`CFGGuider`、`Flux2Scheduler`、`CLIPTextEncode`、`ConditioningZeroOut`、`GetImageSize`、`ReferenceLatent`、`LayerUtility: ImageReel`、`LayerUtility: ImageReelComposit`、`CR Text`、`easy imageScaleDownToSize`、`VAEEncode`、`VAEDecode`、`SeedVR2VideoUpscaler`、`SeedVR2LoadVAEModel`、`SeedVR2LoadDiTModel`、`easy cleanGpuUsed`、`UNETLoader`、`CLIPLoader`、`LoraLoaderModelOnly`、`JWInteger`、`LoadImage`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、UNETLoader、CLIPLoader、CLIPTextEncode、ConditioningZeroOut、LoadImage
