---
key: 平台全量/图片编辑-动漫转真人-QwenImage2.1_MossImage_2117182910007701506.json
name: 图片编辑-动漫转真人-QwenImage2.1_MossImage_2117182910007701506
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/图片编辑-动漫转真人-QwenImage2.1_MossImage_2117182910007701506.json
hash: 1fe0af81c58719ac
coverage: 0.765432
learned_at: 2026-11-14 01:55:19
nodes: [LoadImage, easy cleanGpuUsed, VOSR2ModelLoader, VOSR2Upscale, Image Comparer (rgthree), Reroute, Reroute, Reroute, Reroute, ImpactMinMax, ImpactMinMax, GetImageSizeAndCount, ImageResizeKJv2, GetImageSizeAndCount, ImpactMinMax, ImageScaleToMaxDimension, Reroute, GetImageSizeAndCount, easy cleanGpuUsed, Image Comparer (rgthree), SaveImage, Reroute, UNETLoader, ModelAttentionBackend, LoraLoaderModelOnly, CLIPLoader, VAELoader, TextEncodeQwenImage21, PreviewImage, QwenImage21Cache, Seed (rgthree), KSamplerSelect, RandomNoise, CFGGuider, easy cleanGpuUsed, SamplerCustomAdvanced, VAEDecode, PreviewImage, Image Comparer (rgthree), Images to RGB, easy cleanGpuUsed, Reroute, ManualSigmas, ImageScaleToTotalPixels, easy cleanGpuUsed, Reroute, ModelAttentionBackend, SkipLayerGuidanceDiTSimple, CLIPLoader, VAELoader, CLIPTextEncode, CLIPTextEncode, Seed (rgthree), VAEEncode, VAEDecode, Image Comparer (rgthree), GetImageSizeAndCount, Reroute, easy cleanGpuUsed, LoraLoaderModelOnly, UNETLoader, UNETLoader, MOSSMergePreset, SamplerCustomAdvanced, CFGGuider, RandomNoise, KSamplerSelect, BasicScheduler, easy cleanGpuUsed, LoraLoaderModelOnly, LoadImage, Reroute, SeedVR2TorchCompileSettings, easy cleanGpuUsed, Note, Note, SeedVR2LoadDiTModel, SeedVR2LoadVAEModel, SeedVR2VideoUpscaler, SaveImage, Reroute]
patterns: []
missing: []
---

# 平台全量/图片编辑-动漫转真人-QwenImage2.1_MossImage_2117182910007701506.json

> 来源文件 `comfyui_library/workflows/平台全量/图片编辑-动漫转真人-QwenImage2.1_MossImage_2117182910007701506.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（81 个）：
- `LoadImage`
- `easy cleanGpuUsed`
- `VOSR2ModelLoader`
- `VOSR2Upscale`
- `Image Comparer (rgthree)`
- `Reroute`
- `Reroute`
- `Reroute`
- `Reroute`
- `ImpactMinMax`
- `ImpactMinMax`
- `GetImageSizeAndCount`
- `ImageResizeKJv2`
- `GetImageSizeAndCount`
- `ImpactMinMax`
- `ImageScaleToMaxDimension`
- `Reroute`
- `GetImageSizeAndCount`
- `easy cleanGpuUsed`
- `Image Comparer (rgthree)`
- `SaveImage`
- `Reroute`
- `UNETLoader` ★核心
- `ModelAttentionBackend`
- `LoraLoaderModelOnly` ★核心
- `CLIPLoader`
- `VAELoader`
- `TextEncodeQwenImage21`
- `PreviewImage`
- `QwenImage21Cache`
- `Seed (rgthree)`
- `KSamplerSelect` ★核心
- `RandomNoise`
- `CFGGuider`
- `easy cleanGpuUsed`
- `SamplerCustomAdvanced` ★核心
- `VAEDecode` ★核心
- `PreviewImage`
- `Image Comparer (rgthree)`
- `Images to RGB`
- `easy cleanGpuUsed`
- `Reroute`
- `ManualSigmas`
- `ImageScaleToTotalPixels`
- `easy cleanGpuUsed`
- `Reroute`
- `ModelAttentionBackend`
- `SkipLayerGuidanceDiTSimple`
- `CLIPLoader`
- `VAELoader`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `Seed (rgthree)`
- `VAEEncode` ★核心
- `VAEDecode` ★核心
- `Image Comparer (rgthree)`
- `GetImageSizeAndCount`
- `Reroute`
- `easy cleanGpuUsed`
- `LoraLoaderModelOnly` ★核心
- `UNETLoader` ★核心
- `UNETLoader` ★核心
- `MOSSMergePreset`
- `SamplerCustomAdvanced` ★核心
- `CFGGuider`
- `RandomNoise`
- `KSamplerSelect` ★核心
- `BasicScheduler`
- `easy cleanGpuUsed`
- `LoraLoaderModelOnly` ★核心
- `LoadImage`
- `Reroute`
- `SeedVR2TorchCompileSettings`
- `easy cleanGpuUsed`
- `Note`
- `Note`
- `SeedVR2LoadDiTModel`
- `SeedVR2LoadVAEModel`
- `SeedVR2VideoUpscaler`
- `SaveImage`
- `Reroute`

## 知识

覆盖率 **77%**（62/81）

**有卡**：`LoadImage`、`easy cleanGpuUsed`、`VOSR2ModelLoader`、`VOSR2Upscale`、`ImpactMinMax`、`GetImageSizeAndCount`、`ImageResizeKJv2`、`ImageScaleToMaxDimension`、`SaveImage`、`UNETLoader`、`ModelAttentionBackend`、`LoraLoaderModelOnly`、`CLIPLoader`、`VAELoader`、`TextEncodeQwenImage21`、`QwenImage21Cache`、`Seed (rgthree)`、`KSamplerSelect`、`RandomNoise`、`CFGGuider`、`SamplerCustomAdvanced`、`VAEDecode`、`Images to RGB`、`ManualSigmas`、`ImageScaleToTotalPixels`、`SkipLayerGuidanceDiTSimple`、`CLIPTextEncode`、`VAEEncode`、`MOSSMergePreset`、`BasicScheduler`、`SeedVR2TorchCompileSettings`、`SeedVR2LoadDiTModel`、`SeedVR2LoadVAEModel`、`SeedVR2VideoUpscaler`

**用到的条目**：TextEncodeQwenImage21、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPLoader、CLIPTextEncode、LoadImage、QwenImage21Cache
